from dataclasses import dataclass

@dataclass
class DFcoverageParams:
    Coverage_E_L_Limitof_Liability: str = ""
    Loss_of_Rents_CoverageD: str = ""
    Owners_Contents_CoverageC: str = ""
    Owners_Contents_Burglary_Coverage: str = ""
    Home_Systems_Protection: str = ""
    Service_Line_Coverage: str = ""
    Identity_Theft_Coverage: str = ""

    def __post_init__(self):
        for field in self.__dataclass_fields__:
            value = getattr(self, field)
            
            if isinstance(value, str) and not value.strip():
                setattr(self, field, "N/A")
            elif value is None:
                setattr(self, field, "N/A")