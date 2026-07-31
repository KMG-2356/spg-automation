from playwright.sync_api import Page, expect, TimeoutError
from models.apd_coverages_info_params import APDCoveragesParams

class APDCoveragesPage:

    def __init__(self, page: Page):
        self.page = page

        self.refrigeration_breakdown_select = self.page.locator(
            '[id="cargo.coverages.refrigeration_breakdown"]'
        )
        self.trailer_age_select = self.page.locator(
            '[id="cargo.coverages.trailer_age"]'
        )
        self.reefer_trailer_serviced_select = self.page.locator(
            '[id="cargo.coverages.reefer_trailer_serviced"]'
        )
        self.seafood_select = self.page.locator(
            '[id="cargo.coverages.seafood"]'
        )
        self.radius_select = self.page.locator('[id="cargo.coverages.radius"]')
        self.phys_dam_deductible_select = self.page.locator(
            '[id="cargo.coverages.phys_dam_deductible"]'
        )
        self.ts_limit_select = self.page.locator(
            '[id="cargo.coverages.ts_limit"]'
        )

        self.commodities_btn = self.page.get_by_role("button", name="Commodities")
        self.loading_screen = self.page.locator(".jss53")

    def fill_cargo_coverages(self, params: APDCoveragesParams) -> None:
        self.refrigeration_breakdown_select.select_option(
            params.refrigeration_breakdown
        )
        self.check_loading()
        if self.trailer_age_select.is_visible():
            self.trailer_age_select.select_option(params.trailer_age)
            self.check_loading()

            self.reefer_trailer_serviced_select.select_option(
                params.reefer_trailer_serviced
            )
            self.check_loading()
            self.seafood_select.select_option(params.seafood)
            self.check_loading()

        self.radius_select.select_option(params.radius)
        self.check_loading()

        if self.phys_dam_deductible_select.is_visible():
            self.phys_dam_deductible_select.select_option(
                params.phys_dam_deductible
            )
            self.check_loading()

        self.ts_limit_select.select_option(params.ts_limit)
        self.check_loading()

        expect(self.commodities_btn).to_be_visible()
        expect(self.commodities_btn).to_be_enabled()
        self.commodities_btn.click()

    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")