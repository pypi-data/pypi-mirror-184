""" Module for defining serialisers.

    The key component is the `SERIALISER_SPECS` mapping, which is based on
    the specification in `spec.clj`.
"""
from __future__ import annotations

from typing import TypeVar

from typing_extensions import Protocol

import typing

if typing.TYPE_CHECKING:
    from .base import Serialiser
    from ..services import ServiceValue

T = TypeVar("T")


def get_serialiser(name: str = None) -> Serialiser:
    from .spec import NULL_VALUE_KEY

    """ Retrieve a serialiser instance based on the spec name. """
    from .base import Serialiser

    return Serialiser.by_name(
        NULL_VALUE_KEY if name is None else name
    )


class Serialisable(Protocol):
    @classmethod
    def from_fields(cls: typing.Type[T], **kwargs) -> T:
        pass  # pragma: no cover

    @classmethod
    def attr_mappings(cls) -> typing.Dict[str, typing.Any]:
        pass  # pragma: no cover

    @classmethod
    def from_service_value(
        cls: typing.Type[T], item: ServiceValue
    ) -> T:
        pass  # pragma: no cover


Serialisable_T = TypeVar(
    "Serialisable_T", bound=Serialisable
)
