from dataclasses import dataclass

@dataclass
class DFinsuredInfoParams:
    insured_full_name: str = ""
    type_of_entity: str = ""
    insured_email: str = ""
    insured_phone: str = ""
    insured_occupation: str = ""
    insured_employer: str = ""
    insured_dob: str = ""
    additional_resident_or_spouse: str = ""
    additional_resident_full_name: str = ""
    additional_resident_occupation: str = ""
    additional_resident_dob: str = ""
    addition_resident_employer: str = ""
    insured_address_street1: str = ""
    insured_address_street2: str = ""
    insured_address_city: str = ""
    insured_address_state: str = ""
    insured_address_zip: str = ""

    trustee_full_name: str = "Megan Carter"
    trustee_street_address1: str = "1200 W Broad St"
    trustee_street_address2: str = "Suite 410"
    trustee_street_zip: str = "85004"
    trustee_state: str = "AZ"
    trustee_city: str = "Phoenix"

    estate_manager_name: str = "Monica Reyes"
    estate_manager_dob: str = "12/30/1985"