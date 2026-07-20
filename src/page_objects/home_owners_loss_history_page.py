from playwright.sync_api import Page, expect, TimeoutError
from models.home_owners_loss_history_params import HomeOwnersLossHistoryParams

class HomeOwnersLossHistoryPage:
    def __init__(self, page: Page):
        self.page = page

        self.open_claims_select = self.page.locator("[id=\"ho.loss_history.open_claims\"]")
        self.has_loss_select = self.page.locator("[id=\"ho.loss_history.has_loss\"]")
        self.unrepaired_select = self.page.locator("[id=\"ho.loss_history.unrepaired\"]")
        self.add_another_loss_btn = self.page.locator("button", has_text="Add Another Loss")
        self.home_owners_coverages_btn = self.page.get_by_role("button", name="Homeowners Coverages")
        self.loading_screen = self.page.locator(".jss53")

    def loss_date_input(self, i: int):
        return self.page.locator(f"[id=\"ho.loss_history.losses.{i}.loss_date\"]")

    def loss_type_select(self, i: int):
        return self.page.locator(f"[id=\"ho.loss_history.losses.{i}.type\"]")

    def loss_details_input(self, i: int):
        return self.page.locator(f"[id=\"ho.loss_history.losses.{i}.details\"]")

    def loss_amount_input(self, i: int):
        return self.page.locator(f"[id=\"ho.loss_history.losses.{i}.amount\"]")

    def fill_loss_history(self, params: HomeOwnersLossHistoryParams):

        self.open_claims_select.select_option(params.open_claims)
        self.check_loading()
        self.has_loss_select.select_option(params.has_loss)
        self.check_loading()
        if self.unrepaired_select.is_visible():
            self.unrepaired_select.select_option(params.unrepaired)
            self.check_loading()

        if params.has_loss == "Yes":
            for i, loss in enumerate(params.losses):
                print(f"Loss Object: {loss}")
                if i > 0:
                    self.add_another_loss_btn.click()

                self.loss_date_input(i).fill(loss["Loss Date"])
                self.loss_type_select(i).select_option(loss["Type of Loss"])
                self.loss_details_input(i).fill(loss["Details"])
                self.loss_amount_input(i).fill(loss["Amount ($)"])

        expect(self.home_owners_coverages_btn).to_be_visible()
        expect(self.home_owners_coverages_btn).to_be_enabled()
        self.home_owners_coverages_btn.click()

    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")