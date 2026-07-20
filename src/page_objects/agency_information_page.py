from playwright.sync_api import Page, expect, TimeoutError
from utils.helpers import to_float, get_num
from models.agency_info_params import AgencyInfoParams

class AgencyInformationPage:
    def __init__(self, page: Page):
        self.page = page
        self.agency_information_heading = self.page.get_by_role("heading", name="    Agency Information")
        self.agency_name_input = self.page.get_by_role("textbox").first
        self.agency_id_code_input = self.page.get_by_role("textbox").nth(1)
        self.agency_full_name_input = self.page.get_by_role("textbox").nth(2)
        self.email_input = self.page.get_by_role("textbox").nth(3)
        self.phone_number_input = self.page.get_by_role("textbox").nth(4)
        self.fax_number_input = self.page.get_by_role("textbox").nth(5)
        self.agent_commission_select = self.page.get_by_role("combobox").nth(1)
        self.street_address1_input = self.page.locator(".MuiInputBase-input.MuiInput-input").first
        self.street_address2_input = self.page.locator("div:nth-child(2) > .MuiInputBase-root > .MuiInputBase-input")
        self.city_input = self.page.locator(".MuiFormControl-root.MuiTextField-root.jss102 > .MuiInputBase-root > .MuiInputBase-input")
        self.state_select = self.page.get_by_role("combobox").first
        self.zip_code_input = self.page.locator(".MuiFormControl-root.MuiTextField-root.jss104 > .MuiInputBase-root > .MuiInputBase-input")
        self.insured_information_btn = self.page.get_by_role("button", name="Insured Information")
        self.loading_screen = self.page.locator(".jss53")


    # def fill_agency_information_form(self, data):
    #     expect(self.agency_information_heading).to_be_visible()
    #     self.agency_name_input.fill(data["01_Policy_Info"][0]["Agency Name"])
    #     self.agency_id_code_input.fill(data["01_Policy_Info"][0]["Agency ID Code"])
    #     self.agency_full_name_input.fill(data["01_Policy_Info"][0]["Agent Full Name"])
    #     self.email_input.fill(data["01_Policy_Info"][0]["Agent E-Mail"])
    #     self.phone_number_input.fill(data["01_Policy_Info"][0]["Agent Phone"])
    #     self.fax_number_input.fill(data["01_Policy_Info"][0]["Agent Fax"])
    #     self.agent_commission_select.select_option(to_float(get_num(str(data["01_Policy_Info"][0]["Agent's Commission %"]))))
    #     self.street_address1_input.fill(data["01_Policy_Info"][0]["Address - Street 1"])
    #     self.street_address2_input.fill(data["01_Policy_Info"][0]["Address - Street 2"])
    #     self.city_input.fill(data["01_Policy_Info"][0]["Address - City"])
    #     self.state_select.select_option(label=data["01_Policy_Info"][0]["Address - State"])
    #     self.zip_code_input.fill(str(data["01_Policy_Info"][0]["Address - Zip"]))
    #     self.insured_information_btn.click()

    def fill_agency_information_form(self, params: AgencyInfoParams):
        expect(self.agency_information_heading).to_be_visible()
        self.agency_name_input.fill(params.agency_name)
        self.agency_id_code_input.fill(params.agency_id_code)
        self.agency_full_name_input.fill(params.agent_full_name)
        self.email_input.fill(params.agent_email)
        self.phone_number_input.fill(params.agent_phone)
        self.fax_number_input.fill(params.agent_fax)
        self.agent_commission_select.select_option(to_float(get_num(params.agent_commission)))
        self.zip_code_input.fill(params.zip_code)
        self.check_loading()
        self.street_address1_input.fill(params.address_street1)
        self.street_address2_input.fill(params.address_street2)
        self.city_input.fill(params.city)
        self.state_select.select_option(params.state)
        self.insured_information_btn.click()

    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")
    
