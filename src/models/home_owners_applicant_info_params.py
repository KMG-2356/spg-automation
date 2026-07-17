from dataclasses import dataclass

@dataclass
class HomeOwnersApplicantInfoParams:
    # --- Dwelling Info ---
    protection_class: str = ""
    adequate_water: str = ""
    response_time: str = ""
    accessible_property: str = ""
    single_family: str = ""
    owner_occupied: str = ""
    dwelling_type: str = ""
    manufactured_home: str = ""

    # --- Applicant Info ---
    credit_history: str = ""
    arson_and_fraud: str = ""
    bankruptcy: str = ""
    foreclosure: str = ""
    child_support: str = ""
    repossessions: str = ""
    
    # --- Purchase Details ---
    new_purchase: str = ""
    year_purchased: str = ""
    prior_foreclosure: str = ""
    purchase_price: str = ""
    
    # --- Insurance History ---
    prior_insurance: str = ""
    prior_commonwealth: str = ""
    prior_carrier: str = ""
    previous_expiration: str = ""
    prior_premium: str = ""
    
    # --- Agency & Coverage Details ---
    new_agency: str = ""
    lapse_of_coverage: str = ""
    termination_at_companies_request: str = ""
    reason_for_termination: str = ""
    previous_wind_hail: str = ""