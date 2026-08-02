from dataclasses import dataclass, field
from typing import List

@dataclass
class CargoAdditionalInsuredInformationParams:
    has_applicant_ever_operated_under_different_name: str = ""
    descirbe_other_subcontrating_lease_basis: str = ""
    does_applicant_have_other_carrier_operations: str = ""
    describe_other_operations: str = ""
    does_insured_subcontract_to_other_parties: str =""
    Subcontracting_basis: str =""
    describe_subcontracting_lease_basis: str =""
    subcontractors_responsible_for_cargo_loss: str =""
    maintains_copies_of_subcontractor_insurance: str =""
    is_the_owner_also_listed_as_driver: str =""
    has_insured_had_coverage_in_the_last_3years: str =""
    insurance_placed_through_commonwealth_underwriters: str =""
    any_insurer_canceled_non_renewed_in_last_3years: str =""
    prior_carrier_information_known: str =""
    prior_carrier_name: str =""
    prior_perils_form: str =""
    prior_policy_premium: str =""
    prior_policy_deductible: str =""
    prior_policy_limit: str =""
    prior_policy_expiration_date: str =""
    was_a_renewal_offer_made: str =""
    consecutive_coverage_greater_than_ot_equal_to_12months: str =""
    years_of_experience_same_type_of_work: str =""
    prior_employment_information_known: str =""
    details_for_reasons_of_non_renewal: str =""

    employers: List[EmployerRecord] = field(default_factory=list)
@dataclass
class EmployerRecord:
    employer_name: str =""
    phone: str =""
    street1: str =""
    city: str =""
    state: str =""
    zip_code: str =""
    start_date: str =""
    end_date: str =""
    unit_type_operated: str =""
    commodities_hauled: str =""
    radius: str =""
    object_to_verification: str =""

    

