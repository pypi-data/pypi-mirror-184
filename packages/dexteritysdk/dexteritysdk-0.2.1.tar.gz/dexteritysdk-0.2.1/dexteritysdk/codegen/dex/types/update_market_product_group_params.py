# LOCK-BEGIN[imports]: DON'T MODIFY
from podite import pod

# LOCK-END


# LOCK-BEGIN[class(UpdateMarketProductGroupParams)]: DON'T MODIFY
@pod
class UpdateMarketProductGroupParams:
    pass
    # LOCK-END

    @classmethod
    def to_bytes(cls, obj, **kwargs):
        return cls.pack(obj, converter="bytes", **kwargs)

    @classmethod
    def from_bytes(cls, raw, **kwargs):
        return cls.unpack(raw, converter="bytes", **kwargs)
