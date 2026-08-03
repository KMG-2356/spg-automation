import re
from playwright.sync_api import Page, expect, TimeoutError
from models.property_building_params import BuildingInfoParams

class AdditionalQuestionsPage:
    def __init__(self, page: Page):
        self.page = page
        self.loss_history_btn = self.page.get_by_role("button", name="Location Management")
        self.loading_screen = self.page.locator(".jss53")
    def street_address_input(self, i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.address\"]")
    def suit_unit_floor_input(self, i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.address2\"]")
    def no_of_stories_input(self, i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.stories\"]")
    def area_of_property_input(self, i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.sqfeet\"]")
    def year_built_input(self, i):
        return self.page.locator(f"property_.locations.{i}.buildings.{i}.year_built\"]")
    def type_of_construction_select(self, i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.construction\"]")
    def occupancy_selection(self, i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.occupancy\"]")
    def building_value_input(self, i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.value\"]")
    def is_building_in_good_condition_selection(self, i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.good_condition\"]")
    def valuation_input(self, i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.valuation\"]")
    def does_buildong_have_slate_selection(self, i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.roof_type\"]")
    def coinsurance_selection(self, i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.coinsurance\"]")
    def deductible_selection(self, i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.deductible\"]")
    def distance_to_hydrant_input(self, i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.distance_to_hydrant\"]")
    def distance_unit_input(self, i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.distance_unit\"]")
    def is_the_fire_department_paid_or_volunteer_selection(self, i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.fire_department\"]")
    def is_the_building_equipped_with_sprinkler_system_selection(self, i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.safeguards.sprinkler_system\"]")
    def does_building_contains_central_alarms_selection(self, i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.safeguards.central_alarms\"]")
    def roof_input(self, i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.distance_to_hydrant\"]")
    def electrical_warning_input(self, i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.updates.electricity\"]")
    def plumbing_input(self, i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.updates.plumbing\"]")
    def HVAC_updated_year_input(self, i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.updates.heating_ac\"]")
    #AWNING COVERAGE
    def awning_coverage_selection(self,i):
        return self.page.get_by_text("Add Awning coverage?")
    def awning_limit_input(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.awning.limit\"]")
    def awning_valuation_iselection(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.awning.valuation\"]")
    def awning_coinsurance_selection(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.awning.coinsurance\"]")
    #ADD BUSINESS INTERRUPTION
    def add_business_interruption_coverage_selection(self,i):
        return self.page.get_by_text("Add Business Interruption coverage?")
    def business_limit_input(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.bintr.limit\"]")
    def business_valuation_selection(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.bintr.limit\"]")
    #ADD LOSS OF RENTS
    def add_loss_of_rents_coverage_selection(self,i):
        return self.page.get_by_text("Add Loss of Rents coverage?")
    def loss_of_rents_limit_input(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.lor.limit\"]")
    def loss_of_rents_valuation_selection(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.lor.valuation\"]")
    #ADD BUSINESS PERSONAL PROPERTY COVERAGE
    def BPP_coverage_selection(self,i):
        return self.page.get_by_text("Add Business Personal Property coverage?")
    def BPP_limit_input(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.bpp.limit\"]")
    def BPP_valuation_selection(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.bpp.valuation\"]")
    def BPP_coinsurance_selection(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.bpp.coinsurance\"]")
    #ADD PUMPS AND CANOPY COVERAGE
    def canopy_coverage_selection(self,i):
        return self.page.get_by_text("Add Pumps and Canopy coverage?")
    def canopy_limit_input(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.canopy.limit\"]")
    def canopy_valuation_selection(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.canopy.valuation\"]")
    def canopy_coinsurance_selection(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.canopy.coinsurance\"]")
    #ADD RENOVATION COVERAGE
    def rennovation_coverage_selection(self,i):
        return self.page.get_by_text("Add Renovation coverage?")
    def rennovation_limit_input(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.reno.limit\"]")
    def rennovation_valuation_selection(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.reno.valuation\"]")
    def rennovation_coinsurance_selection(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.reno.coinsurance\"]")
    def rennovation_will_building_be_demolished_selection(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.reno.demolished\"]")
    def rennovation_plan_of_building_input(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.reno.plans\"]")
    def rennovation_expect_start_date_input(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.reno.start_date\"]")
    def rennovation_expect_end_date_input(self,i):
            return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.reno.end_date\"]")
    #ADD SIGN COVERAGE
    def sign_coverage_selection(self,i):
        return self.page.get_by_text("Add Sign coverage?")
    def sign_limit_input(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.sign.limit\"]")
    def sign_valuation_selection(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.sign.valuation\"]")
    def sign_coinsurance_selection(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.sign.coinsurance\"]")
   #ADD SPOILAGE COVERAGE
    def spoilage_coverage_selection(self,i):
        return self.page.get_by_text("Add Renovation coverage?")
    def spoilage_limit_selection(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.spoilage.limit\"]")
    def spoilage_deductible_input(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.spoilage.deductible\"]")
    def spoilage_add_coverage_for_breakdown_selection(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.spoilage.contamination\"]")
    def spoilage_add_coverages_for_outages_selection(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.spoilage.power_outage\"]")
    def spoilage_is_there_refrigeration_maintainence_agreement_selection(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.spoilage.refrig_maint_agreement\"]")

    #CONTRCTOR INFO
    def who_is_doing_work_selection(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.contractor.contractor_type\"]")
    def certificates_of_insurance_to_be_obtained_from_the_subcontractors_selection(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.contractor.ai_cert\"]")
    def is_contractor_info_known_selection(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.contractor.info_known\"]")
    def license_no_input(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.contractor.license_no\"]")
    def no_of_years_in_business_input(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.contractor.years_operating\"]")
    #LOSS PAYEE
    def does_building_have_loss_payee_selection(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.has_loss_payees\"]")     
    def loss_payee_full_name_input(self, i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.loss_payees.{i}.name\"]")
    def loss_payee_street_address1_input(self, i):
        return self.page.locator
    def loss_payee_street_address2_input(self, i):
        return self.page.locator
    def loss_payee_city_input(self, i):
        return self.page.locator
    def loss_payee_state_selection(self, i):
        return self.page.locator
    def loss_payee_zip_input(self, i):
        return self.page.locator
    def is_loss_payee_mortgagee_slection(self, i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.loss_payees.{i}.mortgagee\"]")
    def loan_number_input(self, i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.loss_payees.{i}.loan_number\"]")
    

    
  
    
       

    # def fill_building_information_form(self, params: BuildingInfoParams):  

    #     self.street_address_input(i).fill(params.ZIP_code)
    #     if params.same_as_insured == "No":
    #         self.is_same_as_insured_selection.select_option(params.same_as_insured)
    #         self.check_loading()
    #         self.insured_full_name_input.fill(params.contact_full_name)
    #         self.insured_contact_email_input.fill(params.contact_email)
    #         self.insured_contact_phone_number_input.fill(params.contact_phone)        
    #     if params.same_as_insured == "Yes":
    #         self.insured_full_name_person_to_contact_input.fill(params.contact_full_name)           
        
    #     expect(self.loss_history_btn).to_be_visible()
    #     expect(self.loss_history_btn).to_be_enabled()
    #     self.loss_history_btn.click()

    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")

