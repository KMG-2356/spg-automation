import re
from playwright.sync_api import Page, expect

from utils.helpers import get_num, write_excel_cell

class ProgramSelectionPage:
    def __init__(self, page: Page):
        self.page = page
        self.program_selection_heading = self.page.get_by_role("heading", name="#    Program Selection")
        self.personal_lines_LOB_btn = self.page.locator("div").filter(has_text=re.compile(r"^Personal Lines$")).first
        self.commercial_lines_LOB_btn = self.page.locator("div").filter(has_text=re.compile(r"^Commercial Lines$")).first
        self.monoline_wind_LOB_btn = self.page.locator("div").filter(has_text=re.compile(r"^Monoline Wind \(MD and VA Only\)$")).first
        self.commercial_lines_basic_information_btn = self.page.get_by_role("button", name="Commercial Lines Basic")
        self.personal_line_basic_information_btn = self.page.get_by_role("button", name="Personal Lines Basic")
        self.quote_number_text = self.page.locator("span.jss44")


    def select_monoline_wind_LOB(self):
        expect(self.program_selection_heading).to_be_visible()
        self.monoline_wind_LOB_btn.click()
        self.commercial_lines_basic_information_btn.click()
    def select_commercial_lines_LOB(self):
        expect(self.program_selection_heading).to_be_visible()
        self.commercial_lines_LOB_btn.click()
        expect(self.commercial_lines_basic_information_btn).to_be_visible()
        expect(self.commercial_lines_basic_information_btn).to_be_enabled()
        self.commercial_lines_basic_information_btn.click()
    def select_personal_lines_LOB(self):
        expect(self.program_selection_heading).to_be_visible()
        self.personal_lines_LOB_btn.click()
        expect(self.personal_line_basic_information_btn).to_be_visible()
        expect(self.personal_line_basic_information_btn).to_be_enabled()
        self.personal_line_basic_information_btn.click()
    def save_quote_number(self, output_filename, sheet_name, data):
        quote_number = get_num(self.quote_number_text.inner_text())
        write_excel_cell(f"src/data/output/{output_filename}.xlsx", "Output", row_value=data[sheet_name][0]["Test ID"], column_name="Quote Number", data=quote_number)




