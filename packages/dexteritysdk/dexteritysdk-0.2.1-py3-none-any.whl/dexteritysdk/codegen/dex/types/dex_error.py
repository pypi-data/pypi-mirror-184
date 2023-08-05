# LOCK-BEGIN[imports]: DON'T MODIFY
from podite import (
    AutoTagType,
    Enum,
    pod,
)

# LOCK-END


# LOCK-BEGIN[class(DexError)]: DON'T MODIFY
@pod
class DexError(Enum[AutoTagType]):
    CONTRACT_IS_EXPIRED = None
    CONTRACT_IS_NOT_EXPIRED = None
    INVALID_SYSTEM_PROGRAM_ACCOUNT = None
    INVALID_AOB_PROGRAM_ACCOUNT = None
    INVALID_STATE_ACCOUNT_OWNER = None
    INVALID_ORDER_INDEX = None
    USER_ACCOUNT_FULL = None
    TRANSACTION_ABORTED = None
    MISSING_USER_ACCOUNT = None
    ORDER_NOT_FOUND = None
    NO_OP = None
    OUTOF_FUNDS = None
    USER_ACCOUNT_STILL_ACTIVE = None
    MARKET_STILL_ACTIVE = None
    INVALID_MARKET_SIGNER_ACCOUNT = None
    INVALID_ORDERBOOK_ACCOUNT = None
    INVALID_MARKET_ADMIN_ACCOUNT = None
    INVALID_BASE_VAULT_ACCOUNT = None
    INVALID_QUOTE_VAULT_ACCOUNT = None
    FULL_MARKET_PRODUCT_GROUP = None
    MISSING_MARKET_PRODUCT = None
    INVALID_WITHDRAWAL_AMOUNT = None
    INVALID_TAKER_TRADER = None
    FUNDS_ERROR = None
    INACTIVE_PRODUCT_ERROR = None
    TOO_MANY_OPEN_ORDERS_ERROR = None
    NO_MORE_OPEN_ORDERS_ERROR = None
    NON_ZERO_PRICE_TICK_EXPONENT_ERROR = None
    DUPLICATE_PRODUCT_NAME_ERROR = None
    INVALID_RISK_RESPONSE_ERROR = None
    INVALID_ACCOUNT_HEALTH_ERROR = None
    ORDERBOOK_IS_EMPTY_ERROR = None
    COMBOS_NOT_REMOVED = None
    ACCOUNT_NOT_LIQUIDABLE = None
    FUNDING_PRECISION_ERROR = None
    PRODUCT_DECIMAL_PRECISION_ERROR = None
    PRODUCT_NOT_OUTRIGHT = None
    PRODUCT_NOT_COMBO = None
    INVALID_SOCIAL_LOSS_CALCULATION = None
    PRODUCT_INDEX_MISMATCH = None
    INVALID_ORDER_I_D = None
    INVALID_BYTES_FOR_ZERO_COPY_DESERIALIZATION = None
    INCORRECT_PRINT_TRADE_SIZE = None
    INCORRECT_PRINT_TRADE_PRICE = None
    INCORRECT_PRINT_TRADE_SIDE = None
    INCORRECT_PRINT_TRADE_OPERATOR_CREATOR_FEES = None
    INCORRECT_PRINT_TRADE_OPERATOR_COUNTERPARTY_FEES = None
    INVALID_PRINT_TRADE_OPERATOR_FEES = None
    DEPOSIT_LIMIT_EXCEEDED = None
    WITHDRAW_LIMIT_EXCEEDED = None
    NEGATIVE_DEPOSIT_LIMIT = None
    NEGATIVE_WITHDRAW_LIMIT = None
    DEPOSIT_DENIED_INSUFFICIENT_BALANCE_ON_WHITELIST_ATA_TOKEN = None
    DEPOSIT_DECLINED_UNFROZEN_WHITELIST_ATA_TOKEN = None
    DEPOSIT_DECLINED_NON_EXISTENT_WHITELIST_ATA_TOKEN_ON_TRADER_RISK_GROUP = None
    INVALID_PRODUCT_STATUS_IN_UPDATE_FUNDING = None
    CONTRACT_IS_NOT_EXPIRING = None
    CONTRACT_HAS_NON_ZERO_OPEN_INTEREST = None
    CONTRACT_IS_ACTIVE = None
    # LOCK-END

    @classmethod
    def _to_bytes_partial(cls, buffer, obj, **kwargs):
        # to modify packing, change this method
        return super()._to_bytes_partial(buffer, obj, **kwargs)

    @classmethod
    def _from_bytes_partial(cls, buffer, **kwargs):
        # to modify unpacking, change this method
        return super()._from_bytes_partial(buffer, **kwargs)

    @classmethod
    def to_bytes(cls, obj, **kwargs):
        return cls.pack(obj, converter="bytes", **kwargs)

    @classmethod
    def from_bytes(cls, raw, **kwargs):
        return cls.unpack(raw, converter="bytes", **kwargs)
