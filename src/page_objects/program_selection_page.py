import re
from playwright.sync_api import Page, expect

class ProgramSelectionPage:
    def __init__(self, page: Page):
        self.page = page
        self.program_selection_heading = self.page.get_by_role("heading", name="#    Program Selection")
        self.personal_lines_LOB_btn = self.page.locator("div").filter(has_text=re.compile(r"^Personal Lines$")).first
        self.commercial_lines_LOB_btn = self.page.locator("div").filter(has_text=re.compile(r"^Commercial Lines$")).first
        self.monoline_wind_LOB_btn = self.page.locator("div").filter(has_text=re.compile(r"^Monoline Wind \(MD and VA Only\)$")).first
        self.commercial_lines_basic_information_btn = self.page.get_by_role("button", name="Commercial Lines Basic")
        self.personal_line_basic_information_btn = self.page.get_by_role("button", name="Personal Lines Basic")

    def select_monoline_wind_LOB(self):
        expect(self.program_selection_heading).to_be_visible()
        self.monoline_wind_LOB_btn.click()
        self.commercial_lines_basic_information_btn.click()

    def select_personal_lines_LOB(self):
        expect(self.program_selection_heading).to_be_visible()
        self.personal_lines_LOB_btn.click()
        expect(self.personal_line_basic_information_btn).to_be_visible()
        expect(self.personal_line_basic_information_btn).to_be_enabled()
        self.personal_line_basic_information_btn.click()



