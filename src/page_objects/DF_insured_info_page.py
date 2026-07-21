from playwright.sync_api import Page, expect, TimeoutError
from models.DF_insured_info_params import DFinsuredInfoParams

class DFInsuredInformationPage:
    def __init__(self, page: Page):
        self.page = page
        self.insured_name_input = self.page.locator("[id=\"df.coverages.df_limit_of_liability\"]")
        self.insured_entity_select = self.page.locator("[id=\"insured.entity\"]")
        self.insured_email_input = self.page.locator("[id=\"insured.email\"]")
        self.inured_phone_input = self.page.locator("[id=\"insured.phone\"]")
        self.insured_occupation_input = self.page.locator("[id=\"insured.occupation\"]")
        self.insured_employer_input = self.page.locator("[id=\"insured.employer\"]")
        self.insured_owner_dob_input = self.page.locator("[id=\"insured.owner_dob\"]")
        self.additional_resident_or_spouse_select = self.page.locator(".MuiSvgIcon-root.MuiSvgIcon-colorAction")
        self.insured_additional_name_input = self.page.locator("[id=\"insured.spouse_name\"]")
        self.insured_additional_dob_input = self.page.locator("[id=\"insured.spouse_dob\"]")
        self.insured_additional_occupation_input = self.page.locator("[id=\"insured.spouse_occupation\"]")
        self.insured_additional_employer_input = self.page.locator("[id=\"insured.spouse_employer\"]")
        self.insured_street_address_1_input = self.page.locator(".MuiInputBase-input.MuiInput-input").first
        self.insured_street_address_2_input = self.page.locator("div:nth-child(2) > .MuiInputBase-root > .MuiInputBase-input")
        self.insured_city_input = self.page.locator(".MuiFormControl-root.MuiTextField-root.jss170 > .MuiInputBase-root > .MuiInputBase-input")
        self.insured_state_select = self.page.get_by_role("combobox").nth(1)
        self.insured_zip_input = self.page.locator(".MuiFormControl-root.MuiTextField-root.jss172 > .MuiInputBase-root > .MuiInputBase-input")
        self.insured_lives_out_of_state = self.page.locator("[id=\"insured.out_of_state\"]")
        self.DF_location_btn = self.page.get_by_role("button", name="Dwelling Fire Location")

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
        self.insured_employer_input.fill(params.insured_employer)
        self.check_loading()
        self.insured_owner_dob_input.fill(params.insured_dob)
        self.check_loading()
        if params.additional_resident_or_spouse=="Yes":
            self.additional_resident_or_spouse_select.select_option(params.additional_resident_or_spouse)
            self.check_loading()
            self.insured_additional_name_input.fill(params.additional_resident_full_name)
            self.check_loading()
            self.insured_additional_dob_input.fill(params.additional_resident_dob)
            self.check_loading()
            self.insured_additional_occupation_input.fill(params.additional_resident_occupation)
            self.check_loading()
            self.insured_additional_employer_input.fill(params.addition_resident_employer)
            self.check_loading()
        self.insured_street_address_1_input.fill(params.insured_address_street_1)
        self.check_loading()
        self.insured_street_address_2_input.fill(params.insured_address_street_2)
        self.check_loading()
        self.insured_city_input.fill(params.insured_address_city)
        self.check_loading()
        self.insured_state_select.select_option(params.insured_address_state)
        self.check_loading()
        self.insured_zip_input.fill(params.insured_address_zip)
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

    
