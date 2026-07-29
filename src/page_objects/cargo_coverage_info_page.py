from playwright.sync_api import Page, expect, TimeoutError
from models.cargo_coverage_params import CargoCoverageParams

class CargoCoveragesInformationPage:
    def __init__(self, page: Page):
        self.page = page
        self.terminal_coverage_required_select= self.page.locator("[id=\"cargo.coverages.terminal_coverage\"]")
        self.trailer_interchange_coverage_required_select = self.page.locator("[id=\"cargo.coverages.trailer_interchange\"]")
        self.TI_limit_input = self.page.locator("[id=\"cargo.coverages.trailer_interchange_limit\"]")
        self.written_TI_agreement_in_place_select_ = self.page.locator("[id=\"cargo.coverages.written_agreement\"]")
        self.refrigeration_breakdown_coverage_required_select = self.page.locator("[id=\"cargo.coverages.refrigeration_breakdown\"]")
        self.any_refer_trailers_older_than_10years_select = self.page.locator("[id=\"cargo.coverages.trailer_age\"]")
        self.refer_trailer_serviced_at_least_every_30days_select = self.page.locator("[id=\"cargo.coverages.reefer_trailer_serviced\"]")
        self.hauls_seafood_or_shellfish_select = self.page.locator("[id=\"cargo.coverages.seafood\"]")
        self.cargo_limit_per_unit_input = self.page.locator("[id=\"cargo.coverages.unit_limit\"]")
        self.average_exposure_per_unit_input = self.page.locator("[id=\"cargo.coverages.avg_exposure\"]")
        self.maximum_exposure_per_unit_input = self.page.locator("[id=\"cargo.coverages.max_exposure\"]")
        self.loads_ever_exceed_cargo_insurance_limit_select = self.page.locator("[id=\"cargo.coverages.greater_cargo\"]")
        self.cargo_deductible_select = self.page.locator("[id=\"cargo.coverages.cargo_deductible\"]")
        self.radius_of_operations_select = self.page.locator("[id=\"cargo.coverages.radius\"]")
        self.cov_info_btn = self.page.get_by_role("button", name="Coverages")
        self.commodities_info_btn = self.page.get_by_role("button", name="Commodities")
        self.loading_screen = self.page.locator(".jss53")


    def fill_cargo_coverages_info(self, params: CargoCoverageParams):
        self.cov_info_btn.click()
        self.terminal_coverage_required_select.select_option(params.terminal_coverage_required)
        self.check_loading()
        self.trailer_interchange_coverage_required_select.select_option(params.trailer_interchange_coverage_required)
        self.check_loading()
        if params.trailer_interchange_coverage_required =="Yes":
            self.TI_limit_input.fill(params.TI_limit)
            self.check_loading()         
            self.written_TI_agreement_in_place_select_.select_option(params.written_TI_agreement_in_place)
            self.check_loading()
        self.refrigeration_breakdown_coverage_required_select.select_option(params.refrigeration_breakdown_coverage_required)
        self.check_loading()            
        if params.refrigeration_breakdown_coverage_required =="Yes":
            self.any_refer_trailers_older_than_10years_select.select_option(params.any_refer_trailers_older_than_10years)
            self.check_loading()
            self.refer_trailer_serviced_at_least_every_30days_select.select_option(params.refer_trailer_serviced_at_least_every_30days)
            self.check_loading()
            self.hauls_seafood_or_shellfish_select.select_option(params.hauls_seafood_or_shellfish)
            self.check_loading()
        self.cargo_limit_per_unit_input.fill(params.cargo_limit_per_unit)
        self.check_loading()
        self.average_exposure_per_unit_input.fill(params.average_exposure_per_unit)
        self.check_loading()
        self.maximum_exposure_per_unit_input.fill(params.maximum_exposure_per_unit)
        self.check_loading()
        self.loads_ever_exceed_cargo_insurance_limit_select.select_option(params.loads_ever_exceed_cargo_insurance_limit)
        self.check_loading()
        self.cargo_deductible_select.select_option(params.cargo_deductible)
        self.check_loading()
        print(params.radius_of_operations)
        self.radius_of_operations_select.select_option(params.radius_of_operations)
        self.check_loading()
        expect(self.commodities_info_btn).to_be_visible()
        expect(self.commodities_info_btn).to_be_enabled()
        self.commodities_info_btn.click()

    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")