from dataclasses import dataclass

@dataclass
class InsuredInfoParams:
    full_name: str = ""
    street1: str = ""
    street2: str = ""
    city: str = ""
    state: str = ""
    ZIP_mortgagee: str = ""
    loan_number: str = ""
    relationship: str = ""
    financial_interest: str = ""
    notes: str = ""

