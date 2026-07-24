from dataclasses import dataclass

@dataclass
class CargoCoverageParams:
    terminal_coverage_required: str =""
    trailer_interchange_coverage_required: str =""	
    TI_limit: str =""	
    written_TI_agreement_in_place: str =""
    refrigeration_breakdown_coverage_required: str =""
    any_refer_trailers_older_than_10years: str =""
    refer_trailer_serviced_at_least_every_30days: str =""
    hauls_seafood_or_shellfish: str =""
    cargo_limit_per_unit: str =""	
    average_exposure_per_unit: str =""
    maximum_exposure_per_unit: str =""
    loads_ever_exceed_cargo_insurance_limit: str =""
    cargo_deductible: str =""
    radius_of_operations: str =""
