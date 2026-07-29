from dataclasses import dataclass, field
from typing import List

@dataclass
class CommodityRecord:
    commodity: str = ""
    percent_of_cargo: str = ""
    average_value_per_load: str = ""
    maximum_value_per_load: str = ""

@dataclass
class CargoCommoditiesParams:
    cargo_includes_liquor_manufactured_tobacco: str = ""
    cargo_includes_oversized_overweight_commodities: str = ""
    cargo_includes_excluded_commodities: str = ""

    commodities: List[CommodityRecord] = field(default_factory=list)
