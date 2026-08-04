from dataclasses import dataclass

@dataclass
<<<<<<< HEAD
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

=======
class VacantBuildingParams:

    # Vacant Commercial
    vacant_commercial_is_building_100_percent_vacant: str = ""
    vacant_commercial_how_long_building_vacant: str = ""
    vacant_commercial_prior_occupancy: str = ""
    vacant_commercial_intended_disposition: str = ""
    vacant_commercial_building_secured: str = ""
    vacant_commercial_building_boarded_up: str = ""
    vacant_commercial_building_fenced: str = ""
    vacant_commercial_electricity_turned_off: str = ""
    vacant_commercial_gas_turned_off: str = ""
    vacant_commercial_water_turned_off: str = ""
    vacant_commercial_plumbing_drained: str = ""
    vacant_commercial_structural_issues_or_damage: str = ""
    vacant_commercial_undergoing_renovation_or_demolition: str = ""
    vacant_commercial_new_purchase: str = ""
    vacant_commercial_purchase_date: str = ""
    vacant_commercial_actively_shown_or_marketed: str = ""
    vacant_commercial_hazardous_materials_remaining: str = ""
    vacant_commercial_active_heating: str = ""

    # Vacant Residential
    vacant_residential_is_building_100_percent_vacant: str = ""
    vacant_residential_how_long_building_vacant: str = ""
    vacant_residential_prior_occupancy: str = ""
    vacant_residential_intended_disposition: str = ""
    vacant_residential_building_secured: str = ""
    vacant_residential_building_boarded_up: str = ""
    vacant_residential_building_fenced: str = ""
    vacant_residential_electricity_turned_off: str = ""
    vacant_residential_gas_turned_off: str = ""
    vacant_residential_water_turned_off: str = ""
    vacant_residential_plumbing_drained: str = ""
    vacant_residential_structural_issues_or_damage: str = ""
    vacant_residential_undergoing_renovation_or_demolition: str = ""
    vacant_residential_new_purchase: str = ""
    vacant_residential_purchase_date: str = ""
    vacant_residential_actively_shown_or_marketed: str = ""
    vacant_residential_estate_owned_or_in_probate: str = ""
    vacant_residential_active_heating: str = ""
>>>>>>> bb4c995 (Building scripts updated)
