#   Copyright (c) 2022 Push Technology Ltd., All Rights Reserved.
#
#   Use is subject to license terms.
#
#  NOTICE: All information contained herein is, and remains the
#  property of Push Technology. The intellectual and technical
#  concepts contained herein are proprietary to Push Technology and
#  may be covered by U.S. and Foreign Patents, patents in process, and
#  are protected by trade secret or copyright law.

from __future__ import annotations

import collections
import collections.abc
import functools
import itertools
import typing

import pydantic.dataclasses
from typing_extensions import overload

from diffusion.datatypes import AbstractDataType
from diffusion.features.topics.update import UpdateConstraint, UpdateConstraint_T
from diffusion.internal.serialisers.dataclass_model import DataclassConfigMixin
from diffusion.internal.serialisers.generic_model import (
    GenericConfig
)
from diffusion.internal.services import ServiceValue
from diffusion.internal.utils import (
    validate_member_arguments,
    validate_member_arguments_configured,
    BaseConfig,
)
from diffusion.internal.validation import StrictNonNegativeInt
from diffusion.session.locks.session_locks import SessionLock

TypeGetter = typing.Callable[[typing.Any], typing.Type["AbstractDataType"]]


class ConstraintSingleton(typing.Generic[UpdateConstraint_T]):
    @functools.lru_cache(maxsize=None)
    def __get__(self, instance, owner) -> UpdateConstraint_T:
        return (owner or type(instance))()


class Unconstrained(UpdateConstraint):
    """
    The unconstrained update constraint.
    """

    Instance = typing.cast(typing.ClassVar[ConstraintSingleton], ConstraintSingleton())
    ID: typing.ClassVar[int] = 0

    def __str__(self):
        return "Unconstrained"

    class Config(UpdateConstraint.Config["Unconstrained"]):
        @classmethod
        @functools.lru_cache(maxsize=None)
        def field_names(
            cls, modelcls: typing.Type[Unconstrained], serialiser=None
        ) -> typing.List[str]:
            return []

        @classmethod
        def attr_mappings_all(cls, modelcls):
            return {"unconstrained-constraint": {}}


ConjunctionConstraint_T = typing.TypeVar(
    "ConjunctionConstraint_T", bound="ConjunctionConstraint"
)


@pydantic.dataclasses.dataclass(config=BaseConfig, eq=True, frozen=True)
class ConjunctionConstraint(UpdateConstraint):
    constraints: typing.Tuple[UpdateConstraint, ...]
    ID: typing.ClassVar[int] = 1

    def __init__(
        self,
        constraints_begin: typing.Union[
            UpdateConstraint, typing.Tuple[UpdateConstraint, ...]
        ] = tuple(),
        second_term: typing.Optional[
            typing.Union[UpdateConstraint, typing.Tuple[UpdateConstraint, ...]]
        ] = tuple(),
    ):
        if isinstance(constraints_begin, UpdateConstraint):
            constraints_final = self.process_constraints(
                (*constraints_begin,), second_term
            )
        elif isinstance(constraints_begin, tuple):
            constraints_final = self.process_constraints(constraints_begin, second_term)
        else:
            constraints_final = constraints_begin
        object.__setattr__(self, "constraints", constraints_final)
        self.__pydantic_validate_values__()  # type: ignore
        object.__setattr__(self, "constraints", constraints_final)
        topic_constraints = self.get_topic_constraints()
        if len(list(zip(topic_constraints, range(2)))) > 1:
            raise ValueError(
                "Multiple topic constraints found: "
                f"{' and '.join(map(str, self.get_topic_constraints()))}."
            )

    @classmethod
    def process_constraints(
        cls, constraints_final, second_term
    ) -> typing.Tuple[UpdateConstraint, ...]:
        if not isinstance(second_term, collections.Iterable):
            second_term = (second_term,)
        constraints_final += sum(
            ((*y,) if y is not None else (None,) for y in itertools.chain(second_term)),
            (),
        )
        return constraints_final

    def __str__(self):
        return f"Constraints=({', '.join(str(x) for x in self.constraints)})"

    def __iter__(self):
        return iter(self.constraints)

    class Config(
        DataclassConfigMixin["ConjunctionConstraint"], UpdateConstraint.Config
    ):
        @classmethod
        def as_service_value(
            cls: typing.Type[GenericConfig[ConjunctionConstraint_T]],
            item: ConjunctionConstraint_T,
            serialiser=None,
        ) -> ServiceValue:
            result = (
                typing.cast(GenericConfig[ConjunctionConstraint_T], super())
            ).as_service_value(item, serialiser)
            if len(item.constraints):
                constraint_tuples: typing.Tuple[typing.Any, ...] = sum(
                    [(x.Config.as_tuple(x),) for x in item.constraints],
                    typing.cast(typing.Tuple[typing.Any, ...], tuple()),
                )
                result = result.evolve(**{"conjunction-constraint": constraint_tuples})
            return result


@pydantic.dataclasses.dataclass(frozen=True, eq=True)
class BinaryValueConstraint(UpdateConstraint):
    """
    The update constraint that requires the exact binary value.
    """

    bytes: pydantic.StrictBytes
    ID: typing.ClassVar[int] = 2
    IsTopicConstraint: typing.ClassVar[bool] = True

    def __iter__(self):
        return iter((self,))

    def __str__(self):
        return f"Bytes={self.bytes}"

    class Config(
        DataclassConfigMixin["BinaryValueConstraint"], UpdateConstraint.Config
    ):
        alias = "binary-value-constraint"

        @classmethod
        def attr_mappings_all(cls, modelcls: typing.Type[BinaryValueConstraint]):
            return {"binary-value-constraint": {"binary-value-constraint": "bytes"}}


class NoValueConstraint(UpdateConstraint):
    """
    The update constraint that requires a topic to have no value.
    """

    Instance = typing.cast(typing.ClassVar["NoValueConstraint"], ConstraintSingleton())
    ID: typing.ClassVar[int] = 3
    IsTopicConstraint: typing.ClassVar[bool] = True

    def __str__(self):
        return "NoValue"

    class Config(UpdateConstraint.Config["NoValueConstraint"]):
        @classmethod
        @functools.lru_cache(maxsize=None)
        def field_names(
            cls, modelcls: typing.Type[NoValueConstraint], serialiser=None
        ) -> typing.List[str]:
            return []

        @classmethod
        def attr_mappings_all(cls, modelcls: typing.Type[NoValueConstraint]):
            return {"no-value-constraint": {}}


@pydantic.dataclasses.dataclass(frozen=True)
class LockConstraint(UpdateConstraint):
    """
    The constraint on a [SessionLock][diffusion.session.locks.session_locks.SessionLock]
    """

    ID: typing.ClassVar[int] = 4
    name: pydantic.StrictStr
    sequence: StrictNonNegativeInt

    def _frozen_init(self, name: pydantic.StrictStr, sequence: StrictNonNegativeInt):
        object.__setattr__(self, "name", name)
        object.__setattr__(self, "sequence", sequence)

    @overload
    def __init__(self, session_lock: SessionLock):
        self._frozen_init(session_lock.name, session_lock.sequence)

    @overload
    def __init__(self, name: pydantic.StrictStr, sequence: StrictNonNegativeInt):
        self._frozen_init(name, sequence)

    @validate_member_arguments_configured(check_overloads=True)
    def __init__(
        self,
        *args: typing.Union[pydantic.StrictStr, StrictNonNegativeInt, SessionLock],
        **kwargs: typing.Union[pydantic.StrictStr, StrictNonNegativeInt, SessionLock],
    ):
        pass

    def __str__(self):
        return f"{type(self).__name__}(name='{self.name}', sequence={self.sequence})"

    class Config(DataclassConfigMixin["LockConstraint"], UpdateConstraint.Config):
        @classmethod
        def attr_mappings_all(cls, modelcls: typing.Type[LockConstraint]):
            return {
                "locked-constraint": {
                    "session-lock-name": "name",
                    "session-lock-sequence": "sequence",
                }
            }


class NoTopicConstraint(UpdateConstraint):
    """
    The update constraint that requires the path to have no topic.
    """

    Instance = typing.cast(typing.ClassVar["NoTopicConstraint"], ConstraintSingleton())
    ID: typing.ClassVar[int] = 5
    IsTopicConstraint: typing.ClassVar[bool] = True

    def __str__(self):
        return "NoTopic"

    class Config(DataclassConfigMixin["NoTopicConstraint"], UpdateConstraint.Config):
        @classmethod
        def attr_mappings_all(cls, modelcls: typing.Type[NoTopicConstraint]):
            return {"no-topic-constraint": {}}


WithValuesType = typing.Tuple[typing.Tuple[str, bytes], ...]


@pydantic.dataclasses.dataclass(config=BaseConfig, frozen=True, eq=True)
class PartialJSON(UpdateConstraint):
    """
    The constraint requiring the current value of the
    [JSON][diffusion.datatypes.JSON] topic to match the
    partially described value.
    """

    ID: typing.ClassVar[int] = 6
    IsTopicConstraint: typing.ClassVar[bool] = True

    with_values: WithValuesType
    without_values: typing.FrozenSet[str]

    @property
    def with_values_dict(self) -> collections.abc.Mapping:
        return dict(self.with_values)

    @validate_member_arguments_configured(config=BaseConfig)
    def __init__(
        self, with_values, without_values: typing.FrozenSet[str] = frozenset()
    ):
        object.__setattr__(self, "with_values", with_values)
        object.__setattr__(self, "without_values", without_values)
        self.__pydantic_validate_values__()  # type: ignore
        object.__setattr__(self, "with_values", with_values)
        object.__setattr__(self, "without_values", without_values)

    @validate_member_arguments
    def with_(
        self, pointer: pydantic.StrictStr, value: AbstractDataType
    ) -> "PartialJSON":
        """
        Requires a value at a specific position in the JSON object.

        Notes:
            The `pointer` is a JSON Pointer (https://tools.ietf.org/html/rfc6901) syntax reference
            locating the `value` in the JSON object.

            The `pointer` syntax is not being verified for correctness.

        Args:
            pointer: The pointer expression.
            value: The value.
        Returns:
            The constraint including the specified `pointer`.

        """  # NOQA
        new_with_values: typing.Dict[str, bytes] = {**dict(self.with_values)}
        new_without_values = frozenset(self.without_values)
        for k, v in self.with_values:
            new_with_values[k] = v
        new_with_values[pointer] = value.to_bytes()
        final_without_values = new_without_values - frozenset({pointer})
        return type(self)(tuple(new_with_values.items()), final_without_values)

    @validate_member_arguments
    def without(self, pointer: pydantic.StrictStr):
        """
        Requires a specific position in the JSON object to be empty.

        Notes:
            The `pointer` is a JSON Pointer (https://tools.ietf.org/html/rfc6901) syntax reference
            that should have no value in the JSON object.

            The `pointer` syntax is not being verified for correctness.

        Args:
            pointer: The pointer expression.
        Returns:
            The constraint including the specified `pointer`.
        """  # NOQA
        new_with_values = {k: v for k, v in self.with_values if k is not pointer}
        return type(self)(
            tuple(new_with_values.items()),
            self.without_values.union(frozenset({pointer})),
        )

    def __str__(self):
        return f"with_values={self.with_values}, without_values={self.without_values}"

    class Config(DataclassConfigMixin["PartialJSON"], UpdateConstraint.Config):
        @classmethod
        def attr_mappings_all(cls, modelcls: typing.Type[PartialJSON]):
            return {
                "partial-json-constraint": {
                    "partial-json-constraint-with": "with_values",
                    "partial-json-constraint-without": "without_values",
                }
            }
