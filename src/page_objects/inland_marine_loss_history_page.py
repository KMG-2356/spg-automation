from playwright.sync_api import Page, expect, TimeoutError
from models.inland_marine_loss_history_params import InlandMarineLossHistoryParams

class InlandMarineLossHistoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.has_loss_history_select = self.page.locator("[id=\"history.has_loss\"]")
        self.has_extra_subjectivity_select = self.page.locator("[id=\"history.has_extra_subs\"]")
        self.additional_notes_input = self.page.locator("[id=\"history.notes\"]")
        self.add_another_subjectivity_btn = self.page.get_by_role("button", name="Add Another Subjectivity")
        self.add_another_loss_btn = self.page.get_by_role("button", name="Add Another Loss")
        self.finance_quote_btn = self.page.get_by_role("button", name="Finance Quote")
        self.loading_screen = self.page.locator(".jss53")

    def subjectivity_input(self, i):
        return self.page.locator("[id=\"history.extra_subs.0.text\"]")
    
    def loss_date_input(self, i: int):
        return self.page.locator(f"[id=\"history.losses.{i}.loss_date\"]")

    def loss_type_select(self, i: int):
        return self.page.locator(f"[id=\"history.losses.{i}.type\"]")

    def loss_details_input(self, i: int):
        return self.page.locator(f"[id=\"history.losses.{i}.details\"]")

    def loss_amount_input(self, i: int):
        return self.page.locator(f"[id=\"history.losses.{i}.amount\"]")
    
    def fill_loss_history_form(self, params: InlandMarineLossHistoryParams):
        self.has_loss_history_select.select_option("No")
        self.check_loading()
        self.has_extra_subjectivity_select.select_option("No")
        self.check_loading()
        expect(self.finance_quote_btn).to_be_visible()
        expect(self.finance_quote_btn).to_be_enabled()
        self.finance_quote_btn.click()

    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")
        
