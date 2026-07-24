import re
from playwright.sync_api import Page, expect, TimeoutError
from models.DF_location_params import DFlocationParams
from models.DF_loss_payee_params import DFlossPayeeParams
from page_objects.DF_loss_payee_page import DFLossPayeePage

class DFLocationPage:
    def __init__(self, page: Page):
        self.page = page
        self.loss_payee_page = DFLossPayeePage(self.page)
        self.street_address_input = self.page.locator("div").filter(has_text="Street Address 1").locator("input").nth(0)          
        self.city_input = self.page.locator("div").filter(has_text="city").locator("input").nth(2)
        self.state_selection = self.page.locator("div").filter(has_text="state").locator("select").nth(0)
        self.zip_input = self.page.locator("div").filter(has_text="zip").locator("input").nth(3)
        self.sq_footage_input = self.page.get_by_role("spinbutton", description="Square Footage? Required", exact=True)
        self.location_management_btn = self.page.locator("button").filter(has_text="Dwelling Fire Location Management")
        self.dwelling_fire_heading = self.page.get_by_role("heading", name="    Dwelling Fire")
        self.add_loss_payee_btn = self.page.get_by_role("button", name="Add Another Loss Payee")
        self.df_add_another_location_btn = self.page.get_by_role("button", name="Add Another Location")
        self.df_applicant_information_btn = self.page.get_by_role("button", name="Dwelling Fire Applicant")
        self.loading_screen = self.page.locator(".jss53")


    def cov_a_input(self,i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_dwelling_value\"]")
    def cov_b_select(self,i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_exclude_cov_b\"]")   
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
        return self.page.locator(f"[id=\"df.locations.{i}.df_single_family_residence\"]")
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
        return self.page.locator(f"[id=\"df.locations.{i}.df_close_to_tidal_water\"]")
    def animal_biting_history_selection(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_bite_history\"]")
    def horses_on_premises_selection(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_horses\"]")
    def central_heating_selection(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_central_heating\"]")
    def business_pursuits_selection(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_business_pursuits\"]")
    def new_purchase_selection(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_new_purchase\"]")
    def year_purchased_input(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_year_purchased\"]")
    def prior_foreclosure_selection(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_prior_foreclosure\"]")
    def purchase_price_input(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_purchase_price\"]")
    def square_footage_input(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_area\"]")
    def single_wide_home_select(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_single_wide\"]")
    def located_in_mobile_park_select(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_trailer_park\"]")
    def lot_owned_select(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_owned_lot\"]")
    def electricity_year_input(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_electricity_year\"]")
    def plumbing_year_input(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_plumbing_year\"]")
    def heating_ac_year_input(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_heating_ac_year\"]")
    def updated_electrical_select(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_updated_electrical\"]")
    def fuse_box_select(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_fuse_boxes\"]")
    def knob_and_tube_wiring_select(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_knob_tube\"]")
    def aluminium_wiring_select(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_aluminum\"]")
    def lead_plumbing_select(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_lead_plumbing\"]")
    def rented_airbnb_select(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_airbnb\"]")
    def has_loss_payee_select(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_has_loss_payees\"]")
    def is_loss_payee_mortgage_selection(self,i, j):
        return self.page.locator(f"[id=\"df.locations.{i}.loss_payees.{j}.df_mortgagee\"]")
    def loss_payee_loan_number_input(self, i, j):
        return self.page.locator(f"[id=\"df.locations.{i}.loss_payees.{j}.df_loan_number\"]")
    def loss_payee_is_mortgage_current_selection(self, i, j):
        return self.page.locator(f"[id=\"df.locations.{i}.loss_payees.{j}.df_mortgage_payments\"]")
    def loss_payee_container(self, i):
        return self.page.locator(".MuiGrid-container").filter(has_text="Loss Payee").nth(-2)
    def loss_payee_full_name_input(self, i):
        return self.loss_payee_container(i).locator("div input").nth(0)
    def loss_payee_street_address1_input(self, i):
        return self.loss_payee_container(i).locator("div input").nth(1)
    def loss_payee_street_address2_input(self, i):
        return self.loss_payee_container(i).locator("div input").nth(2)
    def loss_payee_city_input(self, i):
        return self.loss_payee_container(i).locator("div input").nth(3)
    def loss_payee_state_select(self, i):
        return self.loss_payee_container(i).locator("div select").first
    def loss_payee_zip_input(self, i):
        return self.loss_payee_container(i).locator("div input").nth(4)
    def loss_payee_relationship_to_property_input(self, i, j):
        return self.page.locator(f"[id=\"df.locations.{i}.loss_payees.{j}.relationship\"]")
    def loss_payee_financial_interest_select(self, i, j):
        return self.page.locator(f"[id=\"df.locations.{i}.loss_payees.{j}.interest\"]")
    
    def fill_df_location_information(self, params: DFlocationParams, loss_payee_params: DFlossPayeeParams):
        expect(self.dwelling_fire_heading).to_be_visible()
        for i in range(len(params.locations)):
            self.zip_input.fill(params.locations[i]["ZIP Code"])           
            self.check_loading() 
            self.street_address_input.fill(params.locations[i]["Street Address"])
            self.city_input.fill(params.locations[i]["City"])
            self.state_selection.select_option(params.locations[i]["State"])           
            self.check_loading()            
            self.cov_a_input(i).fill(params.locations[i]["Coverage A ($)"])           
            self.cov_b_select(i).select_option(params.locations[i]["Exclude Cov B?"])           
            self.check_loading() 
            if self.increased_cov_b_input(i).is_visible():
                self.increased_cov_b_input(i).fill(params.locations[i]["Coverage B Value ($)"])           
            self.new_purchase_selection(i).select_option(params.locations[i]["New Purchase?"])
            self.check_loading()
            self.year_purchased_input(i).fill("2000" if params.locations[i]["Year Purchased"] == "" else params.locations[i]["Year Purchased"]) 
            self.prior_foreclosure_selection(i).select_option("No" if params.locations[i]["Was Foreclosed When Purchased?"] == "" else params.locations[i]["Was Foreclosed When Purchased?"]) 
            self.check_loading() 
            self.purchase_price_input(i).fill("10" if params.locations[i]["Purchase Price ($)"] == "" else params.locations[i]["Purchase Price ($)"]) 
            self.good_condition_selection(i).select_option(params.locations[i]["Good Condition?"]) 
            self.check_loading()
            self.protection_class_seletion(i).select_option(params.locations[i]["Protection Class"]) 
            self.check_loading()
            self.existing_damage_selection(i).select_option(params.locations[i]["Existing Damage?"]) 
            self.check_loading()
            self.undergoing_renovation_selection(i).select_option(params.locations[i]["Undergoing Renovation?"])
            self.check_loading()
            self.single_family_selection(i).select_option(params.locations[i]["Single Family?"]) 
            self.check_loading()
            if self.number_of_families_selection(i).is_visible():
                self.number_of_families_selection(i).select_option(params.locations[i]["# Families"]) 
                self.check_loading()
            self.is_rented_selection(i).select_option(params.locations[i]["Is Rented?"]) 
            self.check_loading()
            if self.rental_type_selection(i).is_visible():
                self.rental_type_selection(i).select_option(params.locations[i]["Rental Type"]) 
                self.check_loading()
                self.is_rented_to_students_selection(i).select_option(params.locations[i]["Rented to Students?"]) 
                self.check_loading()
                self.is_ins_reqd_selection(i).select_option(params.locations[i]["Renters Ins Required?"]) 
                self.check_loading()
            self.square_footage_input(i).fill(params.locations[i]["Sq Footage"])
            self.check_loading()
            self.no_of_stories_input(i).fill(params.locations[i]["# Stories"]) 
            self.check_loading()
            self.year_built_input(i).fill(params.locations[i]["Year Built"])
            self.check_loading()
            self.type_of_foundation_selection(i).select_option(DFLocationPage.get_masonry_type(params.locations[i]["Foundation Type"]))
            self.check_loading()
            self.type_of_construction_selection(i).select_option(params.locations[i]["Construction Type"]) 
            self.check_loading()          
            self.polybutylene_or_qwest_plumbing_selection(i).select_option(params.locations[i]["Polybutylene / Qwest Plumbing?"]) 
            self.check_loading()
            self.central_heating_selection(i).select_option(params.locations[i]["Central Heating by Licensed Professional?"])
            self.check_loading()
            if self.single_wide_home_select(i).is_visible():
                self.single_wide_home_select(i).select_option(params.single_wide_home)
                self.located_in_mobile_park_select(i).select_option(params.located_in_mobile_park)
                self.lot_owned_select(i).select_option(params.lot_owned)
            if self.is_wood_burning_stove_selection(i).is_visible():
                self.is_wood_burning_stove_selection(i).select_option(params.locations[i]["Wood Burning Stove?"]) 
            self.check_loading()
            if self.water_heater_input(i).is_visible():
                self.water_heater_input(i).fill(params.locations[i]["Water Heater Year"]) 
            if self.is_primary_heat_source_selection(i).is_visible():
                self.is_primary_heat_source_selection(i).select_option("No" if params.locations[i]["Wood Stove Primary Heat?"] == "" else params.locations[i]["Wood Stove Primary Heat?"])
                self.check_loading()
            self.roofing_material_selection(i).select_option(params.locations[i]["Roofing Material"]) 
            self.check_loading()
            self.flat_roof_selection(i).select_option(params.locations[i]["Flat Roof?"]) 
            self.check_loading()
            self.roof_year_input(i).fill(params.locations[i]["Roof Replacement Year"])
            self.check_loading()
            self.siding_material_selection(i).select_option(params.locations[i]["Siding Material"]) 
            self.check_loading()
            self.over_two_acres_selection(i).select_option(params.locations[i]["> 2 Acres?"]) 
            self.check_loading()
            if self.over_ten_acres_selection(i).is_visible():
                self.over_ten_acres_selection(i).select_option(params.locations[i]["> 10 Acres?"]) 
                self.check_loading()
            self.unfenced_pool_selection(i).select_option(params.locations[i]["Unfenced Pool?"]) 
            self.check_loading()
            self.closed_to_tidal_selection(i).select_option(params.locations[i]["Within 1,000 ft of Ocean / Bay / Sound?"]) 
            self.check_loading()
            self.animal_biting_history_selection(i).select_option(params.locations[i]["Animals With Bite History?"]) 
            self.check_loading()
            self.horses_on_premises_selection(i).select_option(params.locations[i]["Horses on Premises?"]) 
            self.check_loading()
            self.business_pursuits_selection(i).select_option(params.locations[i]["Business Pursuits?"]) 
            self.check_loading()

            if self.electricity_year_input(i).is_visible():
                self.electricity_year_input(i).fill(params.locations[i]["Electrical Update Year"])
                self.plumbing_year_input(i).fill(params.locations[i]["Plumbing Update Year"])
                self.heating_ac_year_input(i).fill(params.locations[i]["HVAC Update Year"])
                self.updated_electrical_select(i).select_option(params.locations[i]["100 Amp+ Electrical?"])
                self.check_loading()
                self.fuse_box_select(i).select_option(params.locations[i]["Fuse Boxes?"])
                self.check_loading()
                self.knob_and_tube_wiring_select(i).select_option(params.locations[i]["Knob / Tube Wiring?"])
                self.check_loading()
                self.aluminium_wiring_select(i).select_option(params.locations[i]["Aluminum Wiring?"])
                self.check_loading()
                self.lead_plumbing_select(i).select_option(params.locations[i]["Lead Plumbing?"])
                self.check_loading()
                self.rented_airbnb_select(i).select_option(params.locations[i]["AirBNB / Short-Term Rental?"])
                self.check_loading()

            current_loc_payees = [
                lp for lp in loss_payee_params.loss_payee
                if str(lp["Loc #"]).strip() == str(i + 1)
            ]

            if len (current_loc_payees) > 0:
                self.has_loss_payee_select(i).select_option("Yes")
                self.check_loading()
            else:
                self.has_loss_payee_select(i).select_option("No")
                self.check_loading()

            for j, loss_p in enumerate(current_loc_payees):
                if j > 0:
                    self.add_loss_payee_btn.click()
                    self.check_loading()
                self.loss_payee_full_name_input(j).fill(loss_p["Full Name"])
                self.loss_payee_street_address1_input(j).fill(loss_p["Street 1"])
                self.loss_payee_zip_input(j).fill(loss_p["ZIP"])
                self.check_loading()
                self.loss_payee_city_input(j).fill(loss_p["City"])
                self.loss_payee_state_select(j).select_option(loss_p["State"])           
                self.check_loading()
                self.is_loss_payee_mortgage_selection(i, j).select_option(loss_p["Is Mortgagee?"])
                self.check_loading()
                if self.loss_payee_loan_number_input(i, j).is_visible():
                    self.loss_payee_loan_number_input(i,j).fill("N/A" if loss_p["Loan Number"] == "" else loss_p["Loan Number"])
                if self.loss_payee_is_mortgage_current_selection(i,j).is_visible():
                    self.loss_payee_is_mortgage_current_selection(i,j).select_option("No" if loss_p["Mortgage Current?"] == "" else loss_p["Mortgage Current?"])
                if self.loss_payee_relationship_to_property_input(i,j).is_visible():
                    self.loss_payee_relationship_to_property_input(i,j).fill("N/A")
                if self.loss_payee_financial_interest_select(i,j).is_visible():
                    self.loss_payee_financial_interest_select(i,j).select_option("No")

            if i < (len(params.locations)) - 1:
                expect(self.location_management_btn).to_be_visible()
                expect(self.location_management_btn).to_be_enabled()
                self.location_management_btn.click()
                expect(self.dwelling_fire_heading).to_be_visible()
                self.df_add_another_location_btn.click()
                expect(self.dwelling_fire_heading).to_be_visible()

        expect(self.location_management_btn).to_be_visible()
        expect(self.location_management_btn).to_be_enabled()
        self.location_management_btn.click()
        expect(self.df_applicant_information_btn).to_be_visible()
        expect(self.df_applicant_information_btn).to_be_enabled()
        self.df_applicant_information_btn.click()


    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")
  

    @staticmethod
    def get_masonry_type(foundation_type: str) -> str:
        if "Permanent Masonry" in foundation_type:
            return "Permanent Masonry (Slab, Crawlspace, or Basement)"
        else:
            return foundation_type

