#   Copyright (c) 2022 Push Technology Ltd., All Rights Reserved.
#
#   Use is subject to license terms.
#
#  NOTICE: All information contained herein is, and remains the
#  property of Push Technology. The intellectual and technical
#  concepts contained herein are proprietary to Push Technology and
#  may be covered by U.S. and Foreign Patents, patents in process, and
#  are protected by trade secret or copyright law.
import dataclasses
import functools
import typing

from diffusion.internal.serialisers.generic_model import GenericModel_T, GenericConfig


class DataclassConfigMixin(typing.Generic[GenericModel_T], GenericConfig[GenericModel_T]):
    @classmethod
    @functools.lru_cache(maxsize=None)
    def field_names(
            cls, modelcls: typing.Type[GenericModel_T], serialiser=None
    ) -> typing.List[str]:
        return [field.name for field in dataclasses.fields(modelcls)]
