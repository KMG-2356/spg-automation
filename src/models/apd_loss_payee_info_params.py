from dataclasses import dataclass
from typing import Any

@dataclass
class APDLossPayeeInfoParams:
    has_loss_payee: str = ""
    loss_payees: Any = None