from dataclasses import dataclass
from typing import Any


@dataclass
class APDInsuredInfoParams:
    insured_name: str = ""
    entity_type: str = ""
    insured_email: str = ""
    insured_phone: str = ""

    # Mailing Address
    mailing_street1: str = ""
    mailing_street2: str = ""
    mailing_city: str = ""
    mailing_state: str = ""
    mailing_zip: str = ""

    # Carrier & Operations Info
    new_venture: str = ""
    insured_icc: str = ""
    filings: str = ""
    all_owned_units: str = ""
    carrier_type: str = ""
    own_goods: str = ""
    garage_same: str = ""
    carrier_details: str = ""

    # Primary Garaging Address
    primary_garaging_street1: str = ""
    primary_garaging_street2: str = ""
    primary_garaging_city: str = ""
    primary_garaging_state: str = ""
    primary_garaging_zip: str = ""

    has_secondary_garage: str = ""
    secondary_garages: Any = None

    # Trustee Information
    trustee_name: str = ""
    trustee_street1: str = ""
    trustee_street2: str = ""
    trustee_city: str = ""
    trustee_state: str = ""
    trustee_zip: str = ""