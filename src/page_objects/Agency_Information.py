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
        self.agency_name_input.fill("")
        self.agency_id_code_input.fill("")
        self.agency_full_name_input.fill("")
        self.email_input.fill("")
        self.phone_number_input.fill("")
        self.fax_number_input.fill("")
        self.agent_commission_select.select_option("18.00")
        self.street_address1_input.fill("")
        self.street_address2_input.fill("")
        self.city_input.fill("")
        self.state_select.select_option("")
        self.zip_code_input.fill("")
 
        # self.page.fill('input[name="agency_zip"]', "12345")
  