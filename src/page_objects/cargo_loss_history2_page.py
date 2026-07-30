from playwright.sync_api import Page, expect, TimeoutError
from models.cargo_loss_history2_params import CargoLossHistory2Params

class LossHistoryInformation2Page:
    def __init__(self, page: Page):
        self.page = page
        self.any_losses_in_the_past_3Years_selection = self.page.locator("[id=\"history.has_loss\"]")
        self.any_unreapired_damage_from_prior_loss_selection = self.page.locator("[id=\"history.unrepaired\"]") 
        self.add_extra_subs_selection = self.page.locator("[id=\"history.has_extra_subs\"]")
        self.additional_notes_input = self.page.locator("[id=\"history.notes\"]")
        self.loading_screen = self.page.locator(".jss53")
        self.add_loss_btn = self.page.get_by_role("button", name="Add Another Loss")
        self.add_subjectivity_btn = self.page.get_by_role("button", name="Add Another Sujectivity")
        self.finance_quote_btn = self.page.get_by_role("button", name="Finance Quote")

    # page.get_by_role("combobox").nth(2).click()
    # page.get_by_role("combobox").nth(2).select_option("fire")
    # page.get_by_role("textbox", description="Details", exact=True).click()
    # page.get_by_role("textbox", description="Amount", exact=True).click()

    def loss_date_input(self, i: int):
        return self.page.locator(f"[id=\"history.losses.0.loss_date\"]")
    def loss_details_input(self, i: int):
        return self.page.locator(f"[id=\"history.losses.{i}.details\"]")
    def loss_type_select(self, i: int):
        return self.page.locator(f"[id=\"history.losses.{i}.type\"]")
    def loss_amount_input(self, i: int):
        return self.page.locator(f"[id=\"history.losses.{i}.amount\"]")
    def loss_subjectivity_text_input(self, i: int):
        return self.page.locator(f"[id=\"history.extra_subs.{i}.text\"]")
    def loss_date_input(self, i: int):
        return self.page.locator(f"[id=\"history.losses.{i}.loss_date\"]")


    def fill_loss_history2_info(self, params: CargoLossHistory2Params):
        self.any_losses_in_the_past_3Years_selection.select_option(params.any_losses_in_the_past3_years)
        self.check_loading()        
        self.add_extra_subs_selection.select_option(params.add_extra_subjectivities)
        self.check_loading()
        self.additional_notes_input.fill(params.notes_about_the_insured)
        self.check_loading()
        if params.any_losses_in_the_past3_years == "Yes":
            self.any_unreapired_damage_from_prior_loss_selection.select_option(params.any_unrepaired_damage_from_prior_losses)
            self.check_loading()
            for i, loss in enumerate(params.losses2):
                if i > 0:
                    self.add_loss_btn.click()
                    self.check_loading()       
                self.loss_date_input(i).fill(loss.loss_date)
                self.check_loading()
                self.loss_amount_input(i).fill(loss.amount)
                self.check_loading()
                self.loss_type_select(i).select_option("Fire")
                self.check_loading()
                self.loss_details_input(i).fill(loss.details)
                self.check_loading()

        if params.add_extra_subjectivities=="Yes":
            for i, subjective in enumerate(params.subjectivity):
                if i > 0:
                    self.add_subjectivity_btn.click()
                    self.check_loading()       
                self.loss_subjectivity_text_input(i).fill(subjective.subjectivity_text)
                self.check_loading()

        expect(self.finance_quote_btn).to_be_visible()
        expect(self.finance_quote_btn).to_be_enabled()
        self.finance_quote_btn.click()

    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")   









