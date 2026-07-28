from dataclasses import dataclass
from typing import Any

@dataclass
class RiskInfoParams:
    hiring_process: str = ""
    firing_process: str = ""
    has_trailers: str = ""
    has_extra_equipment: str = ""
    extra_equipment: str = ""
    exemption_reason: str = ""
    secure_vehicle: str = ""
    rented_each_job: str = ""
    rented_equipment: str = ""
    titled_vehicles: str = ""
    owner_driven: str = ""
    inspected_vehicles: str = ""
    inspection_interval: str = ""
    gvw: str = ""
    driver_experience: str = ""
    drivers: Any = None
    vehicles: Any = None
    trailers: Any = None