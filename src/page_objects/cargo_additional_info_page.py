from playwright.sync_api import Page, expect, TimeoutError
from models.cargo_additional_info_params import CargoAdditionalInformationParams

class CargoAdditionalInformationPage:
    def __init__(self, page: Page):
        self.page = page
        self.estimated_gross_revenue_for_coming_year_input = self.page.locator("[id=\"cargo.additional.gr_estimate\"]")
        self.own_haul_total1_input = self.page.locator("[id=\"cargo.additional.gr_years.0.own\"]")
        self.subcontracted_total1_input = self.page.locator("[id=\"cargo.additional.gr_years.0.subcontracted\"]")
        self.own_haul_total2_input = self.page.locator("[id=\"cargo.additional.gr_years.1.own\"]")
        self.subcontracted_total2_input = self.page.locator("[id=\"cargo.additional.gr_years.1.subcontracted\"]")
        self.own_haul_total3_input = self.page.locator("[id=\"cargo.additional.gr_years.2.own\"]")
        self.subcontracted_total3_input = self.page.locator("[id=\"cargo.additional.gr_years.2.subcontracted\"]")
        self.loss_history_btn = self.page.get_by_role("button", name="Loss History", exact=True)
        self.loading_screen = self.page.locator(".jss53")

    def fill_additional_info(self, params: CargoAdditionalInformationParams):
        self.estimated_gross_revenue_for_coming_year_input.fill(params.estimated_gross_revenue_for_coming_year)
        if self.own_haul_total1_input.is_visible():
           self.own_haul_total1_input.fill(params.own_haul_total)
        if self.own_haul_total2_input.is_visible():
           self.own_haul_total2_input.fill(params.own_haul_total)
        if self.own_haul_total3_input.is_visible():
           self.own_haul_total3_input.fill(params.own_haul_total)
        if self.subcontracted_total1_input.is_visible():
           self.subcontracted_total1_input.fill(params.subcontracted_total)  
        if self.subcontracted_total2_input.is_visible():
           self.subcontracted_total2_input.fill(params.subcontracted_total)  
        if self.subcontracted_total3_input.is_visible():
           self.subcontracted_total3_input.fill(params.subcontracted_total)            


        expect(self.loss_history_btn).to_be_visible()
        expect(self.loss_history_btn).to_be_enabled()
        self.loss_history_btn.click()
    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")
