from playwright.sync_api import Page, expect, TimeoutError
from models.home_owners_additional_question_params import HomeOwnersAdditionalQuestionsParams

class HomeOwnersAdditionalQuestionsPage:
    def __init__(self, page: Page):
        self.page = page

        self.deadbolts_select = self.page.locator("[id=\"ho.additional.deadbolts\"]")
        self.central_fire_select = self.page.locator("[id=\"ho.additional.central_fire\"]")
        self.central_burglar_select = self.page.locator("[id=\"ho.additional.central_burglar\"]")
        self.deductible_select = self.page.locator("[id=\"ho.additional.deductible\"]")
        self.roof_valuation_endt_select = self.page.locator("[id=\"ho.additional.roof_valuation_endt\"]")
        self.loading_screen = self.page.locator(".jss53")

        self.additional_comments_input = self.page.locator("[id=\"ho.additional.additional_comments\"]")

        self.finance_quote_btn = self.page.get_by_role("button", name="Finance Quote")

    def fill_additional_info_and_submit(self, params: HomeOwnersAdditionalQuestionsParams):
   
        self.deadbolts_select.select_option(params.deadbolts)
        self.check_loading()
        self.central_fire_select.select_option(params.central_fire)
        self.check_loading()
        self.central_burglar_select.select_option(params.central_burglar)
        self.check_loading()

        self.deductible_select.select_option(str(params.deductible))
        self.check_loading()
        self.roof_valuation_endt_select.select_option(params.roof_valuation_endt)
        self.check_loading()

        self.additional_comments_input.fill(params.additional_comments)

        expect(self.finance_quote_btn).to_be_visible()
        expect(self.finance_quote_btn).to_be_enabled()
        self.finance_quote_btn.click()

    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")