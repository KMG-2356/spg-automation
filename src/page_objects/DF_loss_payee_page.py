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
      
    def is_loss_payee_mortgage_selection(self,i):
        return self.page.locator(f"[id=\"df.locations.{i}.df_increased_cov_b\"]")
    def loan_number_input(self, i):
        return self. page.locator(f"[id=\"df.locations.{i}.loss_payees.{i}.df_loan_number\"]")
    def is_mortgage_current_selection(self, i):
        return self.page.locator(f"[id=\"df.locations.{i}.loss_payees.{i}.df_mortgage_payments\"]")
    
    
    def fill_df_loss_payee_information(self,params: DFlossPayeeParams):      
      
        for i in range(len(params.loss_payees)):
            self.is_loss_payee_mortgage_selection.select_option(params.loss_payee[i]["Street Address"])
            self.check_loading()  
            self.city_input.fill(params.locations[i]["City"])
            self.check_loading() 
            self.state_selection.select_option(params.locations[i]["State"])           
            self.check_loading() 
            if i < len(data["02_WH_Locations"]) - 1:
              expect(self.add_location_button).to_be_visible()
              expect(self.add_location_button).to_be_enabled()
              self.add_location_button.click()

    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")
  



