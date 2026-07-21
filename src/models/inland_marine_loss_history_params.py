from dataclasses import dataclass
from typing import Any

@dataclass
class InlandMarineLossHistoryParams:
    has_loss_history: str = ""
    has_extra_subjectivity: str = ""
    additional_notes: str = ""
    loss: Any = None
    subjectivity: Any = None

