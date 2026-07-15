from dataclasses import dataclass

@dataclass
class AgencyInfoParams:
    agency_name: str = ""
    agency_id_code: str = ""
    agent_full_name: str = ""
    agent_email: str = ""
    agent_phone: str = ""
    agent_fax: str = ""
    agent_commission: str = ""
    address_street1: str = ""
    address_street2: str = ""
    city: str = ""
    state: str = ""
    zip_code: str = ""