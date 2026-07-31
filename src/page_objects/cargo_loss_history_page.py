from playwright.sync_api import Page, expect, TimeoutError
from models.cargo_loss_history_info_params import LossHistoryParams

class LossHistoryInformationPage:
    def __init__(self, page: Page):
        self.page = page
        self.any_losses_in_the_past_3Years_selection = self.page.locator("[id=\"cargo.loss_history.has_losses\"]") 
        self.loading_screen = self.page.locator(".jss53")
        self.add_loss_btn = self.page.get_by_role("button", name="Add Another Loss")
        self.add_info_btn = self.page.get_by_role("button", name="Additional Information")
    def loss_year_input(self, i: int):
        return self.page.locator(f"[id=\"cargo.loss_history.losses.{i}.loss_year\"]")
    def loss_premium_input(self, i: int):
        return self.page.locator(f"[id=\"cargo.loss_history.losses.{i}.loss_premium\"]")
    def loss_type_select(self, i: int):
        return self.page.locator(f"[id=\"cargo.loss_history.losses.{i}.loss_type\"]")
    def loss_paid_input(self, i: int):
        return self.page.locator(f"[id=\"cargo.loss_history.losses.{i}.loss_paid\"]")
    def loss_outstanding_input(self, i: int):
        return self.page.locator(f"[id=\"cargo.loss_history.losses.{i}.loss_outstanding\"]")
    def loss_description_input(self, i: int):
        return self.page.locator(f"[id=\"cargo.loss_history.losses.{i}.loss_other\"]")


    def fill_loss_history_info(self, params: LossHistoryParams):
        self.any_losses_in_the_past_3Years_selection.select_option(params.any_losses_in_the_past_3Years)
        self.check_loading()
        # if self.any_losses_in_the_past_3Years_selection == "Yes":
        for i, loss in enumerate(params.losses):
            if i > 0:
                self.add_loss_btn.click()
                self.check_loading()      
            if self.loss_year_input(i).is_visible(): 
                self.loss_year_input(i).fill(loss.loss_year)
                self.check_loading()
            if self.loss_premium_input(i).is_visible():
                self.loss_premium_input(i).fill(loss.premium_at_time_of_loss)
                self.check_loading()
            if self.loss_type_select(i).is_visible():
                self.loss_type_select(i).select_option(loss.type_of_loss)
                self.check_loading()
            if self.loss_description_input(i).is_visible():
                self.loss_description_input(i).fill("Other")
            if self.loss_paid_input(i).is_visible():
                self.loss_paid_input(i).fill(loss.amount_paid)
                self.check_loading()
            if self.loss_outstanding_input(i).is_visible():
                self.loss_outstanding_input(i).fill(loss.amount_outstanding)
                self.check_loading()


        expect(self.add_info_btn).to_be_visible()
        expect(self.add_info_btn).to_be_enabled()
        self.add_info_btn.click()

    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")   









