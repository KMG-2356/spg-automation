import re
from playwright.sync_api import Page, expect, TimeoutError
from models.apd_insured_info_params import APDInsuredInfoParams

class LossPayeeInformationPage:
    def __init__(self, page: Page):
        self.page = page
        self.has_loss_payee_select = self.page.locator("[id=\"cargo.loss_payees.pd_has_loss_payees\"]")
        self.vehicle_move_right_btn = self.page.locator(".MuiGrid-item").filter(has_text="Select Vehicles").nth(-1).get_by_label("move selected right")
        self.trailer_move_right_btn = self.page.locator(".MuiGrid-item").filter(has_text="Select Trailers").nth(-1).get_by_label("move selected right")
        self.add_another_loss_payee_btn = self.page.get_by_role("button", name="Add Another Loss Payee")
        self.loss_payee_info_heading = self.page.get_by_role("heading", name="    Loss Payee")
        self.loss_payee_street1_input = self.page.locator(".MuiGrid-container").filter(has_text="Loss Payee").nth(-2).locator("input").nth(1)
        self.loss_payee_street2_input = self.page.locator(".MuiGrid-container").filter(has_text="Loss Payee").nth(-2).locator("input").nth(2)
        self.loss_payee_city_input = self.page.locator(".MuiGrid-container").filter(has_text="Loss Payee").nth(-2).locator("input").nth(3)
        self.loss_payee_zip_input = self.page.locator(".MuiGrid-container").filter(has_text="Loss Payee").nth(-2).locator("input").nth(4)
        self.loss_payee_state_select = self.page.locator(".MuiGrid-container").filter(has_text="Loss Payee").nth(-2).locator("select").nth(0)
        self.coverages_btn = self.page.get_by_role("button", name="Coverages")
        self.loading_screen = self.page.locator(".jss53")

    def loss_payee_name_input(self, i):
        return self.page.locator(f"[id=\"cargo.loss_payees.pd_lpayees.{i}.pd_lp_name\"]")

    def loss_payee_apply_all_unit_select(self, i):
        return self.page.locator(f"[id=\"cargo.loss_payees.pd_lpayees.{i}.pd_all_apply\"]")

    def vehicle_choice(self, i):
        return self.page.locator(".MuiGrid-item").filter(has_text="Select Vehicles").nth(-1).get_by_role("list").nth(0).get_by_role("listitem").nth(i-1)

    def trailer_choice(self, i):
        return self.page.locator(".MuiGrid-item").filter(has_text="Select Trailers").nth(-1).get_by_role("list").nth(0).get_by_role("listitem").nth(i-1)

    def fill_apd_loss_payee_info_form(self, params):
        expect(self.loss_payee_info_heading).to_be_visible()
        self.has_loss_payee_select.select_option(params.has_loss_payee)

        if params.has_loss_payee == "Yes":
            for i, loss_payee in enumerate(params.loss_payees):
                if i > 0:
                    self.add_another_loss_payee_btn.click()
                    self.check_loading()
                self.loss_payee_name_input(i).fill(loss_payee["Loss Payee Name"])
                self.loss_payee_street1_input.fill(loss_payee["Address Street 1"])
                self.loss_payee_street2_input.fill(loss_payee["Address Street 2"])
                self.loss_payee_zip_input.fill(loss_payee["ZIP"])
                self.check_loading()
                self.loss_payee_city_input.fill(loss_payee["City"])
                self.loss_payee_state_select.select_option(loss_payee["State"])
                self.loss_payee_apply_all_unit_select(i).select_option(loss_payee["Applies to All Units / Trailers?"])
                self.check_loading()
                if loss_payee["Applies to All Units / Trailers?"] == "No":
                    units = self.parse_units(loss_payee["Assigned Units / Trailers (if not all)"])
                    print(f"units: {units}")
                    if len(units["Vehicle"]) > 0:
                        for choice in units["Vehicle"]:
                            self.check_loading()
                            self.vehicle_choice(choice).click()
                        self.check_loading()
                        if self.vehicle_move_right_btn.is_enabled():
                            self.vehicle_move_right_btn.click()
                            self.check_loading()

                    if len(units["Trailer"]) > 0:
                        for choice in units["Trailer"]:
                            self.check_loading()
                            self.trailer_choice(choice).click()
                        self.check_loading()
                        if self.trailer_move_right_btn.is_enabled():
                            self.trailer_move_right_btn.click()
                            self.check_loading()

        expect(self.coverages_btn).to_be_visible()
        expect(self.coverages_btn).to_be_enabled()
        self.coverages_btn.click()

    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")

    import re

    def parse_units(self, input_str: str) -> dict:
        result = {"Vehicle": [], "Trailer": []}
        
        if not input_str:
            return result
        
        result["Vehicle"] = [int(n) for n in re.findall(r'Vehicle\s*(\d+)', input_str, re.IGNORECASE)]
        result["Trailer"] = [int(n) for n in re.findall(r'Trailer\s*(\d+)', input_str, re.IGNORECASE)]
        
        return result
        