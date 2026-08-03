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
    def awning_coverage_selection(self,i):
        return self.page.locator("div").filter(has_text=re.compile(r"^Add Awning coverage\?$")).nth(0)
    def awning_limit_input(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.awning.limit\"]")
    def awning_valuation_iselection(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.awning.valuation\"]")
    def awning_coinsurance_selection(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.awning.coinsurance\"]")
    def add_business_interruption_coverage_selection(self,i):
        return self.page.locator("div").filter(has_text=re.compile(r"^Add Business Interruption coverage\?$")).nth(0)
    def business_limit_input(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.bintr.limit\"]")
    def business_valuation_selection(self,i):
        return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.bintr.limit\"]")
    def business_valuation_selection(self,i):
            return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.bintr.limit\"]")
    
    
    #LOSS PAYEE

    def loss_payee_full_name_input(self, i):
            return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.updates.heating_ac\"]")
    def loss_payee_street_address1_input(self, i):
            return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.updates.heating_ac\"]")
    def HVAC_updated_year_input(self, i):
            return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.updates.heating_ac\"]")
    def HVAC_updated_year_input(self, i):
            return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.updates.heating_ac\"]")
    def HVAC_updated_year_input(self, i):
            return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.updates.heating_ac\"]")
    def HVAC_updated_year_input(self, i):
            return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.updates.heating_ac\"]")
    def HVAC_updated_year_input(self, i):
            return self.page.locator(f"[id=\"property_.locations.{i}.buildings.{i}.updates.heating_ac\"]")
    

    
  
    
       

    def fill_building_information_form(self, params: BuildingInfoParams):  
        for i, building in enumerate
        self.street_address_input(i).fill(params.ZIP_code)
        if params.same_as_insured == "No":
            self.is_same_as_insured_selection.select_option(params.same_as_insured)
            self.check_loading()
            self.insured_full_name_input.fill(params.contact_full_name)
            self.insured_contact_email_input.fill(params.contact_email)
            self.insured_contact_phone_number_input.fill(params.contact_phone)        
        if params.same_as_insured == "Yes":
            self.insured_full_name_person_to_contact_input.fill(params.contact_full_name)           
        
        expect(self.loss_history_btn).to_be_visible()
        expect(self.loss_history_btn).to_be_enabled()
        self.loss_history_btn.click()

    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")

