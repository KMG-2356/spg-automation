import re
from playwright.sync_api import Page, expect

class InsuredInformationPage:
    def __init__(self, page: Page):
        self.page = page
        self.insured_name_input = self.page.locator("[id=\"insured.name\"]")
        self.insured_email_input = self.page.locator("[id=\"insured.email\"]")
        self.insured_phone_input = self.page.locator("[id=\"insured.phone\"]")
        self.insured_StreetAddress1_input = self.page.get_by_role("textbox").nth(3)
        self.insured_StreetAddress2_input = self.page.get_by_role("textbox").nth(4)
        self.insured_City_input = self.page.get_by_role("textbox").nth(5)
        self.insured_State_selection = self.page.get_by_role("combobox").nth(1)
        self.type_of_entity_selection = self.page.locator("[id=\"insured.entity\"]")
        # self.insured_ZipCode_input = self.page.locator(".MuiInputBase-root.MuiInput-root.MuiInput-underline.Mui-focused > .MuiInputBase-input")
        self.insured_ZipCode_input = self.page.locator(".MuiFormControl-root.MuiTextField-root.jss104 > .MuiInputBase-root > .MuiInputBase-input")
        self.location_information_btn = self.page.get_by_role("button", name="Monoline Wind Location")
    def fill_insured_information(self,data):
        self.insured_name_input.fill(data["01_Policy_Info"][0]["Insured Full Name"])
        self.insured_email_input.fill(data["01_Policy_Info"][0]["Email Address"])
        self.insured_phone_input.fill(str(data["01_Policy_Info"][0]["Phone Number"]))
        self.insured_StreetAddress1_input.fill(data["01_Policy_Info"][0]["Mailing Street 1"])
        self.insured_StreetAddress2_input.fill(data["01_Policy_Info"][0]["Mailing Street 2"])
        self.insured_City_input.fill(data["01_Policy_Info"][0]["Mailing City"])
        self.insured_State_selection.select_option(data["01_Policy_Info"][0]["Mailing State"])
        self.type_of_entity_selection.select_option(data["01_Policy_Info"][0]["Type of Entity"])
        self.insured_ZipCode_input.fill(str(data["01_Policy_Info"][0]["Mailing Zip"]))
        self.page.wait_for_timeout(5000)
        self.location_information_btn.click()
        self.page.wait_for_timeout(5000)

