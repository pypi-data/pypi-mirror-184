# LOCK-BEGIN[imports]: DON'T MODIFY
from dexteritysdk.codegen.dex.types.fractional import Fractional
from podite import pod

# LOCK-END


# LOCK-BEGIN[class(Params)]: DON'T MODIFY
@pod
class Params:
    quantity: "Fractional"
    # LOCK-END

    @classmethod
    def to_bytes(cls, obj, **kwargs):
        return cls.pack(obj, converter="bytes", **kwargs)

    @classmethod
    def from_bytes(cls, raw, **kwargs):
        return cls.unpack(raw, converter="bytes", **kwargs)
