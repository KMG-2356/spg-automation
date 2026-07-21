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