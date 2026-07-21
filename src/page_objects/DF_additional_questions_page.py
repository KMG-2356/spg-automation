from playwright.sync_api import Page, expect, TimeoutError
from models.DF_additional_questions_params import DFadditionalQuestionsParams

class DFAdditionalQusetionsPage:
    def __init__(self, page: Page):
        self.page = page
        self.HigherDeductibleAOP_select = self.page.locator("[id=\"df.additional.df_deductible\"]")
        self.CentralStationAlarms_select = self.page.locator("[id=\"df.additional.df_central_alarms\"]")
        self.RoofValuationEndorsement_select = self.page.locator("[id=\"df.additional.df_roof_valuation_endt\"]")
        self.additional_comments_input = self.page.locator("[id=\"df.additional.df_additional_comments\"]")
        self.DF_finance_quote_btn = self.page.get_by_role("button", name="Finance Quote")


    def fill_DF_additional_questions_info(self, params: DFadditionalQuestionsParams):
        
        self.HigherDeductibleAOP_select.select_option(params.HigherDeductibleAOP)
        self.check_loading()
        self.CentralStationAlarms_select.select_option(params.CentralStationAlarms)
        self.check_loading()
        self.RoofValuationEndorsement_select.select_option(params.RoofValuationEndorsement)
        self.check_loading()
        self.additional_comments_input.fill(params.AdditionalComments)
        self.check_loading()

        expect(self.DF_finance_quote_btn).to_be_visible()
        expect(self.DF_finance_quote_btn).to_be_enabled()
        self.DF_finance_quote_btn.click()

    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")