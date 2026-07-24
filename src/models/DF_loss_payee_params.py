from dataclasses import dataclass
from typing import Any

@dataclass
class DFlossPayeeParams:
    loss_payeefull_name: str = ""
    loss_payee_street1: str = ""
    loss_payee_street2: str = ""
    loss_payee_city: str = ""
    loss_payee_state: str = ""
    loss_payee_zip: str = ""
    is_mortgage: str = ""
    loan_number: str = ""
    is_mortgage_current: str = ""
   
    loss_payee: Any = None
