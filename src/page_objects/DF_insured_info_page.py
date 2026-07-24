from playwright.sync_api import Page, expect, TimeoutError
from models.DF_insured_info_params import DFinsuredInfoParams

class DFInsuredInformationPage:
    def __init__(self, page: Page):
        self.page = page
        self.insured_name_input = self.page.locator("[id=\"insured.name\"]")
        self.insured_entity_select = self.page.locator("[id=\"insured.entity\"]")
        self.insured_email_input = self.page.locator("[id=\"insured.email\"]")
        self.inured_phone_input = self.page.locator("[id=\"insured.phone\"]")
        self.insured_occupation_input = self.page.locator("[id=\"insured.occupation\"]")
        self.insured_employer_input = self.page.locator("[id=\"insured.employer\"]")
        self.insured_owner_dob_input = self.page.locator("[id=\"insured.owner_dob\"]")
        self.additional_resident_or_spouse_select = self.page.get_by_text("Is there an additional")
        self.insured_additional_name_input = self.page.locator("[id=\"insured.spouse_name\"]")
        self.insured_additional_dob_input = self.page.locator("[id=\"insured.spouse_dob\"]")
        self.insured_additional_occupation_input = self.page.locator("[id=\"insured.spouse_occupation\"]")
        self.insured_additional_employer_input = self.page.locator("[id=\"insured.spouse_employer\"]")
        self.insured_street_address_1_input = self.page.locator(".MuiInputBase-input.MuiInput-input").first
        self.insured_street_address_2_input = self.page.locator("div:nth-child(2) > .MuiInputBase-root > .MuiInputBase-input")
        self.insured_city_input = self.page.locator(".MuiFormControl-root.MuiTextField-root.jss170 > .MuiInputBase-root > .MuiInputBase-input")
        self.insured_state_select = self.page.get_by_role("combobox").nth(1)
        self.insured_zip_input = self.page.locator(".MuiFormControl-root.MuiTextField-root.jss172 > .MuiInputBase-root > .MuiInputBase-input")
        self.estate_manager_name_input = self.page.locator("[id=\"insured.estate_name\"]")
        self.estate_manager_dob_input = self.page.locator("[id=\"insured.estate_dob\"]")
        self.trustee_full_name = self.page.locator("[id=\"insured.trustee.name\"]")
        self.trustee_street_address1 = self.page.locator("div:nth-child(2) > .jss94 > .jss97 > div > .MuiInputBase-root > .MuiInputBase-input").first
        self.trustee_street_address2 = self.page.locator("div:nth-child(2) > .jss94 > .jss97 > div:nth-child(2) > .MuiInputBase-root > .MuiInputBase-input")
        self.trustee_street_zip = self.page.locator("div:nth-child(2) > .jss94 > .jss97 > .MuiFormControl-root.MuiTextField-root.jss104 > .MuiInputBase-root > .MuiInputBase-input")
        self.trustee_city = self.page.locator("div:nth-child(2) > .jss94 > .jss97 > .MuiFormControl-root.MuiTextField-root.jss102 > .MuiInputBase-root > .MuiInputBase-input")
        self.trustee_state = self.page.locator(".jss97").nth(1).locator("select")
        self.mailing_street_address1_input = self.page.locator("div", has_text="Mailing Address").locator(".MuiFormControl-root", has_text="Street Address 1").locator("input").nth(0)
        self.mailing_street_address2_input = self.page.locator("div", has_text="Mailing Address").locator(".MuiFormControl-root", has_text="Street Address 2").locator("input").nth(0)
        self.mailing_city_input = self.page.locator("div", has_text="Mailing Address").locator(".MuiFormControl-root", has_text="City").locator("input").nth(0)
        self.mailing_state_select = self.page.locator("div", has_text="Mailing Address").locator(".MuiFormControl-root", has_text="State").locator("select").nth(1)
        self.mailing_zip_input = self.page.locator("div", has_text="Mailing Address").locator(".MuiFormControl-root",has_text="Zip").locator("input").nth(0)
        self.insured_lives_out_of_state = self.page.locator("[id=\"insured.out_of_state\"]")
        self.DF_location_btn = self.page.get_by_role("button", name="Dwelling Fire Location")
        self.loading_screen = self.page.locator(".jss53")

    def fill_DF_insured_info(self, params: DFinsuredInfoParams):
        
        self.insured_name_input.fill(params.insured_full_name)
        self.check_loading()
        self.insured_entity_select.select_option(params.type_of_entity)
        self.check_loading()
        self.insured_email_input.fill(params.insured_email)
        self.check_loading()         
        self.inured_phone_input.fill(params.insured_phone)
        self.check_loading()
        self.insured_occupation_input.fill(params.insured_occupation)
        self.check_loading()            
        self.insured_employer_input.fill("N/A" if params.insured_employer in ["None", ""] else params.insured_employer)
        self.check_loading()
        self.insured_owner_dob_input.fill(params.insured_dob)
        self.check_loading()
        if params.additional_resident_or_spouse=="Yes":
            self.additional_resident_or_spouse_select.click()
            self.check_loading()
            self.insured_additional_name_input.fill(params.additional_resident_full_name)
            self.check_loading()
            self.insured_additional_dob_input.fill(params.additional_resident_dob)
            self.check_loading()
            self.insured_additional_occupation_input.fill(params.additional_resident_occupation)
            self.check_loading()
            print(params.addition_resident_employer)
            self.insured_additional_employer_input.fill("N/A" if params.addition_resident_employer in ["None", ""] else params.addition_resident_employer)
            self.check_loading()

        if self.estate_manager_name_input.is_visible():
            self.estate_manager_name_input.fill(params.estate_manager_name)
            self.estate_manager_dob_input.fill(params.estate_manager_dob)

        if self.trustee_full_name.is_visible():
            self.trustee_full_name.fill(params.trustee_full_name)
            self.trustee_street_address1.fill(params.trustee_street_address1)
            self.trustee_street_address2.fill(params.trustee_street_address2)
            self.trustee_street_zip.fill(params.trustee_street_zip)
            self.trustee_state.select_option(params.trustee_state)
            self.check_loading()
            self.trustee_city.fill(params.trustee_city)

        self.mailing_zip_input.fill(params.insured_address_zip)
        self.check_loading()
        self.mailing_street_address1_input.fill(params.insured_address_street1)
        self.check_loading()
        self.mailing_street_address2_input.fill(params.insured_address_street2)
        self.check_loading()
        self.mailing_city_input.fill(params.insured_address_city)
        self.check_loading()
        self.mailing_state_select.select_option(params.insured_address_state)
        self.check_loading()
        self.insured_lives_out_of_state.select_option("No")



        expect(self.DF_location_btn).to_be_visible()
        expect(self.DF_location_btn).to_be_enabled()
        self.DF_location_btn.click()

    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")

    
