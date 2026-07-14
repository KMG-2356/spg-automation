import re
from playwright.sync_api import Page, expect

class AdditionalQuestionPage:
    def __init__(self, page: Page):
        self.page = page
        self.addition_questions_btn = self.page.get_by_role("button", name="Wind / Hail Additional")
        self.additional_questions_input = self.page.locator("[id=\"wd.additional.additional_comments\"]")
        self.finance_quote_btn = self.page.get_by_role("button", name="Finance Quote")
        self.additional_questions_heading = self.page.get_by_role("heading", name="    Wind / Hail")
        
    def fill_additional_comments(self,data):
        expect(self.addition_questions_btn).to_be_visible()
        expect(self.addition_questions_btn).to_be_enabled()
        self.addition_questions_btn.click()
        expect(self.additional_questions_heading).to_be_visible()
        self.additional_questions_input.fill(data["01_Policy_Info"][0]["Any Additional Comments"])
        expect(self.finance_quote_btn).to_be_visible()
        expect(self.finance_quote_btn).to_be_enabled()
        self.finance_quote_btn.click()
