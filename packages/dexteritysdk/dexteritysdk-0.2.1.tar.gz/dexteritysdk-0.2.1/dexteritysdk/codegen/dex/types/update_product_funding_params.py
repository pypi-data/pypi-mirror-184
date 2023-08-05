# LOCK-BEGIN[imports]: DON'T MODIFY
from dexteritysdk.codegen.dex.types.fractional import Fractional
from dexteritysdk.codegen.dex.types.product_status import ProductStatus
from podite import pod

# LOCK-END


# LOCK-BEGIN[class(UpdateProductFundingParams)]: DON'T MODIFY
@pod
class UpdateProductFundingParams:
    amount: Fractional
    new_product_status: "ProductStatus"
    # LOCK-END

    @classmethod
    def to_bytes(cls, obj, **kwargs):
        return cls.pack(obj, converter="bytes", **kwargs)

    @classmethod
    def from_bytes(cls, raw, **kwargs):
        return cls.unpack(raw, converter="bytes", **kwargs)
