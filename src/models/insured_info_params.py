from dataclasses import dataclass

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
    mailing_street1: str = ""
    mailing_street2: str = ""
    mailing_zip: str = ""
    mailing_city: str = ""
    mailing_state: str = ""
    type_of_entity: str = ""
    
    additional_resident_or_spouse: str = ""
    additional_resident_full_name: str = ""
    additional_resident_occupation: str = ""
    additional_resident_dob: str = ""
    additional_resident_employer: str = ""
    
    mailing_address_different: str = ""
    diff_mailing_zip: str = ""
    diff_mailing_street1: str = ""
    diff_mailing_street2: str = ""
    diff_mailing_city: str = ""
    diff_mailing_state: str = ""
    
    trustee_full_name: str = "Megan Carter"
    trustee_street_address1: str = "1200 W Broad St"
    trustee_street_address2: str = "Suite 410"
    trustee_street_zip: str = "85004"
    trustee_state: str = "AZ"
    trustee_city: str = "Phoenix"