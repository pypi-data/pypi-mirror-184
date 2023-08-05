#   Copyright (c) 2022 Push Technology Ltd., All Rights Reserved.
#
#   Use is subject to license terms.
#
#  NOTICE: All information contained herein is, and remains the
#  property of Push Technology. The intellectual and technical
#  concepts contained herein are proprietary to Push Technology and
#  may be covered by U.S. and Foreign Patents, patents in process, and
#  are protected by trade secret or copyright law.

import enum

from diffusion.internal.serialisers.pydantic import MarshalledModel


class SessionLockScope(enum.IntEnum):
    """
    Values for the `scope` parameter of
    [Session.lock][diffusion.session.Session.lock]

    Since:
        6.10
    """

    UNLOCK_ON_SESSION_LOSS = 0
    """
    The lock will be released when the acquiring session loses its
    current connection to the server.
    """

    UNLOCK_ON_CONNECTION_LOSS = 1
    """
    The lock will be released when the acquiring session is closed.
    """

    def __str__(self):
        return self.name


class Bool(MarshalledModel):
    value: bool

    def __bool__(self):
        return self.value

    class Config(MarshalledModel.Config):
        alias_generator = None

        @classmethod
        def attr_mappings_all(cls, modelcls):
            return {"boolean": {"boolean": "value"}}


class SessionLockAcquisition(MarshalledModel):
    """
    The successful response of a
    [SessionLockRequest][diffusion.session.locks.session_lock_request.SessionLockRequest]
    """

    lock_name: str
    sequence: int
    scope: SessionLockScope

    class Config(MarshalledModel.Config):
        frozen = True
        alias_generator = None

        @classmethod
        def attr_mappings_all(cls, modelcls):
            return {
                "session-lock-acquisition": {
                    "session-lock-name": "lock_name",
                    "session-lock-sequence": "sequence",
                    "session-lock-scope": "scope",
                }
            }

    def __str__(self):
        return (
            f"""SessionLockAcquisition[{self.lock_name}, {self.sequence}, {self.scope}"""
        )
