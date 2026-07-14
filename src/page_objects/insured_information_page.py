import re
from playwright.sync_api import Page, expect

class InsuredInformationPage:
    def __init__(self, page: Page):
        self.page = page
        self.insured_name_input = self.page.locator("[id=\"insured.name\"]")
        self.insured_email_input = self.page.locator("[id=\"insured.email\"]")
        self.insured_phone_input = self.page.locator("[id=\"insured.phone\"]")
        self.insured_street_address1_input = self.page.get_by_role("textbox").nth(3)
        self.insured_street_address2_input = self.page.get_by_role("textbox").nth(4)
        self.insured_city_input = self.page.get_by_role("textbox").nth(5)
        self.insured_state_selection = self.page.get_by_role("combobox").nth(1)
        self.type_of_entity_selection = self.page.locator("[id=\"insured.entity\"]")
        self.insured_zip_code_input = self.page.locator('div:has(> p:text("Zip")) input')
        self.location_information_btn = self.page.get_by_role("button", name="Monoline Wind Location")
        self.insured_information_heading = self.page.get_by_role("heading", name="    Insured")
        self.trustee_full_name = self.page.locator("[id=\"insured.trustee.name\"]")
        self.trustee_street_address1 = self.page.locator("div:nth-child(2) > .jss94 > .jss97 > div > .MuiInputBase-root > .MuiInputBase-input").first
        self.trustee_street_address2 = self.page.locator("div:nth-child(2) > .jss94 > .jss97 > div:nth-child(2) > .MuiInputBase-root > .MuiInputBase-input")
        self.trustee_street_zip = self.page.locator("div:nth-child(2) > .jss94 > .jss97 > .MuiFormControl-root.MuiTextField-root.jss104 > .MuiInputBase-root > .MuiInputBase-input")
        self.trustee_city = self.page.locator("div:nth-child(2) > .jss94 > .jss97 > .MuiFormControl-root.MuiTextField-root.jss102 > .MuiInputBase-root > .MuiInputBase-input")
        self.trustee_state = self.page.get_by_role("combobox").nth(2)
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

    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")

