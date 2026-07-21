from dataclasses import dataclass, field
from typing import List, Any

@dataclass
class LossRecord:
    LossDate: str = ""
    TypeOfLoss: str = ""
    Details: str = ""
    Amount: str = ""

@dataclass
class DFLossHistoryParams:
    any_open_claims: str = ""
    has_loss: str = ""
    unrepairedDamage: str = ""
    losses: Any = field(default_factory=list)    
