from dataclasses import dataclass


@dataclass
class APDCoveragesParams:
    refrigeration_breakdown: str = ""
    trailer_age: str = ""
    reefer_trailer_serviced: str = ""
    seafood: str = ""
    radius: str = ""
    phys_dam_deductible: str = ""
    ts_limit: str = ""