from dataclasses import dataclass, field
from typing import List

@dataclass
class LossHistoryRecord:
    loss_year: str = ""
    premium_at_time_of_loss: str = ""
    type_of_loss: str = ""
    amount_paid: str = ""
    amount_outstanding: str = ""
    other_describe: str = ""


@dataclass
class LossHistoryInfoParams:
      any_losses_in_the_past_3Years: str=""

      losses: List[LossHistoryRecord] = field(default_factory=list)