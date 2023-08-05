#  Copyright (c) 2022 Push Technology Ltd., All Rights Reserved.
#
#  Use is subject to license terms.
#
#  NOTICE: All information contained herein is, and remains the
#  property of Push Technology. The intellectual and technical
#  concepts contained herein are proprietary to Push Technology and
#  may be covered by U.S. and Foreign Patents, patents in process, and
#  are protected by trade secret or copyright law.

from __future__ import annotations

import functools
import io
import typing

import stringcase

import diffusion.datatypes
from diffusion.handlers import LOG
from diffusion.internal.utils import BaseConfig

if typing.TYPE_CHECKING:  # pragma: no cover
    from diffusion.internal.services.abstract import (
        ServiceValue,
    )
    from diffusion.internal.serialisers.base import Serialiser
    from .attrs import MarshalledModel as AttrsModel
    from .pydantic import MarshalledModel as PydanticModel

    Model_Variants = typing.Union[AttrsModel, PydanticModel]
    Model_Variants_T = typing.TypeVar("Model_Variants_T", bound=Model_Variants)

from diffusion.internal.serialisers import T

GenericModel_T = typing.TypeVar("GenericModel_T", bound="GenericModel")
GenericModel_T_Other = typing.TypeVar("GenericModel_T_Other", bound="GenericModel")


def model_variants() -> typing.Tuple[typing.Type[Model_Variants], ...]:
    from .attrs import MarshalledModel as AttrsModel
    from .pydantic import MarshalledModel as PydanticModel

    return AttrsModel, PydanticModel


class GenericConfig(
    typing.Generic[GenericModel_T],
    BaseConfig,
):
    """
    Adds Serialiser support to Model.Config
    'alias' defines the name of the serialiser to map to
    """

    alias: typing.ClassVar[str]
    allow_population_by_field_name = True
    alias_generator = stringcase.spinalcase

    @classmethod
    def verify_item(cls, item, modelcls):
        try:
            assert item._serialiser.name in cls.attr_mappings_all(modelcls)
        except Exception as e:  # pragma: no cover
            LOG.error(f"Got exception {e}")
            raise

    @classmethod
    @functools.lru_cache(maxsize=None)
    def serialiser(cls, name=None) -> "Serialiser":
        from diffusion.internal.serialisers.base import Serialiser

        if not name:
            assert isinstance(cls.alias, str)
        return Serialiser.by_name(name or cls.alias)

    @classmethod
    def to_bytes(cls, item: GenericModel_T, serialiser=None) -> bytes:
        as_tuple = cls.as_tuple(item, serialiser=serialiser)
        return cls.serialiser(serialiser).to_bytes(*as_tuple)

    @classmethod
    def from_service_value(
        cls,
        modelcls: typing.Type[GenericModel_T],
        item: ServiceValue,
    ) -> GenericModel_T:
        fields = cls.get_fields(item, modelcls)
        try:
            return modelcls.from_fields(**fields)
        except Exception as e:  # pragma: no cover
            LOG.error(f"Got exception {e}")
            raise

    @classmethod
    def get_fields(cls, item, modelcls):
        cls.verify_item(item, modelcls)
        mapping = cls.get_model_to_serialiser_mapping(
            modelcls, serialiser=item._serialiser.name
        )
        fields = cls.gen_fields(
            item,
            mapping,
            modelcls,
        )
        try:
            assert fields
            assert all(x is not None for x in fields.keys())
        except Exception as e:  # pragma: no cover
            LOG.error(f"Got exception {e}")
            raise
        return fields

    @classmethod
    def gen_fields(cls, item, model_to_serialiser_mapping, modelcls):
        try:
            result = {
                model_key: modelcls.Config.decode(item[serialiser_key])
                for model_key, serialiser_key in model_to_serialiser_mapping.items()
                if serialiser_key
            }
            assert all(x is not None for x in result.keys())
            return result
        except Exception as e:  # pragma: no cover
            LOG.error(f"Got exception {e}")
            raise

    @classmethod
    def from_tuple(
        cls,
        modelcls: typing.Type[GenericModel_T],
        tp: typing.Tuple[typing.Any, ...],
        serialiser=None,
    ) -> GenericModel_T:
        sv = cls.service_value(serialiser).evolve(*tp)
        result = cls.from_service_value(modelcls, sv)
        return result

    @classmethod
    def fields_from_tuple(
        cls,
        modelcls: typing.Type[GenericModel_T_Other],
        tp: typing.Tuple[typing.Any, ...],
        serialiser=None,
    ) -> typing.Mapping[str, typing.Any]:
        sv = cls.service_value(serialiser).evolve(*tp)
        result = cls.get_fields(sv, modelcls)
        return result

    @classmethod
    def read(
        cls,
        modelcls: typing.Type[GenericModel_T],
        stream: io.BytesIO,
        serialiser=None,
    ) -> GenericModel_T:
        return cls.from_tuple(
            modelcls, tuple(cls.serialiser(serialiser).read(stream)), serialiser
        )

    @classmethod
    @functools.lru_cache(maxsize=None)
    def find_aliases(
        cls, modelcls: typing.Type[GenericModel_T], serialiser: typing.Optional[str]
    ) -> typing.Mapping[str, str]:
        return {}

    @classmethod
    @functools.lru_cache(maxsize=None)
    def get_model_to_serialiser_mapping(
        cls, modelcls: typing.Type[Model_Variants], serialiser=None
    ):
        try:
            final_mapping = modelcls.Config.attr_mappings_final(
                modelcls, serialiser=serialiser
            )
            result = {}
            for serialiser_key, model_key in final_mapping.items():
                final_model_key = getattr(model_key, "__name__", model_key)
                final_serialiser_key = cls.sanitize_key(serialiser_key, serialiser)
                if not (final_serialiser_key and final_model_key):
                    continue
                result.update({final_model_key: final_serialiser_key})

            assert all(x is not None for x in result.keys())
            assert all(x is not None for x in result.values())
            return result
        except Exception as e:  # pragma: no cover
            raise e

    @classmethod
    def sanitize_key(cls, name: str, serialiser=None):
        sv = cls.service_value(serialiser)
        result = sv.sanitize_key(name)
        if result:
            return result
        if cls.alias_generator:
            result = sv.sanitize_key(cls.alias_generator(name))
        if not result:  # pragma: no cover
            LOG.error(f"Couldn't find {name} in {sv.spec}")
        return result

    @classmethod
    @functools.lru_cache(maxsize=None)
    def field_names(
        cls, modelcls: typing.Type[GenericModel_T], serialiser=None
    ) -> typing.List[str]:
        raise NotImplementedError()  # pragma: no cover

    @classmethod
    def get_service_value_args(cls, item: Model_Variants, serialiser=None):
        model_to_serialiser_mapping = cls.get_model_to_serialiser_mapping(
            type(item), serialiser=serialiser
        )
        try:
            mappings = {
                v: cls.as_service_value_field(getattr(item, k), serialiser=v)
                for k, v in model_to_serialiser_mapping.items()
            }  # NOQA
        except Exception as e:  # pragma: no cover
            raise e
        return mappings

    @classmethod
    def as_service_value_field(cls, item: GenericModel_T, serialiser: str = None):
        if isinstance(item, diffusion.datatypes.AbstractDataType):
            return item.encode(item.value)
        elif isinstance(item, GenericModel):
            return item.Config.as_tuple(item, serialiser)
        return item

    @classmethod
    def as_service_value(
        cls: typing.Type[GenericConfig[GenericModel_T]],
        item: GenericModel_T,
        serialiser=None,
    ) -> ServiceValue:
        sv = cls.service_value(serialiser)
        mappings = cls.get_service_value_args(
            typing.cast("Model_Variants", item), serialiser=serialiser
        )
        try:
            return sv.evolve(**mappings)
        except Exception as e:  # pragma: no cover
            LOG.error(f"Caught exception {e}")
            raise

    @classmethod
    def as_tuple(
        cls, item: GenericModel_T, serialiser=None
    ) -> typing.Tuple[typing.Any, ...]:
        return tuple(cls.as_service_value(item, serialiser=serialiser).values())

    @classmethod
    @functools.lru_cache(maxsize=None)
    def get_spec(cls, modelcls: typing.Type["Model_Variants"], serialiser=None):
        rev_mapping = {
            getattr(v, "__name__", v): k
            for k, v in cls.attr_mappings_final(modelcls, serialiser).items()
        }
        spec = [
            rev_mapping.get(
                x,
                rev_mapping.get(cls.alias_generator(x), x),
            )
            for x in cls.field_names(modelcls)
        ]
        return list(filter(bool, spec))

    @classmethod
    @functools.lru_cache(maxsize=None)
    def attr_mappings_final(
        cls, modelcls: typing.Type[Model_Variants], serialiser=None
    ) -> typing.Dict[str, typing.Any]:
        try:
            attr_mapping = cls.attr_mappings_all(modelcls).get(serialiser or cls.alias)
            result = {**(attr_mapping or {})}
            updates = cls.find_aliases(modelcls, serialiser)
            result.update({k: v for k, v in updates.items() if k and v})
            assert all([x for x in result.keys()])
            assert all([x for x in result.values()])
            return result
        except Exception as e:  # pragma: no cover
            raise e

    @classmethod
    @functools.lru_cache(maxsize=None)
    def service_value(cls, serialiser=None):
        from diffusion.internal.services.abstract import ServiceValue

        return ServiceValue(cls.serialiser(serialiser))

    @classmethod
    def attr_mappings_all(cls, modelcls):
        return {cls.alias: modelcls.attr_mappings()}


class GenericModel(object):
    class Config(GenericConfig):
        pass

    def to_bytes(self) -> bytes:
        return self.Config.to_bytes(self)

    @classmethod
    def from_fields(cls: typing.Type[T], **kwargs) -> T:
        # noinspection PyArgumentList
        try:
            return cls(**kwargs)
        except Exception as e:  # pragma: no cover
            LOG.error(f"Got exception {e}")
            raise

    @classmethod
    def attr_mappings(cls) -> typing.Dict[str, typing.Any]:
        return {}

    @classmethod
    def from_service_value(
        cls: typing.Type[GenericModel_T], item: ServiceValue
    ) -> GenericModel_T:
        return cls.Config.from_service_value(cls, item)

    @classmethod
    def from_tuple(
        cls: typing.Type[GenericModel],
        tp: typing.Tuple[typing.Any, ...],
    ):
        result = cls.Config.from_tuple(cls, tp)
        return result


class GenericMetaModel(type):
    Config: typing.Type[GenericConfig]

    # noinspection PyAbstractClass
    def __new__(
        mcs,
        name: str,
        bases: typing.Tuple[type, ...],
        namespace: typing.Dict[str, typing.Any],
        **kwds,
    ) -> typing.Type[GenericModel]:
        result = super().__new__(mcs, name, bases, namespace, **kwds)

        class ConcreteConfig(result.Config):  # type: ignore
            _modelcls = result

        result.Config = ConcreteConfig
        return typing.cast(typing.Type[GenericModel], result)
