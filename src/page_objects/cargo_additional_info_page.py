from playwright.sync_api import Page, expect, TimeoutError
from models.cargo_additional_info_params import CargoAdditionalInformationParams

class CargoAdditionalInformationPage:
    def __init__(self, page: Page):
        self.page = page
        self.estimated_gross_revenue_for_coming_year_input = self.page.locator("[id=\"cargo.additional.gr_estimate\"]")
        self.loss_history_btn = self.page.get_by_role("button", name="Loss History", exact=True)
        self.loading_screen = self.page.locator(".jss53")

    def fill_additional_info(self, params: CargoAdditionalInformationParams):
        self.estimated_gross_revenue_for_coming_year_input.fill(params.estimated_gross_revenue_for_coming_year)
        expect(self.loss_history_btn).to_be_visible()
        expect(self.loss_history_btn).to_be_enabled()
        self.loss_history_btn.click()
    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")
