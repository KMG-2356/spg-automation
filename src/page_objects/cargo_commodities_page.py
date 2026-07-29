from playwright.sync_api import Page, expect, TimeoutError
from models.cargo_commodities_params import CargoCommoditiesParams

class CargoCommoditiesPage:
    def __init__(self, page: Page):
        self.page = page
        self.cargo_includes_liquor_manufactured_tobacco_select = self.page.locator("[id=\"cargo.commodities.liquor_tobacco\"]")
        self.cargo_includes_oversized_overweight_commodities_select = self.page.locator("[id=\"cargo.commodities.overweight\"]")
        self.cargo_includes_excluded_commodities_select = self.page.locator("[id=\"cargo.commodities.exclusions\"]")
        self.add_another_commodities_btn = self.page.get_by_role("button", name="Add Another Commodity")
        self.loss_history_btn = self.page.get_by_role("button", name="Loss History Information")
        self.loading_screen = self.page.locator(".jss53")
        self.add_commodity_btn = self.page.get_by_role("button", name="Add Another Commodity")
    def commodity_selection(self, i: int):
        return self.page.locator(f"[id=\"cargo.commodities.comms.{i}.commodity\"]")
    def percent_of_cargo_input(self, i: int):
        return self.page.locator(f"[id=\"cargo.commodities.comms.{i}.percent\"]")
    def average_value_per_load_input(self, i: int):
        return self.page.locator(f"[id=\"cargo.commodities.comms.{i}.avg_value\"]")
    def maximum_value_per_load_input(self, i: int):
        return self.page.locator(f"[id=\"cargo.commodities.comms.{i}.max_value\"]")
    def fill_commodities(self, params: CargoCommoditiesParams):
        self.cargo_includes_liquor_manufactured_tobacco_select.select_option(params.cargo_includes_liquor_manufactured_tobacco)
        self.check_loading()
        self.cargo_includes_oversized_overweight_commodities_select.select_option(params.cargo_includes_oversized_overweight_commodities)
        self.check_loading()
        self.cargo_includes_excluded_commodities_select.select_option(params.cargo_includes_excluded_commodities)
        self.check_loading()
        for i, commodity in enumerate(params.commodities):
            if i > 0:
                self.add_another_commodities_btn.click()
                self.check_loading()       
            self.commodity_selection(i).select_option(commodity.commodity)
            self.check_loading()
            self.percent_of_cargo_input(i).fill("100")
            self.check_loading()
            self.page.wait_for_timeout(10000)
            self.average_value_per_load_input(i).fill(commodity.average_value_per_load)
            self.check_loading()            
            self.maximum_value_per_load_input(i).fill(commodity.maximum_value_per_load)
            self.check_loading()

        expect(self.loss_history_btn).to_be_visible()
        expect(self.loss_history_btn).to_be_enabled()
        self.loss_history_btn.click()

    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")   









