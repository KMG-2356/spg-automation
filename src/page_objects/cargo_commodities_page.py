from playwright.sync_api import Page, expect, TimeoutError
from models.cargo_commodities_params import CargoCommoditiesParams

class HomeOwnersLossHistoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.cargo_includes_liquor_manufactured_tobacco_select = self.page.locator("[id=\"cargo.commodities.liquor_tobacco\"]")
        self.cargo_includes_oversized_overweight_commodities_select = self.page.locator("[id=\"cargo.commodities.overweight\"]")
        self.cargo_includes_excluded_commodities_select = self.page.locator("[id=\"cargo.commodities.exclusions\"]")
        self.add_another_commodities_btn = self.page.get_by_role("button", name="Add Another Commodity")
        self.loss_history_btn = self.page.get_by_role("button", name="Loss History Information")
    def commodity_selection(self, i: int):
        return self.page.locator(f"[id=\"cargo.commodities.comms.{i}.commodity\"]")
    def percent_of_cargo_input(self, i: int):
        return self.page.locator(f"[id=\"cargo.commodities.comms.{i}.percent\"]")
    def average_value_per_load_input(self, i: int):
        return self.page.locator(f"[id=\"cargo.commodities.comms.{i}.avg_value\"]")
    def maximum_value_per_load_input(self, i: int):
        return self.page.locator(f"[id=\"cargo.commodities.comms.{i}.max_value\"]")
    def fill_commodities(self, params: CargoCommoditiesParams):
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











    .select_option("Bulk_Liquid_Cargoes")
    .click()
    .click()
    .click()
    .click()