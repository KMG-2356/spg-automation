from dataclasses import dataclass
from typing import Any

@dataclass
class InlandMarineParams:
    scheduled_equipment_coverage: str = ""
    miscellaneous_article_coverage: str = ""
    used_for_logging: str = ""
    has_loss_payees: str = ""
    equipments: Any = None
    loss_payees: Any = None
    total_value_of_misc_items: str = ""