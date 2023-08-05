# LOCK-BEGIN[imports]: DON'T MODIFY
from dexteritysdk.solmate.anchor import InstructionDiscriminant
from podite import (
    Enum,
    U64,
    pod,
)

# LOCK-END


# LOCK-BEGIN[instruction_tag]: DON'T MODIFY
@pod
class InstructionTag(Enum[U64]):
    INITIALIZE_MARKET_PRODUCT_GROUP = InstructionDiscriminant()
    UPDATE_MARKET_PRODUCT_GROUP = InstructionDiscriminant()
    INITIALIZE_MARKET_PRODUCT = InstructionDiscriminant()
    DEACTIVATE_MARKET_PRODUCT = InstructionDiscriminant()
    REMOVE_MARKET_PRODUCT = InstructionDiscriminant()
    REMOVE_MARKET_PRODUCT_GROUP = InstructionDiscriminant()
    INITIALIZE_PRINT_TRADE = InstructionDiscriminant()
    SIGN_PRINT_TRADE = InstructionDiscriminant()
    INITIALIZE_TRADER_RISK_GROUP = InstructionDiscriminant()
    NEW_ORDER = InstructionDiscriminant()
    UPDATE_VARIANCE_CACHE = InstructionDiscriminant()
    CONSUME_ORDERBOOK_EVENTS = InstructionDiscriminant()
    CANCEL_ORDER = InstructionDiscriminant()
    DEPOSIT_FUNDS = InstructionDiscriminant()
    WITHDRAW_FUNDS = InstructionDiscriminant()
    UPDATE_PRODUCT_FUNDING = InstructionDiscriminant()
    TRANSFER_FULL_POSITION = InstructionDiscriminant()
    INITIALIZE_COMBO = InstructionDiscriminant()
    UPDATE_TRADER_FUNDING = InstructionDiscriminant()
    CLEAR_EXPIRED_ORDERBOOK = InstructionDiscriminant()
    POP_EVENTS = InstructionDiscriminant()
    SWEEP_FEES = InstructionDiscriminant()
    CHOOSE_SUCCESSOR = InstructionDiscriminant()
    CLAIM_AUTHORITY = InstructionDiscriminant()
    SETUP_CAPITAL_LIMITS = InstructionDiscriminant()
    UPDATE_CAPITAL_LIMITS = InstructionDiscriminant()
    # LOCK-END


