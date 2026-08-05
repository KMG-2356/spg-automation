from dataclasses import dataclass, field
from typing import List

@dataclass
class GLRecord:
    square_feet_of_building: str = ""
    class_code: str = ""
    no_of_acres: str=""

@dataclass
class AdditionalInsuredRecord:
    AI_form: str = ""
    AI_name: str = ""
    Street1: str = ""
    Street2: str = ""
    City: str = ""
    State: str = ""
    ZIP: str = ""


@dataclass
class GeneralLiabilityParams:
    limit_option: str = ""
    years_in_business: str = ""
    years_of_experience: str = ""  
    no_f_acres: str = ""
    is_building_completely_vacant: str = ""
    is_building_secured_from_unauthorized_entry: str = ""
    will_building_be_scheduled_demolish_policy_term: str = ""
    building_currently_damaged: str = ""
    reno_cost: str = ""

    classification_codes: List[GLRecord] = field(default_factory=list)
    additional_insureds: List[AdditionalInsuredRecord] = field(default_factory=list)