from dataclasses import dataclass, field
from typing import List

@dataclass
class DriverRecord:
    vehicle_year: str= ""
    Driver_name: str= ""
    Date_of_birth: str= ""
    License_number: str= ""
    License_state: str= ""
    Years_of_experience: str= ""
    Date_of_hire: str= ""
    Relationship: str= ""
    violation_history_known: str= ""
    major_violations_count: str= ""
    minor_violations_count: str= ""
    At_Fault_accidents_count: str= ""


@dataclass
class DriverInfoParams:
    drivers: List[DriverRecord] = field(default_factory=list)