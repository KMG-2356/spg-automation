import re
from playwright.sync_api import Page, expect

class CommercialLinesBasicInformationPage:
    def __init__(self, page: Page):
        self.page = page
        self.commercial_lines_basic_information_heading = self.page.get_by_role("heading", name="    Commercial Lines")
        self.agency_information_btn = self.page.get_by_role("button", name="Agency Information")
    
    def click_agency_information_button(self):
        expect(self.commercial_lines_basic_information_heading).to_be_visible()
        expect(self.agency_information_btn).to_be_visible()
        expect(self.agency_information_btn).to_be_enabled()
        self.agency_information_btn.click()
        self.page.pause()


