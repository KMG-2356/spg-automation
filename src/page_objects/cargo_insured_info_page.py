from playwright.sync_api import Page, expect, TimeoutError
from models.cargo_insured_info_params import CargoInsuredInformationParams

class CargoInsuredInformationPage:
    def __init__(self, page: Page):
        self.page = page
        self.insured_name_input = self.page.locator("[id=\"insured.name\"]")
        self.insured_entity_select = self.page.locator("[id=\"insured.entity\"]")
        self.insured_email_input = self.page.locator("[id=\"insured.email\"]")
        self.inured_phone_input = self.page.locator("[id=\"insured.phone\"]")
        self.insured_street_address_1_input = self.page.get_by_role("textbox").nth(3)
        self.insured_street_address_2_input = self.page.get_by_role("textbox").nth(4)
        self.insured_city_input = self.page.get_by_role("textbox").nth(5)
        self.insured_state_select = self.page.get_by_role("combobox").nth(1)
        self.insured_zip_input = self.page.locator("text=Mailing Address").locator("..").locator("input").nth(3)
        self.insured_is_new_venture_selection = self.page.locator("[id=\"insured.new_venture\"]")
        self.insured_icc_input = self.page.locator("[id=\"insured.insured_icc\"]")
        self.insured_are_filling_selection = self.page.locator("[id=\"insured.filings\"]")
        self.insured_all_owned_units_selection = self.page.locator("[id=\"insured.all_owned_units\"]")
        self.insured_carrier_type_selection = self.page.locator("[id=\"insured.carrier_type\"]")
        self.insured_own_goods_selection = self.page.locator("[id=\"insured.own_goods\"]")
        self.insured_garage_same_selection = self.page.locator("[id=\"insured.garage_same\"]")
        self.insured_garaging_address1_input = self.page.locator("text=Primary Garaging Address").locator("..").locator("input").nth(0)
        self.insured_garaging_address2_input = self.page.locator("text=Primary Garaging Address").locator("..").locator("input").nth(1)
        self.insured_garaging_city_input = self.page.locator("text=Primary Garaging Address").locator("..").locator("input").nth(2)
        self.insured_garaging_state_selection = self.page.locator("text=Primary Garaging Address").locator("..").locator("select").nth(1)
        self.insured_garaging_zip_input = self.page.locator("text=Primary Garaging Address").locator("..").locator("input").nth(3)
        self.insured_garaging_secondary_selection = page.locator("[id=\"insured.secondary_garaging\"]")
        self.additional_insured_info_btn = self.page.get_by_role("button", name="Additional Insured Information")
        self.loading_screen = self.page.locator(".jss53")


    def fill_cargo_insured_info(self, params: CargoInsuredInformationParams):
        
        self.insured_name_input.fill(params.business_insured_name)
        self.check_loading()
        self.insured_entity_select.select_option(params.type_of_entity)
        self.check_loading()
        self.insured_email_input.fill(params.email_address)
        self.check_loading()         
        self.inured_phone_input.fill(params.phone_number)
        self.check_loading()
        self.insured_street_address_1_input.fill(params.address_street1)
        self.check_loading()            
        self.insured_street_address_2_input.fill(params.address_street2)
        self.check_loading()
        self.insured_city_input.fill(params.address_city)
        self.check_loading()
        self.insured_state_select.select_option(params.address_state)
        self.check_loading()
        self.insured_zip_input.fill(params.address_zip)
        self.check_loading()
        self.insured_is_new_venture_selection.select_option(params.new_venture)
        self.check_loading()
        self.insured_icc_input.fill(params.insured_ICC_docket_number_MC)
        self.check_loading()
        self.insured_are_filling_selection.select_option("None")
        self.check_loading()
        if self.insured_all_owned_units_selection.is_visible():
            self.insured_all_owned_units_selection.select_option(params.include_all_owned_operated_units)
            self.check_loading()
        self.insured_carrier_type_selection.select_option(params.type_of_company_carrier)
        self.check_loading()
        # if self.insured_own_goods_selection.is_visible():
        #     self.insured_own_goods_selection.select_option(params.goo)
        #     self.check_loading()
        # self.insured_garage_same_selection.select_option
        self.check_loading()
        self.insured_garaging_address1_input.fill(params.garaging_address_street1)
        self.check_loading()
        self.insured_garaging_address2_input.fill(params.garaging_address_street2)
        self.check_loading()
        self.insured_garaging_city_input.fill(params.garaging_address_city)
        self.check_loading()
        self.insured_garaging_state_selection.select_option(params.garaging_address_state)
        self.check_loading()
        self.insured_garaging_zip_input.fill(params.garaging_address_zip)
        self.check_loading()
        self.insured_garaging_secondary_selection.select_option("no")
        self.check_loading()
        
        expect(self.additional_insured_info_btn).to_be_visible()
        expect(self.additional_insured_info_btn).to_be_enabled()
        self.additional_insured_info_btn.click()

    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")