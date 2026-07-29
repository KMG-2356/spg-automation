from dataclasses import dataclass, field
from typing import List

@dataclass
class VehicleRecord:
    vehicle_year: str= ""
    vehicle_make: str= ""
    vehicle_type: str= ""
    VIN_known: str= ""
    VIN_number: str= ""

@dataclass
class VehicleInfoParams:
    vehicles: List[VehicleRecord] = field(default_factory=list)
