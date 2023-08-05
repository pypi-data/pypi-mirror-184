# LOCK-BEGIN[imports]: DON'T MODIFY
from dexteritysdk.solmate.dtypes import Usize
from podite import (
    U128,
    U64,
    pod,
)

# LOCK-END


# LOCK-BEGIN[class(OpenOrdersNode)]: DON'T MODIFY
@pod
class OpenOrdersNode:
    id: U128
    qty: U64
    client_id: U64
    prev: Usize
    next: Usize
    # LOCK-END

    @classmethod
    def to_bytes(cls, obj, **kwargs):
        return cls.pack(obj, converter="bytes", **kwargs)

    @classmethod
    def from_bytes(cls, raw, **kwargs):
        return cls.unpack(raw, converter="bytes", **kwargs)
