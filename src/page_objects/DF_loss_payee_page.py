from playwright.sync_api import Page, expect, TimeoutError
from models.DF_loss_payee_params import DFlossPayeeParams
from utils.helpers import get_num

class DFLossPayeePage:
    def __init__(self, page: Page):
       
            self.page = page
            self.full_name_input = self.page.get_by_role("textbox", description="Full Name", exact=True)        
            self.street1_input = self.page.locator(".MuiGrid-root.jss83.MuiGrid-item.MuiGrid-grid-xs-12.MuiGrid-grid-sm-12.MuiGrid-grid-md-6 > .jss94 > .jss97 > div > .MuiInputBase-root > .MuiInputBase-input").first
            self.street2_input = self.page.locator(".MuiGrid-root.jss83.MuiGrid-item.MuiGrid-grid-xs-12.MuiGrid-grid-sm-12.MuiGrid-grid-md-6 > .jss94 > .jss97 > div:nth-child(2) > .MuiInputBase-root > .MuiInputBase-input")
            self.city_input = self.page.locator(".MuiGrid-root.jss83.MuiGrid-item.MuiGrid-grid-xs-12.MuiGrid-grid-sm-12.MuiGrid-grid-md-6 > .jss94 > .jss97 > .MuiFormControl-root.MuiTextField-root.jss102 > .MuiInputBase-root > .MuiInputBase-input")
            self.state_select = self.page.locator(".MuiGrid-root.jss83.MuiGrid-item.MuiGrid-grid-xs-12.MuiGrid-grid-sm-12.MuiGrid-grid-md-6 > .jss94 > .jss97 > .MuiFormControl-root.MuiTextField-root.jss103 > .MuiInputBase-root > .MuiSelect-root")
            self.zip_input = self.page.locator(".jss97.jss99 > .MuiFormControl-root.MuiTextField-root.jss104 > .MuiInputBase-root > .MuiInputBase-input")
            self.loading_screen = self.page.locator(".jss53")
      

    def is_loss_payee_mortgage_selection(self,i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_increased_cov_b\"]")
    def loan_number_input(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.loss_payees.{i}.df_loan_number\"]")
    def is_mortgage_current_selection(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.loss_payees.{i}.df_mortgage_payments\"]")
    def loss_payee_container(self, i):
        return self.page.locator("div").filter(has_text=f"Loss Payee #{i+1}").nth(-2)
    def loss_payee_full_name_input(self, i):
        return self.loss_payee_container(i).locator("div input").nth(0)
    def loss_payee_street_address1_input(self, i):
        return self.loss_payee_container(i).locator("div input").nth(1)
    def loss_payee_street_address2_input(self, i):
        return self.loss_payee_container(i).locator("div input").nth(2)
    def loss_payee_city_input(self, i):
        return self.loss_payee_container(i).locator("div input").nth(3)
    def loss_payee_state_select(self, i):
        return self.loss_payee_container(i).locator("div select").first
    def loss_payee_zip_input(self, i):
        return self.loss_payee_container(i).locator("div input").nth(4)
    def has_loss_payee_select(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_has_loss_payees\"]")
    
    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")
  



