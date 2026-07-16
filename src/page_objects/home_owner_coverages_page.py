from playwright.sync_api import Page, expect, TimeoutError
from models.home_owners_coverages_params import HomeOwnersCoveragesParams

class HomeOwnersCoveragesPage:
    def __init__(self, page: Page):
        self.page = page

        self.dwelling_value_input = self.page.locator("[id=\"ho.coverages.dwelling_value\"]")

        self.cov_b_select = self.page.locator("[id=\"ho.coverages.cov_b\"]")
        self.cov_c_select = self.page.locator("[id=\"ho.coverages.cov_c\"]")
        self.cov_d_select = self.page.locator("[id=\"ho.coverages.cov_d\"]")
        self.limit_of_liability_select = self.page.locator("[id=\"ho.coverages.limit_of_liability\"]")
        self.med_pay_select = self.page.locator("[id=\"ho.coverages.med_pay\"]")
        self.home_systems_protection_select = self.page.locator("[id=\"ho.coverages.home_systems_protection\"]")
        self.service_line_select = self.page.locator("[id=\"ho.coverages.service_line\"]")
        self.identity_theft_select = self.page.locator("[id=\"ho.coverages.identity_theft\"]")
        self.water_backup_select = self.page.locator("[id=\"ho.coverages.water_backup\"]")
        self.replacement_cost_pp_select = self.page.locator("[id=\"ho.coverages.replacement_cost_pp\"]")
        self.extended_repl_cost_dwell_select = self.page.locator("[id=\"ho.coverages.extended_repl_cost_dwell\"]")
        self.special_comp_coverage_select = self.page.locator("[id=\"ho.coverages.special_comp_coverage\"]")
        self.loading_screen = self.page.locator(".jss53")

        self.home_owners_addition_questions_btn = self.page.get_by_role("button", name="Homeowners Additional")

    def fill_coverages_info(self, params: HomeOwnersCoveragesParams):
        self.dwelling_value_input.fill(str(params.dwelling_value))

        self.cov_b_select.select_option(params.cov_b)
        self.check_loading()
        self.cov_c_select.select_option(params.cov_c)
        self.check_loading()
        self.cov_d_select.select_option(params.cov_d)
        self.check_loading()
            
        self.limit_of_liability_select.select_option(params.limit_of_liability)
        self.check_loading()
        self.med_pay_select.select_option(params.med_pay)
        self.check_loading()
            
        self.home_systems_protection_select.select_option(params.home_systems_protection)
        self.check_loading()
        self.service_line_select.select_option(params.service_line)
        self.check_loading()
        self.identity_theft_select.select_option(params.identity_theft)
        self.check_loading()
        self.water_backup_select.select_option(params.water_backup)
        self.check_loading()
        self.replacement_cost_pp_select.select_option(params.replacement_cost_pp)
        self.check_loading()
        self.extended_repl_cost_dwell_select.select_option(params.extended_repl_cost_dwell)
        self.check_loading()
        self.special_comp_coverage_select.select_option(params.special_comp_coverage)
        self.check_loading()

        expect(self.home_owners_addition_questions_btn).to_be_visible()
        expect(self.home_owners_addition_questions_btn).to_be_enabled()
        self.home_owners_addition_questions_btn.click()

    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")