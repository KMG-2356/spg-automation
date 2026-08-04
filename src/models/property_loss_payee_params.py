from dataclasses import dataclass


@dataclass
class PropertyLossPayeeParams:
    full_name: str = ""
    street1: str = ""
    street2: str = ""
    city: str = ""
    state: str = ""
    zip_code: str = ""
    mortgagee: str = ""
    loan_number: str = ""
    relationship: str = ""
    financial_interest: str = ""
    notes: str = ""
