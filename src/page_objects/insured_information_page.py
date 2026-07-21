import re
from playwright.sync_api import Page, expect, TimeoutError
from models.insured_info_params import InsuredInfoParams

class InsuredInformationPage:
    def __init__(self, page: Page):
        self.page = page
        self.insured_name_input = self.page.locator("[id=\"insured.name\"]")
        self.insured_email_input = self.page.locator("[id=\"insured.email\"]")
        self.insured_phone_input = self.page.locator("[id=\"insured.phone\"]")
        self.insured_dob_input = self.page.locator("[id=\"insured.owner_dob\"]")
        self.insured_street_address1_input = self.page.locator(".MuiInputBase-input.MuiInput-input").first
        self.insured_street_address2_input = self.page.locator("div:nth-child(2) > .MuiInputBase-root > .MuiInputBase-input").first
        self.insured_city_input = self.page.locator("div", has_text="Street Address of Residence to be insured").locator(".MuiFormControl-root", has_text="City").locator("input").first
        self.insured_state_selection = self.page.locator("div").filter(has_text="State").locator("select").nth(1)
        self.insured_occupation_input = self.page.locator("[id=\"insured.occupation\"]")
        self.insured_employer_input = self.page.locator("[id=\"insured.employer\"]")
        self.coverage_street_address1_input = self.page.locator("div", has_text="Coverage Address").locator(".MuiFormControl-root", has_text="Street Address 1").locator("input").nth(1)
        self.coverage_street_address2_input = self.page.locator("div", has_text="Coverage Address").locator(".MuiFormControl-root", has_text="Street Address 2").locator("input").nth(1)
        self.coverage_city_input = self.page.locator("div", has_text="Coverage Address").locator(".MuiFormControl-root", has_text="city").locator("input").nth(1)
        self.coverage_zip_input = self.page.locator("div", has_text="Coverage Address").locator(".MuiFormControl-root", has_text="zip").locator("input").nth(1)
        self.coverage_state_select = self.page.locator("div", has_text="Coverage Address").locator(".MuiFormControl-root", has_text="state").locator("select").nth(2)
        self.type_of_entity_selection = self.page.locator("[id=\"insured.entity\"]")
        self.estate_manager_name_input = self.page.locator("[id=\"insured.estate_name\"]")
        self.estate_manager_dob_input = self.page.locator("[id=\"insured.estate_dob\"]")
        self.insured_zip_code_input = self.page.locator("div", has_text="Street Address of Residence to be insured").locator(".MuiFormControl-root", has_text="Zip").locator("input").first
        self.location_information_btn = self.page.get_by_role("button", name="Monoline Wind Location")
        self.insured_information_heading = self.page.get_by_role("heading", name="    Insured")
        self.trustee_full_name = self.page.locator("[id=\"insured.trustee.name\"]")
        self.trustee_street_address1 = self.page.locator("div:nth-child(2) > .jss94 > .jss97 > div > .MuiInputBase-root > .MuiInputBase-input").first
        self.trustee_street_address2 = self.page.locator("div:nth-child(2) > .jss94 > .jss97 > div:nth-child(2) > .MuiInputBase-root > .MuiInputBase-input")
        self.trustee_street_zip = self.page.locator("div:nth-child(2) > .jss94 > .jss97 > .MuiFormControl-root.MuiTextField-root.jss104 > .MuiInputBase-root > .MuiInputBase-input")
        self.trustee_city = self.page.locator("div:nth-child(2) > .jss94 > .jss97 > .MuiFormControl-root.MuiTextField-root.jss102 > .MuiInputBase-root > .MuiInputBase-input")
        self.trustee_state = self.page.get_by_role("combobox").nth(2)
        self.IM_trustee_state_select = self.page.locator("div", has_text="Trustee Info").locator(".MuiFormControl-root", has_text="state").locator("select").nth(3)
        self.IM_trustee_city_input = self.page.locator("div", has_text="Trustee Info").locator(".MuiFormControl-root", has_text="city").locator("input").nth(2)
        self.is_there_an_additional_resident_or_spouse_checkbox = self.page.get_by_text("Is there an additional")
        self.additional_resident_full_name_input = self.page.locator("[id=\"insured.spouse_name\"]")
        self.additional_resident_dob_input = self.page.locator("[id=\"insured.spouse_dob\"]")
        self.additional_resident_occupation_input = self.page.locator("[id=\"insured.spouse_occupation\"]")
        self.additional_resident_employer_input = self.page.locator("[id=\"insured.spouse_employer\"]")
        self.is_the_mailing_address_different_from_the_street_address_select = self.page.locator("[id=\"insured.diff_address\"]")
        self.mailing_street_address1_input = self.page.locator("div", has_text="Mailing Address").locator(".MuiFormControl-root", has_text="Street Address 1").locator("input").nth(1)
        self.mailing_street_address2_input = self.page.locator(".MuiInputBase-root.MuiInput-root.MuiInput-underline.MuiInputBase-fullWidth.MuiInput-fullWidth.Mui-focused > .MuiInputBase-input")
        self.mailing_city_input = self.page.locator("div", has_text="Mailing Address").locator(".MuiFormControl-root", has_text="City").locator("input").nth(1)
        self.mailing_state_select = self.page.get_by_role("combobox").nth(3)
        self.mailing_zip_input = self.page.locator("div", has_text="Street Address of Residence to be insured").locator(".MuiFormControl-root", has_text="Zip").locator("input").nth(1)
        self.IM_mailing_zip_input = self.page.locator("div", has_text="Mailing Address").locator(".MuiFormControl-root", has_text="Zip").locator("input").nth(0)
        self.IM_mailing_city_input = self.page.locator("div", has_text="Mailing Address").locator(".MuiFormControl-root", has_text="City").locator("input").nth(0)
        self.IM_mailing_state_select = self.page.locator("div", has_text="Mailing Address").locator(".MuiFormControl-root", has_text="State").locator("select").nth(1)
        self.IM_mailing_street_address1_input = self.page.locator("div", has_text="Mailing Address").locator(".MuiFormControl-root", has_text="Street Address 1").locator("input").nth(0)
        self.home_owners_dwelling_information_btn = self.page.get_by_role("button", name="Homeowners Dwelling")
        self.inland_marine_btn = self.page.get_by_role("button", name="Inland Marine")
        self.loading_screen = self.page.locator(".jss53")
        
    def fill_insured_information_form(self,data):
        expect(self.insured_information_heading).to_be_visible()
        self.insured_name_input.fill(data["01_Policy_Info"][0]["Insured Full Name"])
        self.insured_email_input.fill(data["01_Policy_Info"][0]["Email Address"])
        self.insured_phone_input.fill(str(data["01_Policy_Info"][0]["Phone Number"]))
        self.insured_street_address1_input.fill(data["01_Policy_Info"][0]["Mailing Street 1"])
        self.insured_street_address2_input.fill(data["01_Policy_Info"][0]["Mailing Street 2"])
        self.insured_zip_code_input.fill(str(data["01_Policy_Info"][0]["Mailing Zip"]))
        self.insured_city_input.fill(data["01_Policy_Info"][0]["Mailing City"])
        self.insured_state_selection.select_option(data["01_Policy_Info"][0]["Mailing State"])
        self.type_of_entity_selection.select_option(data["01_Policy_Info"][0]["Type of Entity"])
        self.check_loading()
        if self.trustee_full_name.is_visible():
            self.trustee_full_name.fill("Megan Carter")
            self.trustee_street_address1.fill("1200 W Broad St")
            self.trustee_street_address2.fill("Suite 410")
            self.trustee_street_zip.fill("85004")
            self.trustee_state.select_option("AZ")
            self.trustee_city.fill("Phoenix")
        expect(self.location_information_btn).to_be_visible()
        expect(self.location_information_btn).to_be_enabled()
        self.location_information_btn.click()


    def fill_insured_information_form_for_ho(self, data: InsuredInfoParams):  
        self.type_of_entity_selection.select_option(data.type_of_entity)
        self.check_loading()
        self.insured_name_input.fill(data.insured_full_name)
        self.insured_occupation_input.fill(data.insured_occupation)
        self.insured_employer_input.fill(data.insured_employer)
        self.insured_email_input.fill(data.insured_email)
        self.insured_phone_input.fill(data.insured_phone)
        self.insured_dob_input.fill(data.insured_dob)
        self.insured_zip_code_input.fill(data.insured_address_zip) 
        self.check_loading 
        self.insured_street_address1_input.fill(data.insured_street1)
        # self.insured_street_address2_input.fill(data.insured_street2) # temporariliy off not affecting premium
        self.insured_city_input.fill(data.insured_city)     
        self.insured_state_selection.select_option(data.insured_state)     
        self.check_loading()

        if self.estate_manager_name_input.is_visible():
            self.estate_manager_name_input.fill("John Doe")
            self.estate_manager_dob_input.fill("08-08-1996")

        if data.additional_resident_or_spouse == "yes":
            self.is_there_an_additional_resident_or_spouse_checkbox.click()
            self.check_loading()
        if self.additional_resident_full_name_input.is_visible():
            self.additional_resident_full_name_input.fill(data.additional_resident_full_name)
            self.additional_resident_occupation_input.fill(data.additional_resident_occupation)
            self.additional_resident_dob_input.fill(data.additional_resident_dob)
            self.additional_resident_employer_input.fill(data.additional_resident_employer)

        self.is_the_mailing_address_different_from_the_street_address_select.select_option(
            data.mailing_address_different
        )
        self.check_loading()
        
        if data.mailing_address_different == "Yes":
            self.mailing_zip_input.fill(data.diff_mailing_zip)
            self.check_loading()
            self.mailing_street_address1_input.fill(data.diff_mailing_street1)
            # self.mailing_street_address2_input.fill(data.diff_mailing_street2) # temporariliy off not affecting premium
            self.mailing_city_input.fill(data.diff_mailing_city)
            self.mailing_state_select.select_option(data.diff_mailing_state)
            self.check_loading()
        
        if self.trustee_full_name.is_visible():
            self.trustee_full_name.fill(data.trustee_full_name)
            self.trustee_street_address1.fill(data.trustee_street_address1)
            self.trustee_street_address2.fill(data.trustee_street_address2)
            self.trustee_street_zip.fill(data.trustee_street_zip)
            # self.trustee_state.select_option(data.trustee_state)
            self.check_loading()
            # self.trustee_city.fill(data.trustee_city)

        
        expect(self.home_owners_dwelling_information_btn).to_be_visible()
        expect(self.home_owners_dwelling_information_btn).to_be_enabled()
        self.home_owners_dwelling_information_btn.click()


    def fill_insured_information_form_for_IM(self, data: InsuredInfoParams):
        self.type_of_entity_selection.select_option(data.type_of_entity)
        self.check_loading()
        self.insured_name_input.fill(data.insured_full_name)
        self.insured_email_input.fill(data.insured_email)
        self.insured_phone_input.fill(data.insured_phone)

        if data.mailing_address_different == "No":
            self.IM_mailing_zip_input.fill(data.coverage_zip) 
            self.check_loading 
            self.IM_mailing_street_address1_input.fill(data.coverage_street_address1)
            self.check_loading()
            self.IM_mailing_state_select.select_option(data.coverage_state)
            self.check_loading()
            self.IM_mailing_city_input.fill(data.coverage_city)
        else:
            self.IM_mailing_zip_input.fill(data.mailing_zip) 
            self.check_loading 
            self.IM_mailing_street_address1_input.fill(data.mailing_street1)
            self.check_loading()
            self.IM_mailing_state_select.select_option(data.mailing_state)
            self.check_loading()
            self.IM_mailing_city_input.fill(data.mailing_city)

        self.coverage_street_address1_input.fill(data.coverage_street_address1)
        self.coverage_street_address2_input.fill(data.coverage_street_address2)
        self.coverage_zip_input.fill(data.coverage_zip)
        self.check_loading()
        self.coverage_city_input.fill(data.coverage_city)
        self.coverage_state_select.select_option(data.coverage_state)
        self.check_loading()

        if self.trustee_full_name.is_visible():
            self.trustee_full_name.fill(data.trustee_full_name)
            self.trustee_street_address1.fill(data.trustee_street_address1)
            self.trustee_street_address2.fill(data.trustee_street_address2)
            self.trustee_street_zip.fill(data.trustee_street_zip)
            self.IM_trustee_state_select.select_option(data.trustee_state)
            self.check_loading()
            self.IM_trustee_city_input.fill(data.trustee_city)

        expect(self.inland_marine_btn).to_be_visible()
        expect(self.inland_marine_btn).to_be_enabled()
        self.inland_marine_btn.click()

    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")

