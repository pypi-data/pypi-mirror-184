# LOCK-BEGIN[imports]: DON'T MODIFY
from podite import (
    I128,
    pod,
)

# LOCK-END


# LOCK-BEGIN[class(FastInt)]: DON'T MODIFY
@pod
class FastInt:
    value: I128
    # LOCK-END

    @classmethod
    def to_bytes(cls, obj, **kwargs):
        return cls.pack(obj, converter="bytes", **kwargs)

    @classmethod
    def from_bytes(cls, raw, **kwargs):
        return cls.unpack(raw, converter="bytes", **kwargs)
