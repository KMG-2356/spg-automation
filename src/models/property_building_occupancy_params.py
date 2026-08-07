from dataclasses import dataclass

@dataclass
class BuildingOccupancyParams:

    vacant_is_building_100_percent_vacant: str = ""
    vacant_how_long_building_vacant: str = ""
    vacant_prior_occupancy: str = ""
    vacant_intended_disposition: str = ""
    vacant_building_secured: str = ""
    vacant_building_boarded_up: str = ""
    vacant_building_fenced: str = ""
    vacant_electricity_turned_off: str = ""
    vacant_gas_turned_off: str = ""
    vacant_water_turned_off: str = ""
    vacant_plumbing_drained: str = ""
    vacant_structural_issues_or_damage: str = ""
    vacant_undergoing_renovation_or_demolition: str = ""
    vacant_new_purchase: str = ""
    vacant_purchase_date: str = ""
    vacant_actively_shown_or_marketed: str = ""
    vacant_hazardous_materials_remaining: str = ""
    vacant_active_heating: str = ""
    vacant_estate_owned_or_in_probate: str = ""

    # Manufacturer

    manufacturer_desc_of_manufacturing_options: str = ""
    manufacturer_does_manufacturer_do_any_woodwork: str = ""
    manufacturer_does_manufacturer_do_any_welding: str = ""
    manufacturer_does_manufacturer_use_any_flammable_chemicals: str = ""

    # Church

    church_cooking: str = ""
    church_grills: str = ""
    church_auto_extinguish: str = ""

    # Builders Risk

    brisk_new_construction: str = ""
    brisk_floors_above: str = ""
    brisk_floors_below: str = ""
    brisk_start_date: str = ""
    brisk_end_date: str = ""
    brisk_lift_tilt_proto: str = ""
    brisk_filled_land: str = ""
    brisk_pilings: str = ""
    brisk_project_desc: str = ""
    brisk_standpipe: str = ""
    brisk_existing_structure: str = ""

    # Grocery Store

    grocery_gas_station: str = ""
    grocery_cooking: str = ""
    grocery_limited_cooking: str = ""
    grocery_grills: str = ""
    grocery_liquor_sales: str = ""
    grocery_auto_extinguish: str = ""
    grocery_operations: str = ""
    grocery_pct_occupied: str = ""
    grocery_flammable_materials: str = ""
    grocery_flammable_desc: str = ""
    grocery_denied_insurance: str = ""