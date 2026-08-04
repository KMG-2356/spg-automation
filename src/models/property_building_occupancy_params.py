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

