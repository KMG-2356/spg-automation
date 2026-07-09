import re
from playwright.sync_api import Page, expect

class AgencyInformationPage:
    def __init__(self, page: Page):
        self.page = page
        self.agency_information_heading = self.page.get_by_role("heading", name="    Agency Information")
        self.agency_name_input = self.page.get_by_role("textbox").first
        self.agency_id_code_input = self.page.get_by_role("textbox").nth(1)
        self.agency_full_name_input = self.page.get_by_role("textbox").nth(2)
        self.email_input = self.page.get_by_role("textbox").nth(3)
        self.phone_number_input = self.page.get_by_role("textbox").nth(4)
        self.fax_number_input = self.page.get_by_role("textbox").nth(5)
        self.agent_commission_select = self.page.get_by_role("combobox").nth(1)
        self.street_address1_input = self.page.locator(".MuiInputBase-input.MuiInput-input").first
        self.street_address2_input = self.page.locator("div:nth-child(2) > .MuiInputBase-root > .MuiInputBase-input")
        self.city_input = self.page.locator(".MuiFormControl-root.MuiTextField-root.jss102 > .MuiInputBase-root > .MuiInputBase-input")
        self.state_select = self.page.get_by_role("combobox").first
        self.zip_code_input = self.page.locator(".MuiFormControl-root.MuiTextField-root.jss104 > .MuiInputBase-root > .MuiInputBase-input")
        self.insured_information_btn = self.page.get_by_role("button", name="Insured Information")


    def fill_agency_information_form(self):
        expect(self.agency_information_heading).to_be_visible()
        # Fill in the form fields here
        # Example:
        # self.page.fill('input[name="agency_name"]', "Test Agency")
        # self.page.fill('input[name="agency_address"]', "123 Test St")
        # self.page.fill('input[name="agency_city"]', "Test City")
        # self.page.fill('input[name="agency_state"]', "TS")
        # self.page.fill('input[name="agency_zip"]', "12345")
  


