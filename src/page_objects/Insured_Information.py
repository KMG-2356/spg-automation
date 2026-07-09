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
        self.insured_ZipCode_input = self.page.locator(".MuiInputBase-root.MuiInput-root.MuiInput-underline.Mui-focused > .MuiInputBase-input")

    def fill_insured_information(self,data):
        self.insured_Name_input.fill("name")
        self.insured_email_input.fill("E-MAIL@ .E")
        self.insured_phone_input.fill("990")
        self.insured_StreetAddress1_input.fill("ADD11")
        self.insured_StreetAddress2_input.fill("ADD22")
        self.insured_City_input.fill("1CITY")
        self.insured_State_selection.select_option("LA")
        self.insured_ZipCode_input.fill("11ZIP")
