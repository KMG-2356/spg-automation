from dataclasses import dataclass

@dataclass
class CargoAdditionalInformationParams:
   estimated_gross_revenue_for_coming_year: str = ""
   own_haul_total: str = ""
   subcontracted_total: str = ""
