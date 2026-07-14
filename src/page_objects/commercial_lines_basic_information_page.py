import re
from playwright.sync_api import Page, expect

class CommercialLinesBasicInformationPage:
    def __init__(self, page: Page):
        self.page = page
        self.commercial_lines_basic_information_heading = self.page.get_by_role("heading", name="    Commercial Lines")
        self.underwriter_select = self.page.locator("[id=\"basics.assignments.underwriter\"]")
        self.assistant_select = self.page.locator("[id=\"basics.assignments.assistant\"]")
        self.is_this_a_renewal_select = self.page.locator("[id=\"basics.renewal.is_renewal\"]")
        self.generate_new_application_select = self.page.locator("[id=\"basics.renewal.app_required\"]")
        self.agency_information_btn = self.page.get_by_role("button", name="Agency Information")
    
    def fill_commercial_line_basic_information_form(self):
        expect(self.commercial_lines_basic_information_heading).to_be_visible()
        self.underwriter_select.select_option("49") # Amy Nelson
        self.assistant_select.select_option("120") # Ashley O Neal
        self.is_this_a_renewal_select.select_option("no")
        self.generate_new_application_select.select_option("yes")
        expect(self.agency_information_btn).to_be_visible()
        expect(self.agency_information_btn).to_be_enabled()
        self.agency_information_btn.click()

