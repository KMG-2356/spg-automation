from dataclasses import dataclass, field
from typing import List, Any

@dataclass
class LossRecord:
    loss_date: str = ""
    loss_type: str = ""
    loss_details: str = ""
    loss_amount: str = ""

@dataclass
class HomeOwnersLossHistoryParams:
    open_claims: str = ""
    has_loss: str = ""
    unrepaired: str = ""
    losses: Any = field(default_factory=list)