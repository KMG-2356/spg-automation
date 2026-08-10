import re
from typing import Dict
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

        self.new_venture_select = self.page.locator('[id="insured.new_venture"]')
        self.insured_icc_input = self.page.locator('[id="insured.insured_icc"]')
        self.filings_select = self.page.locator('[id="insured.filings"]')
        self.all_owned_units_select = self.page.locator('[id="insured.all_owned_units"]')
        self.carrier_type_select = self.page.locator('[id="insured.carrier_type"]')
        self.own_goods_select = self.page.locator('[id="insured.own_goods"]')
        self.garage_same_select = self.page.locator('[id="insured.garage_same"]')
        self.carrier_details_input = self.page.locator('[id="insured.carrier_details"]')

        self.primary_garaging_street1_input = self.page.locator(".MuiGrid-item").filter(has_text="Primary Garaging Address").nth(7).locator("input").nth(0)
        self.primary_garaging_street2_input = self.page.locator(".MuiGrid-item").filter(has_text="Primary Garaging Address").nth(7).locator("input").nth(1)
        self.primary_garaging_city_input = self.page.locator(".MuiGrid-item").filter(has_text="Primary Garaging Address").nth(7).locator("input").nth(2)
        self.primary_garaging_state_select = self.page.locator(".MuiGrid-item").filter(has_text="Primary Garaging Address").nth(7).locator("select").nth(0)
        self.primary_garaging_zip_input = self.page.locator(".MuiGrid-item").filter(has_text="Primary Garaging Address").nth(7).locator("input").nth(3)

        self.has_secondary_garage_select = self.page.locator("[id=\"insured.secondary_garaging\"]")

        self.secondary_garage_street1_input = self.page.locator(".MuiGrid-container").filter(has_text="Secondary Garaging Address").nth(-1).locator("input").nth(0)
        self.secondary_garage_street2_input = self.page.locator(".MuiGrid-container").filter(has_text="Secondary Garaging Address").nth(-1).locator("input").nth(1)
        self.secondary_garage_city_input = self.page.locator(".MuiGrid-container").filter(has_text="Secondary Garaging Address").nth(-1).locator("input").nth(2)
        self.secondary_garage_zip_input = self.page.locator(".MuiGrid-container").filter(has_text="Secondary Garaging Address").nth(-1).locator("input").nth(3)
        self.secondary_garage_state_select = self.page.locator(".MuiGrid-container").filter(has_text="Secondary Garaging Address").nth(-1).locator("select").nth(0)

        self.add_another_garaging_address_btn = self.page.get_by_role("button", name="Add Another Garaging Address")

        self.trustee_name_input = self.page.locator('[id="insured.trustee.name"]')
        self.trustee_street1_input = self.page.locator(".MuiGrid-container").filter(has=self.page.locator("[id=\"insured.trustee.name\"]")).nth(5).locator("input").nth(1)
        self.trustee_street2_input = self.page.locator(".MuiGrid-container").filter(has=self.page.locator("[id=\"insured.trustee.name\"]")).nth(5).locator("input").nth(2)
        self.trustee_city_input = self.page.locator(".MuiGrid-container").filter(has=self.page.locator("[id=\"insured.trustee.name\"]")).nth(5).locator("input").nth(3)
        self.trustee_state_select = self.page.locator(".MuiGrid-container").filter(has=self.page.locator("[id=\"insured.trustee.name\"]")).nth(5).locator("select").nth(0)
        self.trustee_zip_input = self.page.locator(".MuiGrid-container").filter(has=self.page.locator("[id=\"insured.trustee.name\"]")).nth(5).locator("input").nth(4)

        self.addition_insured_info_btn = self.page.get_by_role("button", name="Additional Insured Information")

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

    def fill_insured_information_cargo_additional_form(self, params: InsuredInfoParams):  
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


        self.new_venture_select.select_option(params.new_venture)
        self.check_loading()

        self.insured_icc_input.fill(params.insured_icc)

        self.filings_select.select_option(params.filings)
        self.check_loading()

        if self.all_owned_units_select.is_visible():
            self.all_owned_units_select.select_option(params.all_owned_units)
            self.check_loading()

        self.carrier_type_select.select_option(params.carrier_type)
        self.check_loading()

        if self.own_goods_select.is_visible():
            self.own_goods_select.select_option(params.own_goods)
            self.check_loading()

        self.garage_same_select.select_option(params.garage_same)
        self.check_loading()

        if self.carrier_details_input.is_visible():
            self.carrier_details_input.fill(params.carrier_details)

        if params.garage_same == "No":
            self.primary_garaging_street1_input.fill(params.primary_garaging_street1)
            self.primary_garaging_street2_input.fill(params.primary_garaging_street2)
            self.primary_garaging_zip_input.fill(params.primary_garaging_zip)
            self.check_loading()
            self.primary_garaging_city_input.fill(params.primary_garaging_city)
            self.primary_garaging_state_select.select_option(
                params.primary_garaging_state
            )

        if self.has_secondary_garage_select.is_visible():
            self.has_secondary_garage_select.select_option(params.has_secondary_garage)
            self.check_loading()

        if params.has_secondary_garage == "Yes":
            for i, garage in enumerate(params.secondary_garages):
                if i > 0:
                    self.add_another_garaging_address_btn.click()
                    self.check_loading()
                address = self.parse_us_address(garage)
                self.secondary_garage_street1_input.fill(address["street_address"])
                self.secondary_garage_zip_input.fill(address["zip_code"])
                self.check_loading()
                self.secondary_garage_city_input.fill(address["city"])
                self.secondary_garage_state_select.select_option(address["state"])

        if self.trustee_name_input.is_visible():
            self.trustee_name_input.fill(params.trustee_name)
            self.trustee_street1_input.fill(params.trustee_street1)
            self.trustee_street2_input.fill(params.trustee_street2)
            self.trustee_zip_input.fill(params.trustee_zip)
            self.check_loading()
            self.trustee_city_input.fill(params.trustee_city)
            self.trustee_state_select.select_option(params.trustee_state)

        expect(self.addition_insured_info_btn).to_be_visible()
        expect(self.addition_insured_info_btn).to_be_enabled()
        self.addition_insured_info_btn.click()


    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")


    def parse_us_address(self, address_str: str) -> Dict[str, str]:
        if not address_str or not isinstance(address_str, str):
            raise ValueError("Invalid Address")
        pattern = r"^(?P<street>.*?),\s*(?P<city>[^,]+),\s*(?P<state>[A-Za-z]{2})\s+(?P<zip>\d{5}(?:-\d{4})?)$"

        match = re.match(pattern, address_str.strip())

        if match:
            data = match.groupdict()
            return {
                "street_address": data["street"].strip(),
                "city": data["city"].strip(),
                "state": data["state"].upper(),
                "zip_code": data["zip"].strip(),
            }
        raise ValueError("Invalid Address")

