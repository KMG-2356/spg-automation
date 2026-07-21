import re
from playwright.sync_api import Page, expect, TimeoutError
from models.DF_location_params import DFlocationParams

class DFLocationPage:
    def __init__(self, page: Page):
       
            self.page = page
            self.street_address_input = self.page.get_by_role("textbox").first            
            self.city_input = self.page.get_by_role("textbox").nth(2)
            self.state_selection = self.page.get_by_role("combobox").first
            self.zip_input = self.page.get_by_role("textbox").nth(3)
            self.sq_footage_input = self.page.get_by_role("spinbutton", description="Square Footage? Required", exact=True)
    def cov_a_input(self,i):
        return self.page.page.locator(f"[id=\"df.locations.{i}.df_dwelling_value\"]")
    def cov_b_select(self,i):
        return self.page.locator(f"[id=\"df.locations{i}.df_exclude_cov_b\"]")   
    def increased_cov_b_input(self,i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_increased_cov_b\"]")
    def protection_class_seletion(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_protection_class\"]")
    def good_condition_selection(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_good_condition\"]")
    def existing_damage_selection(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_existing_damage\"]")
    def undergoing_renovation_selection(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_renovation_or_construction\"]")
    def single_family_selection(self, i):
        return self.page.locator("[id=\"df.locations.{i}.df_single_family_residence\"]")
    def number_of_families_selection(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_num_of_families\"]")
    def is_rented_selection(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_dwelling_rented\"]")  
    def type_of_occupancy_selection(self, i):
        return self.page.locator(f'[id=\"wd.locations.{i}.residential\"]')
    def rental_type_selection(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_rental_type\"]") 
    def is_rented_to_students_selection(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_rented_to_students\"]")
    def is_ins_reqd_selection(self, i):
        return self. page.locator(f"[id=\"df.locations.{i}.df_renters_insurance\"]")
    def year_built_input(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_year_built\"]")
    def is_ins_reqd_selection(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_renters_insurance\"]")
    def no_of_stories_input(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_stories\"]")
    def type_of_foundation_selection(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_type_of_foundation\"]")
    def type_of_construction_selection(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_type_of_construction\"]")
    def polybutylene_or_qwest_plumbing_selection(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_polybutylene_or_qwest_plumbing\"]")
    def central_heating_selection(self, i):
        return self.page.locator("[id=\"df.locations.{i}.df_central_heating\"]")
    def is_wood_burning_stove_selection(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_wood_burning_stove\"]")
    def is_primary_heat_source_selection(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_prim_heat_source\"]")
    def water_heater_input(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_water_heater\"]")
    def roofing_material_selection(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_roofing_material\"]")
    def flat_roof_selection(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_flat_roof\"]")
    def roof_year_input(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_roof_year\"]")    
    def siding_material_selection(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_siding_material\"]")
    def over_two_acres_selection(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_over_two_acres\"]")    
    def over_ten_acres_selection(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_over_ten_acres\"]")
    def unfenced_pool_selection(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_unfenced_pool\"]")
    def closed_to_tidal_selection(self, i):
        return self.page.locator("[id=\"df.locations.0.df_close_to_tidal_water\"]")
    def animal_biting_history_selection(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_bite_history\"]")
    def horses_on_premises_selection(self, i):
        return self.page.locator("[id=\"df.locations.{i}.df_central_heating\"]")
    def central_heating_selection(self, i):
        return self.page.locator("[id=\"df.locations.{i}.df_central_heating\"]")
    def business_pursuits_selection(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_business_pursuits\"]")
    def new_purchase_selection(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_new_purchase\"]")
    def year_purchased_input(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_year_purchased\"]")
    def prior_foreclosure_selection(self, i):
        return self.page.locator("[id=\"df.locations.0.df_prior_foreclosure\"]")
    def purchase_price_input(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_purchase_price\"]")
    
    def fill_df_location_information(self,params: DFlocationParams):
        
        for i in range(len(params.locations)):
            self.street_address_input.fill(params.locations[i]["Street Address"])
            self.check_loading()  
            self.city_input.fill(params.locations[i]["City"])
            self.check_loading() 
            self.state_selection.select_option(params.locations[i]["State"])           
            self.check_loading()            
            self.zip_input.fill(params.locations[i]["ZIP Code"])           
            self.check_loading() 
            self.cov_a_input.fill(params.locations[i]["Coverage A ($)"])           
            self.check_loading() 
            self.cov_b_select.select_option(params.locations[i]["Exclude Cov B?"])           
            self.check_loading() 
            if params.locations[i]["Coverage A ($)"]=="No":
                self.increased_cov_b_input.fill(params.locations[i]["Coverage B Value ($)"])           
                self.check_loading()
            self.new_purchase_selection.select_option(params.locations[i]["New Purchase?"])
            self.check_loading()
            self.year_purchased_input.fill(params.locations[i]["Year Purchased"]) 
            self.check_loading()
            self.prior_foreclosure_selection.select_option(params.locations[i]["Was Foreclosed When Purchased?"]) 
            self.check_loading()
            self.purchase_price_input.fill(params.locations[i]["Purchase Price ($)"]) 
            self.check_loading()
            self.good_condition_selection.select_option(params.locations[i]["Good Condition?"]) 
            self.check_loading()
            self.protection_class_seletion.select_option(params.locations[i]["Protection Class"]) 
            self.check_loading()
            self.existing_damage_selection.select_option(params.locations[i]["Existing Damage?"]) 
            self.check_loading()
            self.undergoing_renovation_selection.select_option(params.locations[i]["Undergoing Renovation?"])
            self.check_loading()
            self.single_family_selection.select_option(params.locations[i]["Single Family?"]) 
            self.check_loading()
            if (params.locations[i]["Single Family?"])=="No":
                self.number_of_families_selection.select_option(params.locations[i]["# Families"]) 
                self.check_loading()
            self.is_rented_selection.select_option(params.locations[i]["Is Rented?"]) 
            self.check_loading()
            if (params.locations[i]["Is Rented?"])=="Yes":
                self.rental_type_selection.select_option(params.locations[i]["Rental Type"]) 
                self.check_loading()
                self.is_rented_to_students_selection.select_option(params.locations[i]["Rented to Students?"]) 
                self.check_loading()
                self.is_ins_reqd_selection.select_option(params.locations[i]["Renters Ins Required?"]) 
                self.check_loading()
            self.sq_footage_input.fill(params.locations[i]["Sq Footage"]) 
            self.check_loading()
            self.year_built_input.fill(params.locations[i]["Year Built"]) 
            self.check_loading()
            self.no_of_stories_input.fill(params.locations[i]["# Stories"]) 
            self.check_loading()
            self.type_of_foundation_selection.select_option(params.locations[i]["Foundation Type"])
            self.check_loading()
            self.type_of_construction_selection.select_option(params.locations[i]["Construction Type"]) 
            self.check_loading()          
            self.polybutylene_or_qwest_plumbing_selection.select_option(params.locations[i]["Polybutylene / Qwest Plumbing?"]) 
            self.check_loading()
            self.central_heating_selection.select_option(params.locations[i]["Central Heating by Licensed Professional?"])
            self.check_loading()
            self.is_wood_burning_stove_selection.select_option(params.locations[i]["Wood Burning Stove?"]) 
            self.check_loading()
            if (params.locations[i]["Wood Burning Stove?"])=="Yes":
                self.water_heater_input.select_option(params.locations[i]["Wood Stove Primary Heat?"]) 
                self.check_loading()
            # self.roof_year_input.select_option(params.locations[i]["Water Heater Year"])
            # self.check_loading()
            self.roofing_material_selection.select_option(params.locations[i]["Roofing Material"]) 
            self.check_loading()
            self.flat_roof_selection.select_option(params.locations[i]["Flat Roof?"]) 
            self.check_loading()
            self.roof_year_input.select_option(params.locations[i]["Roof Replacement Year"])
            self.check_loading()
            self.siding_material_selection.select_option(params.locations[i]["Siding Material"]) 
            self.check_loading()
            self.over_two_acres_selection.select_option(params.locations[i]["> 2 Acres?"]) 
            self.check_loading()
            if (params.locations[i]["> 2 Acres?"])=="Yes":
                self.over_ten_acres_selection.select_option(params.locations[i]["> 10 Acres?"]) 
                self.check_loading()
            self.unfenced_pool_selection.select_option(params.locations[i]["Unfenced Pool?"]) 
            self.check_loading()
            self.closed_to_tidal_selection.select_option(params.locations[i]["Within 1,000 ft of Ocean / Bay / Sound?"]) 
            self.check_loading()
            self.animal_biting_history_selection.select_option(params.locations[i]["Animals With Bite History?"]) 
            self.check_loading()
            self.horses_on_premises_selection.select_option(params.locations[i]["Horses on Premises?"]) 
            self.check_loading()
            self.business_pursuits_selection.select_option(params.locations[i]["Business Pursuits?"]) 
            self.check_loading()

            # expect(self.location_management_btn).to_be_visible()
            # expect(self.location_management_btn).to_be_enabled()
            # self.location_management_btn.click()
            # self.check_loading()

            if i < (len(params.locations)) - 1:
            #   expect(self.add_location_button).to_be_visible()
            #   expect(self.add_location_button).to_be_enabled()
              self.add_location_button.click()

    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")
  



