import re
from playwright.sync_api import Page, expect, TimeoutError
from models.property_insured_params import InsuredInfoParams

class InsuredInformationPage:
    def __init__(self, page: Page):
        self.page = page
        self.insured_name_input = self.page.locator("[id=\"insured.name\"]")
        self.insured_email_input = self.page.locator("[id=\"insured.email\"]")
        self.insured_phone_input = self.page.locator("[id=\"insured.phone\"]")
        self.insured_street_address1_input = self.page.get_by_text("Street Address 1Street").locator("input").nth(0)
        self.insured_street_address2_input = self.page.get_by_text("Street Address 1Street").locator("input").nth(1)
        self.insured_city_input = self.page.get_by_text("Street Address 1Street").locator("input").nth(2)
        self.insured_zip_input = self.page.get_by_text("Street Address 1Street").locator("input").nth(3)
        self.insured_state_selection = self.page.get_by_text("Street Address 1Street").locator("select").nth(0)
        self.type_of_entity_selection = self.page.locator("[id=\"insured.entity\"]")      
        self.insured_information_heading = self.page.get_by_role("heading", name="    Insured")
        self.trustee_full_name = self.page.locator("[id=\"insured.trustee.name\"]")
        self.trustee_street_address1 = self.page.get_by_text("Street Address 1Street").locator("input").nth(8)
        self.trustee_street_address2 = self.page.get_by_text("Street Address 1Street").locator("input").nth(9)
        self.trustee_street_zip = self.page.locator("div:nth-child(2) > .jss94 > .jss97 > .MuiFormControl-root.MuiTextField-root.jss104 > .MuiInputBase-root > .MuiInputBase-input")
        self.trustee_city = self.page.get_by_text("Street Address 1Street").locator("input").nth(10)
        self.trustee_state = self.page.get_by_text("Street Address 1Street").locator("select").nth(2)  
        self.trustee_zip_input = self.page.get_by_text("Street Address 1Street").locator("input").nth(11)           
        self.is_the_mailing_address_different_from_the_street_address_select = self.page.get_by_text("Is Insured's physical address same as the mailing address?")
        self.physical_street_address1_input = self.page.get_by_text("Street Address 1Street").locator("input").nth(4)
        self.physical_street_address2_input = self.page.get_by_text("Street Address 1Street").locator("input").nth(5)
        self.physical_state_select = self.page.get_by_text("Street Address 1Street").locator("select").nth(1)
        self.physical_city_input = self.page.get_by_text("Street Address 1Street").locator("input").nth(6)
        self.physical_zip_input = self.page.get_by_text("Street Address 1Street").locator("input").nth(7)    
        self.location_btn = self.page.get_by_role("button", name="Location")
        self.loading_screen = self.page.locator(".jss53")
        
    

    def fill_insured_information_form(self, params: InsuredInfoParams):  
        self.type_of_entity_selection.select_option(params.type_of_entity)
        self.check_loading()
        print(params.type_of_entity)
        self.insured_name_input.fill(params.insured_full_name)
        self.insured_email_input.fill(params.insured_email)
        self.insured_phone_input.fill(params.insured_phone)
        self.insured_zip_input.fill(params.insured_address_zip)
        self.insured_street_address1_input.fill(params.insured_street1)
        self.insured_street_address2_input.fill(params.insured_street2) # temporariliy off not affecting premium
        self.insured_city_input.fill(params.insured_city)     
        self.insured_state_selection.select_option(params.insured_state)     
        self.check_loading()
        if params.mailing_address_different == "Yes":
           self.is_the_mailing_address_different_from_the_street_address_select.click()
           self.check_loading()
        
        if params.mailing_address_different == "No":
            self.physical_zip_input.fill(params.physical_zip)
            self.check_loading()
            self.physical_street_address1_input.fill(params.physical_street1)
            self.physical_street_address2_input.fill(params.physical_street2) # temporariliy off not affecting premium
            self.physical_city_input.fill(params.physical_city)
            self.physical_state_select.select_option(params.physical_state)
            self.check_loading()
        
        if self.trustee_full_name.is_visible():
            self.trustee_full_name.fill(params.trustee_full_name)                       
            self.trustee_street_address1.fill(params.trustee_street_address1)
            self.trustee_street_zip.fill(params.trustee_street_zip)
            self.check_loading() 
            self.trustee_street_address2.fill(params.trustee_street_address2)
            self.trustee_state.select_option(params.trustee_state)
            self.check_loading()
            self.trustee_city.fill(params.trustee_city)


        expect(self.location_btn).to_be_visible()
        expect(self.location_btn).to_be_enabled()
        self.location_btn.click()

    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")

