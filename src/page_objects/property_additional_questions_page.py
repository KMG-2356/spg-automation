import re
from playwright.sync_api import Page, expect, TimeoutError
from models.property_insured_params import InsuredInfoParams

class AdditionalQuestionsPage:
    def __init__(self, page: Page):
        self.page = page
        self.is_same_as_insured_selection = self.page.locator("[id=\"prop_misc.insp_same_as_insured\"]")
        self.insured_full_name_person_to_contact_input = self.page.locator("[id=\"prop_misc.insp_same_full_name\"]")
        self.insured_full_name_input = self.page.locator("[id=\"prop_misc.insp_full_name\"]")
        self.insured_contact_email_input = self.page.locator("[id=\"prop_misc.insp_email\"]")
        self.insured_contact_phone_number_input = self.page.locator("[id=\"prop_misc.insp_phone\"]")         
        self.loss_history_btn = self.page.get_by_role("button", name="Loss History")
        self.propert_endorsement_ext_select = self.page.locator("[id=\"prop_misc.ext_endst\"]")
        self.policy_term_select = self.page.locator("#term")
        self.loading_screen = self.page.locator(".jss53")       

    def fill_additional_question_information_form(self, params: InsuredInfoParams):  
        self.check_loading()
        if self.policy_term_select.is_visible():
            self.policy_term_select.select_option(params.policy_term)
            self.check_loading()
        if params.same_as_insured == "No":
            self.is_same_as_insured_selection.select_option(params.same_as_insured)
            self.check_loading()
            self.insured_full_name_input.fill(params.contact_full_name)
            self.insured_contact_email_input.fill(params.contact_email)
            self.insured_contact_phone_number_input.fill(params.contact_phone) 
            self.check_loading()
        if params.same_as_insured == "Yes":
            self.insured_full_name_person_to_contact_input.fill(params.contact_full_name)      
            self.check_loading()
        if self.propert_endorsement_ext_select.is_visible():
            self.propert_endorsement_ext_select.select_option("No")
            self.check_loading()
        
        expect(self.loss_history_btn).to_be_visible()
        expect(self.loss_history_btn).to_be_enabled()
        self.loss_history_btn.click()

    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")

