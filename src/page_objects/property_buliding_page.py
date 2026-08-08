import re
from playwright.sync_api import Page, expect, TimeoutError
from models.property_building_occupancy_params import BuildingOccupancyParams
from models.property_building_params import BuildingInfoParams

class BuildingInformationPage:
    def __init__(self, page: Page):
        self.page = page
        self.loss_history_btn = self.page.get_by_role("button", name="Location Management")
        self.add_another_loss_payee_btn = self.page.get_by_role("button", name="Add Another Loss Payee")
        self.loading_screen = self.page.locator(".jss53")
    def street_address_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.address\"]")
    def suit_unit_floor_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.address2\"]")
    def no_of_stories_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.stories\"]")
    def area_of_property_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.sqfeet\"]")
    def year_built_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.year_built\"]")
    def type_of_construction_select(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.construction\"]")
    def occupancy_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.occupancy\"]")
    def building_value_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.value\"]")
    def is_building_in_good_condition_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.good_condition\"]")
    def valuation_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.valuation\"]")
    def does_buildong_have_slate_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.roof_type\"]")
    def coinsurance_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.coinsurance\"]")
    def deductible_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.deductible\"]")
    def distance_to_hydrant_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.distance_to_hydrant\"]")
    def distance_unit_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.distance_unit\"]")
    def is_the_fire_department_paid_or_volunteer_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.fire_department\"]")
    def is_the_building_equipped_with_sprinkler_system_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.safeguards.sprinkler_system\"]")
    def does_building_contains_central_alarms_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.safeguards.central_alarms\"]")
    def roof_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.updates.roof\"]")
    def electrical_warning_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.updates.electricity\"]")
    def plumbing_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.updates.plumbing\"]")
    def HVAC_updated_year_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.updates.heating_ac\"]")
    def risk_uninsured_select(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.uninsured\"]")
    def risk_new_building(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.new_building\"]")
    def risk_prior_carrier_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.prior_carrier\"]")
    def risk_prior_expiration_date_input(self,i,j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.prior_expiration\"]")
    def risk_days_wo_insurance_input(self,i,j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.days_wo_insurance\"]")

    #AWNING COVERAGE

    def awning_coverage_checkbox(self):
        return self.page.get_by_text("Add Awning coverage?")
    def awning_limit_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.awning.limit\"]")
    def awning_valuation_iselection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.awning.valuation\"]")
    def awning_coinsurance_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.awning.coinsurance\"]")
    
    #ADD BUSINESS INTERRUPTION

    def add_business_interruption_coverage_checkbox(self):
        return self.page.get_by_text("Add Business Interruption coverage?")
    def business_limit_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.bintr.limit\"]")
    def business_valuation_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.bintr.valuation\"]")
    #ADD LOSS OF RENTS

    def add_loss_of_rents_coverage_checkbox(self):
        return self.page.get_by_text("Add Loss of Rents coverage?")
    def loss_of_rents_limit_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.lor.limit\"]")
    def loss_of_rents_valuation_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.lor.valuation\"]")
    #ADD BUSINESS PERSONAL PROPERTY COVERAGE

    def BPP_coverage_checkbox(self):
        return self.page.get_by_text("Add Business Personal Property coverage?")
    def BPP_limit_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.bpp.limit\"]")
    def BPP_valuation_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.bpp.valuation\"]")
    def BPP_coinsurance_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.bpp.coinsurance\"]")
    #ADD PUMPS AND CANOPY COVERAGE

    def canopy_coverage_checkbox(self):
        return self.page.get_by_text("Add Pumps and Canopy coverage?")
    def canopy_limit_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.canopy.limit\"]")
    def canopy_valuation_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.canopy.valuation\"]")
    def canopy_coinsurance_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.canopy.coinsurance\"]")
    
    #ADD RENOVATION COVERAGE

    # def rennovation_coverage_checkbox(self):
    #     return self.page.get_by_text("Add Renovation coverage?")
    # def rennovation_limit_input(self, i, j):
    #     return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.reno.limit\"]")
    # def rennovation_valuation_selection(self, i, j):
    #     return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.reno.valuation\"]")
    # def rennovation_coinsurance_selection(self, i, j):
    #     return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.reno.coinsurance\"]")
    # def rennovation_will_building_be_demolished_selection(self, i, j):
    #     return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.reno.demolished\"]")
    # def rennovation_plan_of_building_input(self, i, j):
    #     return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.reno.plans\"]")
    # def rennovation_expect_start_date_input(self, i, j):
    #     return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.reno.start_date\"]")
    # def rennovation_expect_end_date_input(self, i, j):
    #         return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.reno.end_date\"]")
    
    #ADD SIGN COVERAGE

    def sign_coverage_checkbox(self, i, j):
        return self.page.get_by_text("Add Sign coverage?")
    def sign_limit_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.sign.limit\"]")
    def sign_valuation_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.sign.valuation\"]")
    def sign_coinsurance_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.sign.coinsurance\"]")
    
   #ADD SPOILAGE COVERAGE

    def spoilage_coverage_checkbox(self):
        return self.page.get_by_text("Add Spoilage coverage?")
    def spoilage_limit_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.spoilage.limit\"]")
    def spoilage_deductible_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.spoilage.deductible\"]")
    def spoilage_add_coverage_for_breakdown_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.spoilage.contamination\"]")
    def spoilage_add_coverages_for_outages_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.spoilage.power_outage\"]")
    def spoilage_is_there_refrigeration_maintainence_agreement_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.spoilage.refrig_maint_agreement\"]")

    #CONTRCTOR INFO

    def who_is_doing_work_checkbox(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.contractor.contractor_type\"]")
    def certificates_of_insurance_to_be_obtained_from_the_subcontractors_selection(self,i,j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.contractor.ai_cert\"]")
    def is_contractor_info_known_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.contractor.info_known\"]")
    def license_no_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.contractor.license_no\"]")
    def no_of_years_in_business_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.contractor.years_operating\"]")
    
    #LOSS PAYEE

    def does_building_have_loss_payee_selection(self,i,j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.has_loss_payees\"]")     
    def loss_payee_full_name_input(self,i,j,k):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.loss_payees.{k}.name\"]")
    def loss_payee_street_address1_input(self):
        return self.page.locator(".MuiGrid-container").filter(has=self.page.locator("div").filter(has_text="Loss Payee")).nth(-2).locator(".MuiGrid-item").filter(has_text="Mailing Address").locator("input").nth(0)
    def loss_payee_street_address2_input(self):
        return self.page.locator(".MuiGrid-container").filter(has=self.page.locator("div").filter(has_text="Loss Payee")).nth(-2).locator(".MuiGrid-item").filter(has_text="Mailing Address").locator("input").nth(1)
    def loss_payee_city_input(self):
        return self.page.locator(".MuiGrid-container").filter(has=self.page.locator("div").filter(has_text="Loss Payee")).nth(-2).locator(".MuiGrid-item").filter(has_text="Mailing Address").locator("input").nth(2)
    def loss_payee_state_selection(self):
        return self.page.locator(".MuiGrid-container").filter(has=self.page.locator("div").filter(has_text="Loss Payee")).nth(-2).locator(".MuiGrid-item").filter(has_text="Mailing Address").locator("select").nth(0)
    def loss_payee_zip_input(self):
        return self.page.locator(".MuiGrid-container").filter(has=self.page.locator("div").filter(has_text="Loss Payee")).nth(-2).locator(".MuiGrid-item").filter(has_text="Mailing Address").locator("input").nth(3)
    def is_loss_payee_mortgagee_slection(self,i,j,k):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.loss_payees.{k}.mortgagee\"]")
    def loan_number_input(self,i,j,k):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.loss_payees.{k}.loan_number\"]")
    def loss_payee_relationship_input(self, i,j,k):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.loss_payees.{k}.relationship\"]")
    def loss_payee_financial_interest_select(self,i,j,k):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.loss_payees.{k}.interest\"]")
    
   #VACANT ADDITIONAL QUESTIONS

    def is_new_purchase_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.vacant_quals.new_purchase\"]")
    def prior_occupancy_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.vacant_quals.prior_occupancy\"]")
    def vacant_since_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.vacant_quals.vacant_since\"]")
    def is_building_100_percent_vacant_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.vacant_quals.fully_vacant\"]")     
    def any_structural_work_being_done_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.vacant_quals.structural_work\"]")
    def boarded_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.vacant_quals.boarded\"]")
    def locked_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.vacant_quals.locked\"]")
    def fenced_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.vacant_quals.fenced\"]")
    def is_electricity_still_active_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.vacant_quals.electricity\"]")
    def is_gas_still_active_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.vacant_quals.gas\"]")
    def is_water_still_active_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.vacant_quals.water\"]")
    def intended_disposition_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.vacant_quals.intended_disposition\"]")
    def will_heat_be_maintained_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.vacant_quals.heat\"]")
    def is_plumbing_system_drained_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.vacant_quals.plumbing\"]")
    def any_unfenced_pool_or_body_of_water_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.vacant_quals.unfenced_pool\"]")
    def is_located_on_more_than_2acres_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.vacant_quals.over_two_acres\"]")
       
  #APPARTMENT ADDITIONAL QUESTIONS

    def are_70_or_more_of_apartment_units_ocupied_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.apartment_quals.min_occupancy_rate\"]")
    def no_of_apartment_units_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.apartment_quals.num_apt_units\"]")
    def average_monthly_rent_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.apartment_quals.avg_rent\"]")
    def is_heating_maintained_in_all_units_during_winter_months_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.apartment_quals.winter_heating\"]")
    def are_all_units_equipped_with_working_smoke_detectors_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.apartment_quals.smoke_detectors\"]")
    def is_outdoor_property_scheduled_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.apartment_quals.sched_outdoor_prop\"]")
    def is_the_apartment_used_for_student_housing_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.apartment_quals.student_housing\"]")
    def is_housing_subsidized_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.apartment_quals.subsidized_housing\"]")
    def insured_been_in_business_minimum_of_2years_OR_has_5years_of_management_experience_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.apartment_quals.insured_experience\"]")
    def is_renters_insurance_required_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.apartment_quals.renters_insurance\"]")
    def is_there_a_resident_manager_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.apartment_quals.resident_manager\"]")

#GARAGE ADDITIONAL QUESTIONS

    def does_garage_only_engage_in_auto_glass_replacement_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.garage_quals.minor_repair\"]")
    def does_garage_do_welding_torching_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.garage_quals.welding\"]")
    def is_garage_an_auto_body_shop_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.garage_quals.body_shop\"]")
    def is_garage_used_primarily_for_storage_of_tires_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.garage_quals.tire_storage\"]")
#MANUFACTURER ADDITIONAL QUESTIONS

    def type_of_manufacturing_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.occupancy_mfg\"]")
    def desc_of_manufacturing_options_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.manufacturer_quals.description\"]")
    def does_manufacturer_do_any_woodwork_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.manufacturer_quals.woodwork\"]")
    def does_manufacturer_do_any_welding_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.manufacturer_quals.welding\"]")
    def does_manufacturer_use_any_flammable_chemicals_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.manufacturer_quals.flammable_materials\"]")

#RETAIL ADDITIONAL QUESTIONS

    def type_of_retail_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.retail_quals.retail_select\"]")
    def describe_type_of_retail_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.retail_quals.description\"]")
    def does_this_retail_establishment_sell_antiques_selections(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.antique_store\"]")
    def does_this_retail_establishment_have_refrigeration_units_selections(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.retail_refrigeration\"]")

#WAREHOUSE ADDITIONAL QUESTIONS
    
    def does_this_warehouse_has_refrigerating_units_selection(self, i, j): 
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.warehouse_refrigeration\"]")
    def any_hazardous_material_storage_selection(self, i, j): 
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.warehouse_quals.hazardous_mats\"]")
    def describe_hazardous_material_input(self, i, j): 
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.warehouse_quals.hazardous_mats_desc\"]")
    def any_chemical_substance_storage_selection(self, i, j): 
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.warehouse_quals.chemical_storage\"]")
    def any_explosive_storage_selection(self, i, j): 
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.warehouse_quals.explosive_storage\"]")
    def any_firework_storage_selection(self, i, j): 
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.warehouse_quals.fireworks_storage\"]")

#SOCIAL CLUB ADDITIONAL QUESTIONS

    def social_do_employees_cook_food_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.club_quals.cooking\"]")

#OFFICE ADDITIONAL QUESTIONS

    def describe_type_of_office_work_done_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.office_quals.description\"]")
    #CHURCH ADDITIONAL QUESTIONS

    def church_cooking_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.church_quals.cooking\"]")

    def church_grills_selection(self, i, j):
        '''Optional'''
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.church_quals.grills\"]")

    def church_auto_extinguish_selection(self, i, j):
        '''Optional'''
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.church_quals.auto_extinguish\"]")
    

#CONDOMINIUM ADDITIONAL QUESTIONS

    def condo_are_70_or_more_of_apartment_units_ocupied_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.condo_quals.min_occupancy_rate\"]")
    def condo_are_units_rented_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.condo_quals.rented\"]")
    def condo_no_of_units_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.condo_quals.num_units\"]")
    def condo_is_heating_maintained_in_all_units_during_winter_months_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.condo_quals.winter_heating\"]")
    def condo_are_all_units_equipped_with_working_smoke_detectors_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.condo_quals.smoke_detectors\"]")
    def condo_is_outdoor_property_scheduled_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.condo_quals.sched_outdoor_prop\"]")
    def condo_is_the_apartment_used_for_student_housing_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.condo_quals.student_housing\"]")
    def condo_is_housing_subsidized_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.condo_quals.subsidized_housing\"]")
    def condo_insured_been_in_business_minimum_of_2years_OR_has_5years_of_management_experience_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.condo_quals.insured_experience\"]")

#HEALTH CARE FACILITY ADDITIONAL QUESTIONS
    def health_no_of_beds_in_facility_input(self, i, j): 
            return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.healthcare_quals.num_beds\"]")
    def healthare_all_beds_equipped_with_smoke_detector_selection(self, i, j): 
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.healthcare_quals.smoke_co_detectors\"]")
    def healthis_owner_or_employees_on_site_24_hours(self, i, j): 
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.healthcare_quals.on_site_24hr\"]")
    def healthis_premises_smoke_free_selection(self, i, j): 
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.healthcare_quals.smoke_free\"]")
    def healthis_cooking_allowed_in_rooms_selection(self, i, j): 
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.healthcare_quals.cooking_in_rooms\"]")
    def healthdo_employees_cook_food_selection(self, i, j): 
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.healthcare_quals.cooking\"]")

#WOODWORKING ADDITIONAL QUESTIONS

    def are_all_wiping_cloths_selection(self, i, j): 
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.woodworking_quals.proper_disposal\"]")
    def does_risk_have_dust_removal_system_selection(self, i, j): 
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.woodworking_quals.dust_removal\"]")
    def are_premises_well_kept_selection(self, i, j): 
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.woodworking_quals.good_housekeeping\"]")
 
#RESTAURANT ADDITIONAL QUESTIONS

    def does_owner_have_at_least_2years_of_prior_restaurant_ownership_selection(self, i, j): 
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.restaurant_quals.prior_experience\"]")
    def does_restaurant_have_approved_ANSUL_selection(self, i, j): 
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.restaurant_quals.auto_extinguish\"]")
    def are_foods_prepared_cold_selection(self, i, j): 
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.restaurant_quals.limited_cooking\"]")
    def percentage_of_sales_that_are_liquor_input(self, i, j): 
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.restaurant_quals.liquor_sales\"]")



    #BUILDERS RISK ADDITIONAL QUESTIONS
    def new_construction_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.brisk_quals.new_construction\"]")

    def floors_above_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.brisk_quals.floors_above\"]")

    def floors_below_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.brisk_quals.floors_below\"]")

    def start_date_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.brisk_quals.start_date\"]")

    def end_date_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.brisk_quals.end_date\"]")

    def lift_tilt_proto_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.brisk_quals.lift_tilt_proto\"]")

    def filled_land_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.brisk_quals.filled_land\"]")

    def pilings_selection(self, i, j):
        '''Optional'''
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.brisk_quals.pilings\"]")

    def project_desc_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.brisk_quals.project_desc\"]")

    def standpipe_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.brisk_quals.standpipe\"]")

    def existing_structure_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.brisk_quals.existing_structure\"]")

    # Builder's Risks Safeguards

    # SAFEGUARDS / PROTECTIONS

    def sprinkler_system_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.safeguards.sprinkler_system\"]")

    def central_alarms_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.safeguards.central_alarms\"]")

    def safeguard_fenced_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.safeguards.fenced\"]")

    def lighting_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.safeguards.lighting\"]")

    def detection_systems_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.safeguards.detection_systems\"]")

    def video_surveillance_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.safeguards.video_surveillance\"]")

    def safeguards_storage_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.safeguards.storage\"]")

    def other_protections_input(self):
        '''Optional'''
        return self.page.get_by_role("textbox", name="If other protections are present, please specify them", exact=True)
    
    #GROCERY STORE ADDITIONAL QUESTIONS

    def gas_station_selection(self, i, j):
            return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.grocery_quals.gas_station\"]")

    def cooking_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.grocery_quals.cooking\"]")

    # def limited_cooking_selection(self, i, j):
    #     '''Optional'''
    #     return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.grocery_quals.limited_cooking\"]")

    # def grills_selection(self, i, j):
    #     '''Optional'''
    #     return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.grocery_quals.grills\"]")

    def liquor_sales_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.grocery_quals.liquor_sales\"]")

    def auto_extinguish_selection(self, i, j):
        '''Optional'''
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.grocery_quals.auto_extinguish\"]")

    def operations_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.grocery_quals.operations\"]")

    def pct_occupied_input(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.grocery_quals.pct_occupied\"]")

    def flammable_materials_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.grocery_quals.flammable_materials\"]")

    # def flammable_desc_input(self, i, j):
    #     '''Optional'''
    #     return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.grocery_quals.flammable_desc\"]")

    def denied_insurance_selection(self, i, j):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.grocery_quals.denied_insurance\"]")
#HOTEL/MOTEL ADDITIONAL QUESTIONS

    def no_of_hotel_units_input(self, i, j): 
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.hotel_quals.num_hotel_units\"]")
    def hotels_are_all_hotels_equipped_with_smoke_detectors_selection(self, i, j): 
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.hotel_quals.smoke_detectors\"]")
    def hotels_are_room_entrance_doors_equipped_with_a_deadbolt_and_peephole_selection(self, i, j): 
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.hotel_quals.deadbolt\"]")
    def hotels_is_cooking_allowed_in_rooms_selection(self, i, j): 
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.hotel_quals.cooking\"]")
    def hotels_insured_has_been_in_business_in_min_of_2years_selection(self, i, j): 
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.hotel_quals.prior_experience\"]")
    def hotels_are_rooms_rented_in_long_term_basis_selection(self, i, j): 
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.hotel_quals.long_rent\"]")
    def hotels_is_there_restaurant_within_premises_selection(self, i, j): 
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.hotel_quals.restaurant\"]")

#DWELLING ADDITIONAL QUESTIONS
 
    def is_dwelling_occupied_selection(self, i, j): 
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.dwelling_quals.occupied\"]")
    def no_of_families_residing_selection(self, i, j): 
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.dwelling_quals.num_families\"]")
    def is_dwelling_seasonal_risk_selection(self, i, j): 
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.dwelling_quals.seasonal_risk\"]")
    def does_dwelling_contain_space_heater_selection(self, i, j): 
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.dwelling_quals.wood_burning_stove\"]")
    def dwelling_are_all_units_equipped_with_smoke_heaters_selection(self, i, j): 
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.dwelling_quals.smoke_detectors\"]")
    def dwelling_is_renters_insurance_reqd_selection(self, i, j): 
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.dwelling_quals.renters_insurance\"]")
    def dwelling_is_housing_subsidized_selection(self, i, j): 
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.dwelling_quals.subsidized_housing\"]")
#OTHER
    def describe_other_occupancy_input(self, i, j): 
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{j}.occupancy_otherg\"]")
  
#BUILDERS RISK ADDITIONAL QUESTIONS
#GROCERY STORE ADDITIONAL QUESTIONS
#CHURCH ADDITIONAL QUESTIONS

    def fill_building_information_form(self, params: BuildingInfoParams, location_idx: int = 0, building_idx: int = 0):
        i = location_idx
        j = building_idx

        self.street_address_input(i,j).fill(params.street)
        if params.Suite_Unit_floor:
            self.suit_unit_floor_input(i, j).fill(params.Suite_Unit_floor)
        if params.stories_Sq_Ft:
            self.no_of_stories_input(i, j).fill(params.stories_Sq_Ft)
            self.area_of_property_input(i, j).fill(params.stories_Sq_Ft)
        if params.year_built:
            self.year_built_input(i, j).fill(params.year_built)
        if params.construction:
            self.type_of_construction_select(i, j).select_option(params.construction)
            self.check_loading()
        if params.slate_Wood_shake_roof:
            self.does_buildong_have_slate_selection(i, j).select_option(params.slate_Wood_shake_roof)
            self.check_loading()
        print(params.occupancy)
        if params.occupancy:
            self.occupancy_selection(i, j).select_option(params.occupancy)
            self.check_loading()

            #newly added
        if "Manufacturer" in params.occupancy:
            self.type_of_manufacturing_selection(i, j).select_option(params.type_of_manufacturing)
            self.check_loading()          

        if "Church" in params.occupancy:
            # Required field (always fills)
            self.church_cooking_selection(i, j).select_option(params.building_occupancy.church_cooking)
            self.check_loading()

            # Optional field with visibility check
            if self.church_grills_selection(i, j).is_visible():
                self.church_grills_selection(i, j).select_option(params.building_occupancy.church_grills)
                self.check_loading()

            # Optional field with visibility check
            if self.church_auto_extinguish_selection(i, j).is_visible():
                self.church_auto_extinguish_selection(i, j).select_option(params.building_occupancy.church_auto_extinguish)
                self.check_loading()

        # BUILDERS RISK ADDITIONAL QUESTIONS
        if "Builders Risk" in params.occupancy:
            self.new_construction_selection(i, j).select_option(params.building_occupancy.brisk_new_construction)
            self.check_loading()

            self.floors_above_input(i, j).fill(params.building_occupancy.brisk_floors_above)
            self.floors_below_input(i, j).fill(params.building_occupancy.brisk_floors_below)

            self.start_date_input(i, j).fill(params.building_occupancy.brisk_start_date)
            self.end_date_input(i, j).fill(params.building_occupancy.brisk_end_date)

            self.lift_tilt_proto_selection(i, j).select_option(params.building_occupancy.brisk_lift_tilt_proto)
            self.check_loading()

            self.filled_land_selection(i, j).select_option(params.building_occupancy.brisk_filled_land)
            self.check_loading()

            # Optional field with visibility check
            if self.pilings_selection(i, j).is_visible():
                self.pilings_selection(i, j).select_option(params.building_occupancy.brisk_pilings)
                self.check_loading()

            self.project_desc_input(i, j).fill(params.building_occupancy.brisk_project_desc)

            self.standpipe_selection(i, j).select_option(params.building_occupancy.brisk_standpipe)
            self.check_loading()

            self.existing_structure_selection(i, j).select_option(params.building_occupancy.brisk_existing_structure)
            self.check_loading()

            # SAFEGUARDS / PROTECTIONS
            self.sprinkler_system_selection(i, j).select_option("No")
            self.check_loading()

            self.central_alarms_selection(i, j).select_option("No")
            self.check_loading()

            self.fenced_selection(i, j).select_option("No")
            self.check_loading()

            self.lighting_selection(i, j).select_option("No")
            self.check_loading()

            self.detection_systems_selection(i, j).select_option("No")
            self.check_loading()

            self.video_surveillance_selection(i, j).select_option("No")
            self.check_loading()

            self.safeguards_storage_selection(i, j).select_option("No")
            self.check_loading()

            # Optional input field with visibility check
            if self.other_protections_input().is_visible():
                self.other_protections_input().fill("N/A")
        
        # GROCERY STORE ADDITIONAL QUESTIONS
        if "Grocery Store" in params.occupancy:
            self.gas_station_selection(i, j).select_option(params.building_occupancy.grocery_gas_station)
            self.check_loading()

            self.cooking_selection(i, j).select_option(params.building_occupancy.grocery_cooking)
            self.check_loading()
        

            # Optional field with visibility check
            # if self.limited_cooking_selection(i, j).is_visible():
            #     self.limited_cooking_selection(i, j).select_option(params.building_occupancy.grocery_limited_cooking)
            #     self.check_loading()

            # Optional field with visibility check
            # if self.grills_selection(i, j).is_visible():
            #     self.grills_selection(i, j).select_option(params.building_occupancy.grocery_grills)
            #     self.check_loading()

            self.liquor_sales_input(i, j).fill(params.building_occupancy.grocery_liquor_sales)

            # Optional field with visibility check
            if self.auto_extinguish_selection(i, j).is_visible():
                self.auto_extinguish_selection(i, j).select_option(params.building_occupancy.grocery_auto_extinguish)
                self.check_loading()

            self.operations_input(i, j).fill(params.building_occupancy.grocery_operations)
            self.pct_occupied_input(i, j).fill(params.building_occupancy.grocery_pct_occupied)

            self.flammable_materials_selection(i, j).select_option(params.building_occupancy.grocery_flammable_materials)
            self.check_loading()

            # Optional field with visibility check
            # if self.flammable_desc_input(i, j).is_visible():
            #     self.flammable_desc_input(i, j).fill(params.building_occupancy.grocery_flammable_desc)

            self.denied_insurance_selection(i, j).select_option(params.building_occupancy.grocery_denied_insurance)
            self.check_loading()

        if params.building_value:
            self.building_value_input(i, j).fill(params.building_value)
        if params.good_condition:
            self.is_building_in_good_condition_selection(i, j).select_option(params.good_condition)
            self.check_loading()
        if params.valuation:
            self.valuation_input(i, j).select_option(params.valuation)
            self.check_loading()
        if params.coinsurance:
            if self.coinsurance_selection(i, j).is_visible():
                self.coinsurance_selection(i, j).select_option(params.coinsurance)
                self.check_loading()
            if self.deductible_selection(i, j).is_visible():
                self.deductible_selection(i, j).select_option(params.deductible)
                self.check_loading()
        self.risk_uninsured_select(i, j).select_option(params.risk_uninsured)
        self.check_loading()

        # Protection & Safeguards
        if self.risk_new_building(i,j).is_visible():
            self.risk_new_building(i,j).select_option(params.risk_new_buidling)
            self.check_loading()
        if self.risk_prior_carrier_input(i,j).is_visible():
            self.risk_prior_carrier_input(i,j).fill(params.risk_prior_carrier)
        if self.risk_prior_expiration_date_input(i,j).is_visible():
            self.risk_prior_expiration_date_input(i,j).fill(params.risk_prior_expiration_date)
        if self.risk_days_wo_insurance_input(i,j).is_visible():
            self.risk_days_wo_insurance_input(i,j).fill(params.risk_days_wo_insurance)
        self.check_loading()
        if params.hydrant_Dist:
            self.distance_to_hydrant_input(i, j).fill(params.hydrant_Dist)
        if params.dist_unit:
            self.distance_unit_input(i, j).select_option(params.dist_unit)
            self.check_loading()
        if params.fire_dept:
            self.is_the_fire_department_paid_or_volunteer_selection(i, j).select_option(params.fire_dept)
            self.check_loading()
        if params.sprinkler:
            self.is_the_building_equipped_with_sprinkler_system_selection(i, j).select_option(params.sprinkler)
            self.check_loading()
        if params.central_Alarm:
            self.does_building_contains_central_alarms_selection(i, j).select_option(params.central_Alarm)
            self.check_loading()

        # Building Updates
        print(f"roof updated year: {params.roof_updated_year}")
        if params.roof_updated_year:
            self.roof_input(i, j).fill(params.roof_updated_year)
        if params.electrical_updated_year:
            self.electrical_warning_input(i, j).fill(params.electrical_updated_year)
        if params.plumbing_updated_year:
            self.plumbing_input(i, j).fill(params.plumbing_updated_year)
        if params.HVAC_updated_year:
            self.HVAC_updated_year_input(i, j).fill(params.HVAC_updated_year)

        # 1. AWNING COVERAGE
        if params.awning_limit:
            self.awning_coverage_checkbox().click()
            self.check_loading()
            self.awning_limit_input(i, j).fill(str(params.awning_limit))
            if params.awning_valuation:
                self.awning_valuation_iselection(i, j).select_option(str(params.awning_valuation))
                self.check_loading()
            if params.awning_coinsurance:
                self.awning_coinsurance_selection(i, j).select_option(str(params.awning_coinsurance))
                self.check_loading()

        # 2. BUSINESS INTERRUPTION
        if params.business_interruption_limit:
            self.add_business_interruption_coverage_checkbox().click()
            self.check_loading()
            self.business_limit_input(i, j).fill(str(params.business_interruption_limit))
            if params.business_interruption_valuation:
                self.business_valuation_selection(i, j).select_option(params.business_interruption_valuation)
                self.check_loading()


        # 3. LOSS OF RENTS
        if params.loss_of_rents_limit:
            self.add_loss_of_rents_coverage_checkbox().click()
            self.check_loading()
            self.loss_of_rents_limit_input(i, j).fill(str(params.loss_of_rents_limit))
            if params.loss_of_rents_valuation:
                self.loss_of_rents_valuation_selection(i, j).select_option(str(params.loss_of_rents_valuation))
                self.check_loading()

        # 4. BUSINESS PERSONAL PROPERTY (BPP)
        if params.business_personal_property_limit:
            self.BPP_coverage_checkbox().click()
            self.check_loading()
            self.BPP_limit_input(i, j).fill(str(params.business_personal_property_limit))
            if params.business_personal_property_valuation:
                self.BPP_valuation_selection(i, j).select_option(str(params.business_personal_property_valuation))
                self.check_loading()
            if params.business_personal_property_coinsurance:
                self.BPP_coinsurance_selection(i, j).select_option(str(params.business_personal_property_coinsurance))
                self.check_loading()

        # 5. PUMPS AND CANOPY
        if params.pump_and_canopy_limit:
            self.canopy_coverage_checkbox().click()
            self.check_loading()
            self.canopy_limit_input(i, j).fill(str(params.pump_and_canopy_limit))
            if params.pump_and_canopy_valuation:
                self.canopy_valuation_selection(i, j).select_option(str(params.pump_and_canopy_valuation))
                self.check_loading()
            if params.pump_and_canopy_coinsurance:
                self.canopy_coinsurance_selection(i, j).select_option(str(params.pump_and_canopy_coinsurance))
                self.check_loading()

        # 6. RENOVATION COVERAGE
        # FOR CP
        # if params.renovation_limit:
        #     self.rennovation_coverage_checkbox().click()
        #     self.check_loading()
        #     self.rennovation_limit_input(i, j).fill(str(params.renovation_limit))
        #     if params.renovation_valuation:
        #         self.rennovation_valuation_selection(i, j).select_option(str(params.renovation_valuation))
        #         self.check_loading()
        #     if params.renovation_coinsurance:
        #         self.rennovation_coinsurance_selection(i, j).select_option(str(params.renovation_coinsurance))
        #         self.check_loading()
        #     if params.will_the_building_be_demolished:
        #         self.rennovation_will_building_be_demolished_selection(i, j).select_option(str(params.will_the_building_be_demolished))
        #         self.check_loading()
        #     if params.building_plans:
        #         self.rennovation_plan_of_building_input(i, j).fill(str(params.building_plans))
        #     print(f"start_date: {params.renovation_start_date}, end_date: {params.renovation_end_date}")
        #     if params.renovation_start_date:
        #         self.rennovation_expect_start_date_input(i, j).fill(params.renovation_start_date)
        #     if params.renovation_end_date:
        #         self.rennovation_expect_end_date_input(i, j).fill(params.renovation_end_date)

            # Fill Contractor details with dummy values since parameters aren't in dataclass
            if self.who_is_doing_work_checkbox(i,j).is_visible():
                self.who_is_doing_work_checkbox(i, j).select_option("Licensed General Contractor")
                self.check_loading()
                self.certificates_of_insurance_to_be_obtained_from_the_subcontractors_selection(i, j).select_option("No")
                self.check_loading()
                self.is_contractor_info_known_selection(i, j).select_option("No")
                self.check_loading()
                if self.license_no_input(i, j).is_visible(): 
                    self.license_no_input(i, j).fill("LIC123456")
                    self.no_of_years_in_business_input(i, j).fill("5")

        # 7. SIGN COVERAGE
        if params.sign_limit:
            self.sign_coverage_checkbox(i, j).click()
            self.check_loading()
            self.sign_limit_input(i, j).fill(str(params.sign_limit))
            if params.sign_valuation:
                self.sign_valuation_selection(i, j).select_option(str(params.sign_valuation))
                self.check_loading()
            if params.sign_coinsurance:
                self.sign_coinsurance_selection(i, j).select_option(str(params.sign_coinsurance))
                self.check_loading()

        # 8. SPOILAGE COVERAGE
        if params.spoilage_limit:
            self.spoilage_coverage_checkbox().click()
            self.check_loading()
            self.spoilage_limit_selection(i, j).select_option(str(params.spoilage_limit))
            self.check_loading()
            if params.spoilage_deductible:
                self.spoilage_deductible_input(i, j).fill(str(params.spoilage_deductible))
            if params.spoilage_contamination:
                self.spoilage_add_coverage_for_breakdown_selection(i, j).select_option(str(params.spoilage_contamination))
                self.check_loading()
            if params.spoilage_power_outage:
                self.spoilage_add_coverages_for_outages_selection(i, j).select_option(str(params.spoilage_power_outage))
                self.check_loading()
            if params.refrigeration_maintenance_agreement:
                self.spoilage_is_there_refrigeration_maintainence_agreement_selection(i, j).select_option(str(params.refrigeration_maintenance_agreement))
                self.check_loading()

        building_occupancy = params.building_occupancy
        print(building_occupancy)
        if "Vacant" in params.occupancy:
            self.is_new_purchase_selection(i, j).select_option(str(building_occupancy.vacant_new_purchase))
            self.check_loading()
            self.prior_occupancy_input(i, j).fill(str(building_occupancy.vacant_prior_occupancy))
            self.vacant_since_input(i, j).fill(str(building_occupancy.vacant_how_long_building_vacant))
            self.is_building_100_percent_vacant_selection(i, j).select_option(str(building_occupancy.vacant_is_building_100_percent_vacant))
            self.check_loading()
            self.any_structural_work_being_done_selection(i, j).select_option(str(building_occupancy.vacant_undergoing_renovation_or_demolition))
            self.check_loading()
            self.boarded_selection(i, j).select_option(str(building_occupancy.vacant_building_boarded_up))
            self.check_loading()
            self.locked_selection(i, j).select_option(str(building_occupancy.vacant_building_secured))
            self.check_loading()
            self.fenced_selection(i, j).select_option(str(building_occupancy.vacant_building_fenced))
            self.check_loading()
            self.is_electricity_still_active_selection(i, j).select_option(str(building_occupancy.vacant_electricity_turned_off))
            self.check_loading()
            self.intended_disposition_selection(i, j).select_option(str(building_occupancy.vacant_intended_disposition))
            self.check_loading()
            if self.will_heat_be_maintained_selection(i,j).is_visible():
                self.will_heat_be_maintained_selection(i, j).select_option(str(building_occupancy.vacant_active_heating))
                self.check_loading()
            self.is_plumbing_system_drained_selection(i, j).select_option(str(building_occupancy.vacant_plumbing_drained))
            self.check_loading()
            if self.is_water_still_active_selection(i, j).is_visible():
                self.is_water_still_active_selection(i, j).select_option(str(building_occupancy.vacant_water_turned_off))
                self.check_loading()
            if self.any_unfenced_pool_or_body_of_water_selection(i,j).is_visible(): 
                self.any_unfenced_pool_or_body_of_water_selection(i,j).select_option(params.unfenced_pool)
                self.check_loading()
            if self.is_gas_still_active_selection(i, j).is_visible(): 
                self.is_gas_still_active_selection(i, j).select_option(str(building_occupancy.vacant_gas_turned_off))
                self.check_loading()
            if self.is_located_on_more_than_2acres_selection(i,j).is_visible():
                self.is_located_on_more_than_2acres_selection(i,j).select_option("No")
                self.check_loading()

        if params.occupancy == "Manufacturer":
                    self.desc_of_manufacturing_options_input(i,j).fill(params.building_occupancy.manufacturer_desc_of_manufacturing_options)
                    self.does_manufacturer_do_any_woodwork_selection(i,j).select_option(params.building_occupancy.manufacturer_does_manufacturer_do_any_woodwork)
                    self.does_manufacturer_do_any_welding_selection(i,j).select_option(params.building_occupancy.manufacturer_does_manufacturer_do_any_welding)
                    self.does_manufacturer_use_any_flammable_chemicals_selection(i,j).select_option(params.building_occupancy.manufacturer_does_manufacturer_use_any_flammable_chemicals)
        
        if params.occupancy == "Garage (0931)":
            self.does_garage_only_engage_in_auto_glass_replacement_selection(i,j).select_option("No")
            self.does_garage_do_welding_torching_selection(i,j).select_option("No")
            self.is_garage_an_auto_body_shop_selection(i,j).select_option("No")
            self.is_garage_used_primarily_for_storage_of_tires_selection(i,j).select_option("No")

        if params.occupancy == "Apartment (0311 - 0313)":
            self.are_70_or_more_of_apartment_units_ocupied_selection(i,j).select_option("No")
            self.no_of_apartment_units_input(i,j).fill(params.building_occupancy.apartment_how_many_units_in_building)
            self.average_monthly_rent_input(i,j).fill("100000")
            self.is_heating_maintained_in_all_units_during_winter_months_selection(i,j).select_option("No")
            self.are_all_units_equipped_with_working_smoke_detectors_selection(i,j).select_option("No")
            self.is_outdoor_property_scheduled_selection(i,j).select_option("No")
            self.is_the_apartment_used_for_student_housing_selection(i,j).select_option("No")
            self.is_housing_subsidized_selection(i,j).select_option("No")
            self.insured_been_in_business_minimum_of_2years_OR_has_5years_of_management_experience_selection(i,j).select_option("No")
            self.is_renters_insurance_required_selection(i,j).select_option(params.renters_ins)
            self.is_there_a_resident_manager_selection(i,j).select_option("No")

        if params.occupancy == "Retail (0567)":
            self.type_of_retail_selection(i,j).select_option("Gift Shops")
            self.describe_type_of_retail_input(i,j).fill("Gift Shops")
            self.does_this_retail_establishment_sell_antiques_selections(i, j).select_option(params.retail_antiques)
            self.does_this_retail_establishment_have_refrigeration_units_selections(i, j).select_option(params.retail_refrigeration)

        if params.occupancy == "Warehouse(1212)":
            self.any_hazardous_material_storage_selection(i,j).select_option(params.building_occupancy.warehouse_are_any_flammable_or_hazardous_materials_stored)
            self.any_chemical_substance_storage_selection(i,j).select_option("No")
            self.any_explosive_storage_selection(i,j).select_option("No")
            self.any_firework_storage_selection(i,j).select_option("No")
            self.does_this_warehouse_has_refrigerating_units_selection(i,j).select_option(params.building_occupancy.does_this_warehouse_has_refrigerating_units)

        if params.occupancy == "Woodworking (3959)":
            self.are_all_wiping_cloths_selection(i,j).select_option("No")
            self.does_risk_have_dust_removal_system_selection(i,j).select_option("No")
            self.are_premises_well_kept_selection(i,j).select_option("Yes")

        if params.occupancy == "Social Club (0755-0756)":
            self.social_do_employees_cook_food_selection(i,j).select_option("No")

        if params.occupancy == "Office (0702)":
            self.describe_type_of_office_work_done_input(i,j).fill(params.building_occupancy.office_describe_the_type_of_office_use)

        if params.occupancy == "Restaurant (0532/0542/0545)":
            self.does_owner_have_at_least_2years_of_prior_restaurant_ownership_selection(i,j).select_option("No")
            self.does_restaurant_have_approved_ANSUL_selection(i,j).select_option("No")
            self.are_foods_prepared_cold_selection(i,j).select_option("No")
            self.percentage_of_sales_that_are_liquor_input(i,j).fill("45")

        if params.occupancy == "Hotel/Motel (0742 - 0747)":
            self.no_of_hotel_units_input(i,j).fill("50")
            self.hotels_are_all_hotels_equipped_with_smoke_detectors_selection(i,j).select_option("No")
            self.hotels_are_room_entrance_doors_equipped_with_a_deadbolt_and_peephole_selection(i,j).select_option("No")
            self.hotels_are_rooms_rented_in_long_term_basis_selection(i,j).select_option(params.building_occupancy.hotels_are_rooms_rented_on_a_longterm_basis)
            self.hotels_is_cooking_allowed_in_rooms_selection(i,j).select_option("No")
            self.hotels_insured_has_been_in_business_in_min_of_2years_selection(i,j).select_option("No")
            self.hotels_is_there_restaurant_within_premises_selection(i,j).select_option("No")

        if params.occupancy == "Health Care Facility - Assisted Living or Group Home (0852)":
            self.health_no_of_beds_in_facility_input(i,j).fill("250")
            self.healthare_all_beds_equipped_with_smoke_detector_selection(i,j).select_option("Yes")
            self.healthdo_employees_cook_food_selection(i,j).select_option("No")
            self.healthis_cooking_allowed_in_rooms_selection(i,j).select_option("No")
            self.healthis_owner_or_employees_on_site_24_hours(i,j).select_option("No")
            self.healthis_premises_smoke_free_selection(i,j).select_option("No")

        if params.occupancy == "Dwelling (1, 2, 3, or 4 Family) (0196 - 0198)":
            self.is_dwelling_occupied_selection(i,j).select_option("No")
            self.no_of_families_residing_selection(i,j).select_option("2")
            self.is_dwelling_seasonal_risk_selection(i,j).select_option("No")
            self.does_dwelling_contain_space_heater_selection(i,j).select_option("No")
            self.are_all_units_equipped_with_working_smoke_detectors_selection(i,j).select_option("No")
            self.dwelling_is_renters_insurance_reqd_selection(i,j).select_option("No")
            self.dwelling_is_housing_subsidized_selection(i,j).select_option("No")

        if params.occupancy == "Condominium (0331 - 0333)":
            self.condo_are_70_or_more_of_apartment_units_ocupied_selection(i,j).select_option("No")
            self.condo_are_all_units_equipped_with_working_smoke_detectors_selection(i,j).select_option("No")
            self.condo_no_of_units_input(i,j).fill(params.building_occupancy.Condominium_How_many_units_in_the_building)
            self.condo_are_units_rented_selection(i,j).select_option("No")
            self.condo_is_heating_maintained_in_all_units_during_winter_months_selection(i,j).select_option("No")
            self.condo_are_all_units_equipped_with_working_smoke_detectors_selection(i,j).select_option("No")
            self.condo_is_outdoor_property_scheduled_selection(i,j).select_option("No")
            self.condo_is_the_apartment_used_for_student_housing_selection(i,j).select_option("No")
            self.condo_is_housing_subsidized_selection(i,j).select_option("No")
            self.condo_insured_been_in_business_minimum_of_2years_OR_has_5years_of_management_experience_selection(i,j).select_option("No")

        if params.occupancy == "Other":
            print(params.desc_other_occupancy)
            self.describe_other_occupancy_input(i,j).fill(params.desc_other_occupancy)
        # Loss Payees Flow
        if params.loss_payees:
            self.does_building_have_loss_payee_selection(i, j).select_option("yes")
            for k, payee in enumerate(params.loss_payees):
                if k > 0:
                    self.add_another_loss_payee_btn.click()
                    self.check_loading()
                self.loss_payee_full_name_input(i, j, k).fill(payee.full_name)
                if payee.street1:
                    self.loss_payee_street_address1_input().fill(payee.street1)
                if payee.street2:
                    self.loss_payee_street_address2_input().fill(payee.street2)
                if payee.city:
                    self.loss_payee_city_input().fill(payee.city)
                if payee.state:
                    self.loss_payee_state_selection().select_option(payee.state)
                    self.check_loading()
                if payee.zip_code:
                    self.loss_payee_zip_input().fill(payee.zip_code)
                    self.check_loading()
                if payee.mortgagee:
                    self.is_loss_payee_mortgagee_slection(i, j, k).select_option(payee.mortgagee)
                    self.check_loading()
                if payee.loan_number:
                    self.loan_number_input(i, j, k).fill(payee.loan_number)
                if self.loss_payee_relationship_input(i,j,k).is_visible():
                    self.loss_payee_relationship_input(i,j,k).fill(payee.relationship)
                if self.loss_payee_financial_interest_select(i,j,k).is_visible():
                    self.loss_payee_financial_interest_select(i,j,k).select_option(payee.financial_interest)
        else:
            if self.does_building_have_loss_payee_selection(i, j).is_visible():
                self.does_building_have_loss_payee_selection(i, j).select_option("no")


    @staticmethod
    def get_vacant_prefix(occupancy_type: str) -> str:
        if "residential" in str(occupancy_type).lower():
            return "Vacant Residential — "
        return "Vacant Commercial — "

    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")