from playwright.sync_api import Page, expect, TimeoutError
from models.inland_marine_params import InlandMarineParams

class InlandMarinePage:
    def __init__(self, page: Page):
        self.page = page
        self.scheduled_equipment_coverage_btn = self.page.get_by_text("Scheduled Equipment Coverage")
        self.miscellaneous_article_coverage_btn = self.page.get_by_text("Miscellaneous Articles")
        self.used_for_logging_select = self.page.locator("[id=\"im.logging\"]")
        self.has_loss_payees_select = self.page.locator("[id=\"im.has_loss_payees\"]")
        self.add_another_equipment = self.page.get_by_role("button", name="Add Another Item to Schedule")
        self.add_loss_payee_btn = self.page.get_by_role("button", name="Add Another Loss Payee")
        self.total_value_of_misc_items = self.page.locator("[id=\"im.misc_articles_value\"]")
        self.loss_history_btn = self.page.get_by_role("button", name="Loss History")
        self.loading_screen = self.page.locator(".jss53")
    

    def scheduled_equipment_description_input(self, i):
        return self.page.locator(f"[id=\"im.equipment.{i}.description\"]")
    
    def scheduled_equipment_manufacturer_input(self, i):
        return self.page.locator(f"[id=\"im.equipment.{i}.manufacturer\"]")
    
    def scheduled_equipment_serial_number_input(self, i):
        return self.page.locator(f"[id=\"im.equipment.{i}.serial\"]")
    
    def scheduled_equipment_value_input(self, i):
        return self.page.locator(f"[id=\"im.equipment.{i}.value\"]")
    
    def loss_payee_name_input(self,i):
        return self.page.locator(f"[id=\"im.loss_payees.{i}.name\"]")

    def loss_payee_equipment_select(self,i):
        return self.page.locator(f"[id=\"im.loss_payees.{i}.equipment\"]")
    
    def loss_payee_interest_select(self,i):
        return self.page.locator(f"[id=\"im.loss_payees.{i}.interest\"]")

    def loss_payee_container(self, i):
        return self.page.locator(".MuiGrid-container").filter(has=self.page.locator(f"[id='im.loss_payees.{i}.name']")).nth(-1)

    def loss_payee_street_address1_input(self, i):
        return self.loss_payee_container(i).locator(".MuiFormControl-root", has_text="Street Address 1").locator("input")

    def loss_payee_street_address2_input(self, i):
        return self.loss_payee_container(i).locator(".MuiFormControl-root", has_text="Street Address 2").locator("input")
    
    def loss_payee_city_input(self, i):
        return self.loss_payee_container(i).locator(".MuiFormControl-root", has_text="city").locator("input")

    def loss_payee_zip_input(self, i):
        return self.loss_payee_container(i).locator(".MuiFormControl-root", has_text="zip").locator("input")
    
    def loss_payee_state_select(self, i):
        return self.loss_payee_container(i).locator(".MuiFormControl-root", has_text="state").locator("select")
    
    def loss_payee_loan_number_input(self, i):
        return self.page.locator(f"[id=\"im.loss_payees.{i}.loan_number\"]")

    def fill_inland_marine_form(self, params: InlandMarineParams):
        self.scheduled_equipment_coverage_btn.click()
        self.check_loading()
        
        if params.miscellaneous_article_coverage == "Yes":
            self.miscellaneous_article_coverage_btn.click()
            self.check_loading()
        
        for i, equipment in enumerate(params.equipments):
            if i > 0:
                self.add_another_equipment.click()
                self.check_loading()
            self.scheduled_equipment_description_input(i).fill(equipment["Description"])
            self.scheduled_equipment_manufacturer_input(i).fill(equipment["Manufacturer"])
            self.scheduled_equipment_serial_number_input(i).fill(equipment["Serial Number"])
            self.scheduled_equipment_value_input(i).fill(equipment["Value ($)"])

        self.has_loss_payees_select.select_option(params.has_loss_payees)
        self.check_loading()

        if self.used_for_logging_select.is_visible():
            self.used_for_logging_select.select_option(params.used_for_logging)
            self.check_loading()

        if params.has_loss_payees == "Yes":
            for i, loss_payee in enumerate(params.loss_payees):
                if i > 0:
                    self.add_loss_payee_btn.click()
                self.loss_payee_name_input(i).fill(loss_payee["Loss Payee Name"])
                self.loss_payee_street_address1_input(i).fill(loss_payee["Street Address"])
                self.loss_payee_zip_input(i).fill(loss_payee["ZIP"])
                self.check_loading()
                self.loss_payee_city_input(i).fill(loss_payee["City"])
                self.loss_payee_state_select(i).select_option(loss_payee["State"])
                self.loss_payee_equipment_select(i).select_option(loss_payee["Equipment Item #"])
                self.check_loading()
                self.loss_payee_interest_select(i).select_option(loss_payee["Interest Type"])
                self.check_loading()
                if self.loss_payee_loan_number_input(i).is_visible():
                    self.loss_payee_loan_number_input(i).fill(loss_payee["Loan Number (if Lenders LP)"])

        if self.total_value_of_misc_items.is_visible():
            self.total_value_of_misc_items.fill(params.total_value_of_misc_items)

        expect(self.loss_history_btn).to_be_visible()
        expect(self.loss_history_btn).to_be_enabled()
        self.loss_history_btn.click()
                
    
    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")
