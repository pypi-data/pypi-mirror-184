# LOCK-BEGIN[imports]: DON'T MODIFY
from dexteritysdk.codegen.dex.types.leg import Leg
from dexteritysdk.codegen.dex.types.product_metadata import ProductMetadata
from dexteritysdk.solmate.dtypes import Usize
from podite import (
    FixedLenArray,
    pod,
)

# LOCK-END


# LOCK-BEGIN[class(Combo)]: DON'T MODIFY
@pod
class Combo:
    metadata: ProductMetadata
    num_legs: Usize
    legs_array: FixedLenArray["Leg", 4]
    # LOCK-END

    @classmethod
    def to_bytes(cls, obj, **kwargs):
        return cls.pack(obj, converter="bytes", **kwargs)

    @classmethod
    def from_bytes(cls, raw, **kwargs):
        return cls.unpack(raw, converter="bytes", **kwargs)
