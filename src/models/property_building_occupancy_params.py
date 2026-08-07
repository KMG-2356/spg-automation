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

    #Apartment
    apartment_how_many_units_in_building: str = ""

    #Warehouse
    warehouse_are_any_flammable_or_hazardous_materials_stored: str = ""
    does_this_warehouse_has_refrigerating_units: str = ""

    #Office
    office_describe_the_type_of_office_use: str = ""

    #Hotels
    hotels_are_rooms_rented_on_a_longterm_basis: str = ""

    #Dwelling    
    dwelling_number_of_families: str = ""

    #Condo
    Condominium_How_many_units_in_the_building: str = ""

