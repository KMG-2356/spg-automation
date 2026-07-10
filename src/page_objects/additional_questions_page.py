import re
from playwright.sync_api import Page, expect

class AdditionalQuestionPage:
    def __init__(self, page: Page):
        self.page = page
        self.addition_questions_btn = self.page.get_by_role("button", name="Wind / Hail Additional")
        self.additional_questions_input = self.page.locator("[id=\"wd.additional.additional_comments\"]")
        self.print_your_documents_button = self.page.get_by_role("button", name="Print Your Quote Documents")
        
    def fill_additional_comments(self,data):
        self.addition_questions_btn.click()
        self.additional_questions_input.fill(data["01_Policy_Info"][0]["Any Additional Comments"])
        self.print_your_documents_button.click()

