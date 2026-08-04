from dataclasses import dataclass, field
from typing import Optional

from models.property_building_params import BuildingInfoParams


@dataclass
class PropertyLocationParams:
    index: int = 0
    city: str = ""
    state: str = "AL"
    zip_code: str = ""
    coverage_form: str = "basic"
    theft_sublimit: str = ""
    protection_class: str = "4"
    inspection_fee: str = "yes"
    is_coastal: str = "yes"
    distance_coast: str = "within1k"
    nc_island: str = "yes"
    exc_wh_cov: str = "yes"
    has_hazard: str = "yes"
    hazard_desc: str = ""
    wh_tiv_percent: str = "2.00"
    buildings: list[BuildingInfoParams] = field(default_factory=list)