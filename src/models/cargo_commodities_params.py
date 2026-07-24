from dataclasses import dataclass
from typing import Any

@dataclass
class CargoCommoditiesParams:
    cargo_includes_liquor_manufactured_tobacco: str = ""
    cargo_includes_oversized_overweight_commodities: str = ""
    cargo_includes_excluded_commodities: str = ""
    commodity: str = ""
    percent_of_cargo: str = ""
    average_value_per_load: str = ""
    maximum_value_per_load: str = ""

    commodities: Any = None
