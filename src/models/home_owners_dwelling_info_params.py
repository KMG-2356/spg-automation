from dataclasses import dataclass

@dataclass
class HomeOwnersDwellingInfoParams:
    protection_class: str = ""
    adequate_water: str = ""
    response_time: str = ""
    accessible_property: str = ""
    single_family: str = ""
    owner_occupied: str = ""
    dwelling_type: str = ""
    manufactured_home: str = ""
    
    stories: str = ""
    year_built: str = ""
    dwelling_area: str = ""
    
    good_condition: str = ""
    existing_damage: str = ""
    renovation_or_construction: str = ""
    type_of_construction: str = ""
    type_of_foundation: str = ""
    is_dwelling_single_wide_select: str = ""
    is_dwelling_lot_owned_select: str = ""
    is_dwelling_trailer_park_select: str = ""
    is_dwelling_rented: str = ""
    
    central_heating: str = ""
    wood_burning_stove: str = ""
    polybutylene_or_qwest_plumbing: str = ""
    prim_heat_source: str = ""
    water_heater: str = ""
    
    roofing_material: str = ""
    flat_roof: str = ""
    roof_year: str = ""
    siding_material: str = ""
    
    over_two_acres: str = ""
    over_ten_acres: str = ""
    unfenced_pool: str = ""
    close_to_tidal_water: str = ""
    horses: str = ""
    bite_history: str = ""
    business_pursuits: str = ""
    has_loss_payees: str = ""

    update_years_electricty_years: str = ""
    update_years_plumbing_years: str = ""
    update_years_heating_ac_years: str = ""
    update_years_updated_electrical: str = ""
    update_years_has_fuse_box: str = ""
    update_years_has_knob_tube: str = ""
    update_years_has_aluminium_wiring: str = ""
    update_years_has_lead_plumbing: str = ""

    loss_payee_full_name: str = ""
    loss_payee_street_address1: str = ""
    loss_payee_street_address2: str = ""
    loss_payee_city: str = ""
    loss_payee_state: str = ""
    loss_payee_zip: str = ""
    is_loss_payee_mortgage: str = ""
    are_mortgage_payments_current: str = ""
    loss_payee_loan_number: str = ""

    loss_payees: int = 0