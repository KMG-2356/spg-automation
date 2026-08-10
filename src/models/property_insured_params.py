from dataclasses import dataclass
from typing import Any

@dataclass
class InsuredInfoParams:
    insured_full_name: str = ""
    insured_email: str = ""
    insured_phone: str = ""
    insured_occupation: str = ""
    insured_employer: str = ""
    insured_dob: str = ""
    insured_street1: str = ""
    insured_street2: str = ""
    insured_address_zip: str = ""
    insured_city: str = ""
    insured_state: str = ""
    type_of_entity: str=""
    physical_street1: str = ""
    physical_street2: str = ""
    physical_zip: str = ""
    physical_city: str = ""
    physical_state: str = ""  
    trustee_full_name: str = ""
    trustee_street_address1: str = ""
    trustee_street_address2: str = ""
    trustee_street_zip: str = ""
    trustee_state: str = ""
    trustee_city: str = ""
    mailing_address_different:str=""
    same_as_insured:str=""
    contact_full_name:str=""
    contact_email:str=""
    contact_phone:str=""
    policy_term: str =""

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