import random
from playwright.sync_api import Page, expect, TimeoutError
from models.home_owners_dwelling_info_params import HomeOwnersDwellingInfoParams

class HomeOwnersDwellingInformationPage:
    def __init__(self, page: Page):
        self.page = page

        self.home_owners_dwelling_information_heading = self.page.get_by_role("heading", name="    Homeowners")
        self.protection_class_select = self.page.locator("[id=\"ho.dwelling.protection_class\"]")
        self.adequate_water_select = self.page.locator("[id=\"ho.dwelling.adequate_water\"]")
        self.response_time_select = self.page.locator("[id=\"ho.dwelling.response_time\"]")
        self.accessible_property_select = self.page.locator("[id=\"ho.dwelling.accessible_property\"]")
        self.single_family_select = self.page.locator("[id=\"ho.dwelling.single_family\"]")
        self.owner_occupied_select = self.page.locator("[id=\"ho.dwelling.owner_occupied\"]")
        self.dwelling_type_select = self.page.locator("[id=\"ho.dwelling.dwelling_type\"]")
        self.manufactured_home_select = self.page.locator("[id=\"ho.dwelling.manufactured_home\"]")
        
        # Numeric Inputs & Details
        self.stories_input = self.page.locator("[id=\"ho.dwelling.stories\"]")
        self.year_built_input = self.page.locator("[id=\"ho.dwelling.year_built\"]")
        self.dwelling_area_input = self.page.get_by_role("spinbutton", description="Dwelling Area (sq. footage)", exact=True)
        
        # Condition & Construction
        self.good_condition_select = self.page.locator("[id=\"ho.dwelling.good_condition\"]")
        self.existing_damage_select = self.page.locator("[id=\"ho.dwelling.existing_damage\"]")
        self.renovation_or_construction_select = self.page.locator("[id=\"ho.dwelling.renovation_or_construction\"]")
        self.type_of_construction_select = self.page.locator("[id=\"ho.dwelling.type_of_construction\"]")
        self.type_of_foundation_select = self.page.locator("[id=\"ho.dwelling.type_of_foundation\"]")
        
        # Utilities & Plumbing
        self.central_heating_select = self.page.locator("[id=\"ho.dwelling.central_heating\"]")
        self.wood_burning_stove_select = self.page.locator("[id=\"ho.dwelling.wood_burning_stove\"]")
        self.polybutylene_or_qwest_plumbing_select = self.page.locator("[id=\"ho.dwelling.polybutylene_or_qwest_plumbing\"]")
        self.prim_heat_source_select = self.page.locator("[id=\"ho.dwelling.prim_heat_source\"]")
        self.water_heater_input = self.page.locator("[id=\"ho.dwelling.water_heater\"]")
        
        # Roof & Siding
        self.roofing_material_select = self.page.locator("[id=\"ho.dwelling.roofing_material\"]")
        self.flat_roof_select = self.page.locator("[id=\"ho.dwelling.flat_roof\"]")
        self.roof_year_input = self.page.locator("[id=\"ho.dwelling.roof_year\"]")
        self.siding_material_select = self.page.locator("[id=\"ho.dwelling.siding_material\"]")
        
        # Property & Liabilities
        self.over_two_acres_select = self.page.locator("[id=\"ho.dwelling.over_two_acres\"]")
        self.over_ten_acres_select = self.page.locator("[id=\"ho.dwelling.over_ten_acres\"]")
        self.unfenced_pool_select = self.page.locator("[id=\"ho.dwelling.unfenced_pool\"]")
        self.close_to_tidal_water_select = self.page.locator("[id=\"ho.dwelling.close_to_tidal_water\"]")
        self.horses_select = self.page.locator("[id=\"ho.dwelling.horses\"]")
        self.bite_history_select = self.page.locator("[id=\"ho.dwelling.bite_history\"]")
        self.business_pursuits_select = self.page.locator("[id=\"ho.dwelling.business_pursuits\"]")
        self.has_loss_payees_select = self.page.locator("[id=\"ho.dwelling.has_loss_payees\"]")

        # Update Years
        self.update_years_electricty_years_input = self.page.locator("[id=\"ho.dwelling.electricity_year\"]")
        self.update_years_plumbing_years_input = self.page.locator("[id=\"ho.dwelling.plumbing_year\"]")
        self.update_years_heating_ac_years_input = self.page.locator("[id=\"ho.dwelling.heating_ac_year\"]")
        self.update_years_updated_electrical_select = self.page.locator("[id=\"ho.dwelling.updated_electrical\"]")
        self.update_years_has_fuse_box_select = self.page.locator("[id=\"ho.dwelling.fuse_boxes\"]")
        self.update_years_has_knob_tube_select = self.page.locator("[id=\"ho.dwelling.knob_tube\"]")
        self.update_years_has_aluminium_wiring_select = self.page.locator("[id=\"ho.dwelling.aluminum\"]")
        self.update_years_has_lead_plumbing_select = self.page.locator("[id=\"ho.dwelling.lead_plumbing\"]")
        self.loading_screen = self.page.locator(".jss53")

        # loss payee
        self.add_another_loss_payee_btn = self.page.get_by_role("button", name="Add Another Loss Payee")
        self.home_owner_applicant_information_btn = self.page.get_by_role("button", name="Homeowners Applicant")

    
    def loss_payee_container(self, i):
        return self.page.locator("div").filter(has_text=f"Loss Payee #{i+1}").nth(-2)

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

    def loss_payee_mortgagee_select(self, i):
        return self.page.locator(f"[id=\"ho.dwelling.loss_payees.{i}.mortgagee\"]")
    
    def loss_payee_loan_number_input(self, i):
        return self.page.locator(f"[id=\"ho.dwelling.loss_payees.{i}.loan_number\"]")
    
    def loss_payee_are_mortgage_payments_current_select(self, i):
        return self.page.locator(f"[id=\"ho.dwelling.loss_payees.{i}.mortgage_payments\"]")
    
    def loss_payee_relationship_to_property_input(self, i):
        return self.page.locator(f"[id=\"ho.dwelling.loss_payees.{i}.relationship\"]")

    def loss_payee_is_there_financial_interest_select(self, i):
        return self.page.locator(f"[id=\"ho.dwelling.loss_payees.{i}.interest\"]")


    def fill_home_owners_dwelling_information_form(self, params: HomeOwnersDwellingInfoParams, data):
        expect(self.home_owners_dwelling_information_heading).to_be_visible()
        
        self.protection_class_select.select_option(params.protection_class)
        self.check_loading()
        self.adequate_water_select.select_option(params.adequate_water)
        self.check_loading()
        self.response_time_select.select_option(params.response_time)
        self.check_loading()
        self.accessible_property_select.select_option(params.accessible_property)
        self.check_loading()
        self.single_family_select.select_option(params.single_family)
        self.check_loading()
        self.owner_occupied_select.select_option(params.owner_occupied)
        self.check_loading()
        self.dwelling_type_select.select_option(params.dwelling_type)
        self.check_loading()
        self.manufactured_home_select.select_option(params.manufactured_home)
        self.check_loading()

        self.stories_input.fill(params.stories)
        self.year_built_input.fill(params.year_built)

        self.good_condition_select.select_option(params.good_condition)
        self.check_loading()
        self.existing_damage_select.select_option(params.existing_damage)
        self.check_loading()
        self.renovation_or_construction_select.select_option(params.renovation_or_construction)
        self.check_loading()
        self.type_of_construction_select.select_option(HomeOwnersDwellingInformationPage.get_construction_type(params.manufactured_home))
        self.check_loading()
        self.type_of_foundation_select.select_option(HomeOwnersDwellingInformationPage.get_masonry_type(params.type_of_foundation))
        self.check_loading()

        self.dwelling_area_input.fill(params.dwelling_area)

        self.central_heating_select.select_option(params.central_heating)
        self.check_loading()
        self.wood_burning_stove_select.select_option(params.wood_burning_stove)
        self.check_loading()
        self.polybutylene_or_qwest_plumbing_select.select_option(params.polybutylene_or_qwest_plumbing)
        self.check_loading()

        if self.prim_heat_source_select.is_visible():
            self.prim_heat_source_select.select_option(params.prim_heat_source) 
        
        self.check_loading()
        self.water_heater_input.fill(params.water_heater)
        self.check_loading()

        self.roofing_material_select.select_option(params.roofing_material)
        self.check_loading()
        self.flat_roof_select.select_option(params.flat_roof)
        self.check_loading()
        self.roof_year_input.fill(params.roof_year)
        self.check_loading()
        self.siding_material_select.select_option(params.siding_material)
        self.check_loading()

        self.over_two_acres_select.select_option(params.over_two_acres)
        self.check_loading()
        if self.over_ten_acres_select.is_visible():
            self.over_ten_acres_select.select_option(params.over_ten_acres)
        self.check_loading()
        self.unfenced_pool_select.select_option(params.unfenced_pool)
        self.check_loading()
        self.close_to_tidal_water_select.select_option(params.close_to_tidal_water)
        self.check_loading()
        self.horses_select.select_option(params.horses)
        self.check_loading()
        self.bite_history_select.select_option(params.bite_history)
        self.check_loading()
        self.business_pursuits_select.select_option(params.business_pursuits)
        self.check_loading()

        if self.update_years_electricty_years_input.is_visible():
            self.update_years_electricty_years_input.fill(params.update_years_electricty_years)
            self.update_years_heating_ac_years_input.fill(params.update_years_heating_ac_years)
            self.update_years_plumbing_years_input.fill(params.update_years_plumbing_years)
            self.update_years_has_aluminium_wiring_select.select_option(params.update_years_has_aluminium_wiring)
            self.check_loading()
            self.update_years_has_fuse_box_select.select_option(params.update_years_has_fuse_box)
            self.check_loading()
            self.update_years_has_knob_tube_select.select_option(params.update_years_has_knob_tube)
            self.check_loading()
            self.update_years_has_lead_plumbing_select.select_option(params.update_years_has_lead_plumbing)
            self.check_loading()
            self.update_years_updated_electrical_select.select_option(params.update_years_updated_electrical)
            self.check_loading()

        self.has_loss_payees_select.select_option("Yes")
        self.check_loading()

        print(f"Payess: {params.loss_payees}: Len: {params.loss_payees}")
        for i in range(0, params.loss_payees):
            self.loss_payee_full_name_input(i).fill(data["HO_LossPayees"][i]["Full Name"])
            self.loss_payee_street_address1_input(i).fill(data["HO_LossPayees"][i]["Street 1"])
            self.loss_payee_street_address2_input(i).fill(data["HO_LossPayees"][i]["Street 2"])
            self.loss_payee_zip_input(i).fill(data["HO_LossPayees"][i]["ZIP"])
            self.check_loading()
            self.loss_payee_mortgagee_select(i).select_option(data["HO_LossPayees"][i]["Is Mortgagee?"])
            if data["HO_LossPayees"][i]["Is Mortgagee?"] == "Yes":
                self.loss_payee_loan_number_input(i).fill(data["HO_LossPayees"][i]["Loan Number"])
                self.loss_payee_are_mortgage_payments_current_select(i).select_option(data["HO_LossPayees"][i]["Mortgage Current?"])
            else:
                self.loss_payee_relationship_to_property_input(i).fill("N/A")
                self.loss_payee_is_there_financial_interest_select(i).select_option("No")
            expect(self.add_another_loss_payee_btn).to_be_visible
            expect(self.add_another_loss_payee_btn).to_be_enabled
            if i+1 < params.loss_payees:
                self.add_another_loss_payee_btn.click()

        expect(self.home_owner_applicant_information_btn).to_be_visible()
        expect(self.home_owner_applicant_information_btn).to_be_enabled()
        self.home_owner_applicant_information_btn.click()
        
        
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
        
    @staticmethod
    def get_construction_type(is_manufactured: str):
        construction_types = None
        if is_manufactured == "Yes":
            construction_types = ["Modular", "Manufactured Home"]
        else:
            construction_types = ["Manufactured Home", "Condo", "Frame", "Log Home", "Masonry Veneer", "Mixed - Frame and Masonry", "Town Home"]

        if not construction_types:
            raise ValueError(f"invalid value is_manufactured: {is_manufactured}")
        
        return random.choice(construction_types)
        

        


