from playwright.sync_api import Page, expect, TimeoutError
from models.cargo_insured_info_params import CargoInsuredInformationParams

class CargoInsuredInformationPage:
    def __init__(self, page: Page):
        self.page = page
        self.terminal_coverage_required_select= self.page.locator("[id=\"cargo.insured.different_name\"]")
        self.trailer_interchange_coverage_required: str =""	
        self.TI_limit: str =""	
        self.written_TI_agreement_in_place: str =""
        self.refrigeration_breakdown_coverage_required: str =""
        self.any_refer_trailers_older_than_10years: str =""
        self.refer_trailer_serviced_at_least_every_30days: str =""
        self.hauls_seafood_or_shellfish: str =""
        self.cargo_limit_per_unit: str =""	
        self.average_exposure_per_unit: str =""
        self.maximum_exposure_per_unit: str =""
        self.loads_ever_exceed_cargo_insurance_limit: str =""
        self.cargo_deductible: str =""
        self.radius_of_operations: str =""
        self.loading_screen = self.page.locator(".jss53")


    def fill_cargo_insured_info(self, params: CargoInsuredInformationParams):
        
        self.insured_name_input.fill(params.business_insured_name)
        self.check_loading()
        self.insured_entity_select.select_option(params.type_of_entity)
        self.check_loading()
        self.insured_email_input.fill(params.email_address)
        self.check_loading()         
        self.inured_phone_input.fill(params.phone_number)
        self.check_loading()
        self.insured_street_address_1_input.fill(params.address_street1)
        self.check_loading()            
        self.insured_street_address_2_input.fill(params.address_street2)
        self.check_loading()
        self.insured_city_input.fill(params.address_city)
        self.check_loading()
        self.insured_state_select.select_option(params.address_state)
        self.check_loading()
        self.insured_zip_input.fill(params.address_zip)
        self.check_loading()
        self.insured_is_new_venture_selection.select_option(params.new_venture)
        self.check_loading()
        self.insured_icc_input.fill(params.insured_ICC_docket_number_MC)
        self.check_loading()
        self.insured_are_filling_selection.select_option("None")
        self.check_loading()
        if self.insured_all_owned_units_selection.is_visible():
            self.insured_all_owned_units_selection.select_option(params.include_all_owned_operated_units)
            self.check_loading()
        self.insured_carrier_type_selection.select_option(params.type_of_company_carrier)
        self.check_loading()
        # if self.insured_own_goods_selection.is_visible():
        #     self.insured_own_goods_selection.select_option(params.goo)
        #     self.check_loading()
        # self.insured_garage_same_selection.select_option
        self.check_loading()
        self.insured_garaging_address1_input.fill(params.garaging_address_street1)
        self.check_loading()
        self.insured_garaging_address2_input.fill(params.garaging_address_street2)
        self.check_loading()
        self.insured_garaging_city_input.fill(params.garaging_address_city)
        self.check_loading()
        self.insured_garaging_state_selection.select_option(params.garaging_address_state)
        self.check_loading()
        self.insured_garaging_zip_input.fill(params.garaging_address_zip)
        self.check_loading()
        self.insured_garaging_secondary_selection.select_option("no")
        self.check_loading()
        
        expect(self.additional_insured_info_btn).to_be_visible()
        expect(self.additional_insured_info_btn).to_be_enabled()
        self.additional_insured_info_btn.click()

    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")