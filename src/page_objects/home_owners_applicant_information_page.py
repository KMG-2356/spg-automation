from playwright.sync_api import Page, expect
from models.home_owners_applicant_info_params import HomeOwnersApplicantInfoParams

class HomeOwnerApplicantInformationPage:
    def __init__(self, page: Page):
        self.page = page
        self.protection_class_select = self.page.locator("[id=\"ho.dwelling.protection_class\"]")
        self.adequate_water_select = self.page.locator("[id=\"ho.dwelling.adequate_water\"]")
        self.response_time_select = self.page.locator("[id=\"ho.dwelling.response_time\"]")
        self.accessible_property_select = self.page.locator("[id=\"ho.dwelling.accessible_property\"]")
        self.single_family_select = self.page.locator("[id=\"ho.dwelling.single_family\"]")
        self.owner_occupied_select = self.page.locator("[id=\"ho.dwelling.owner_occupied\"]")
        self.dwelling_type_select = self.page.locator("[id=\"ho.dwelling.dwelling_type\"]")
        self.manufactured_home_select = self.page.locator("[id=\"ho.dwelling.manufactured_home\"]")
        self.prior_insurance_select = self.page.locator("[id=\"ho.applicant.prior_insurance\"]")
        self.prior_commonwealth_select = self.page.locator("[id=\"ho.applicant.prior_commonwealth\"]")
        self.new_agency_select = self.page.locator("[id=\"ho.applicant.new_agency\"]")
        self.lapse_of_coverage_select = self.page.locator("[id=\"ho.applicant.lapse_of_coverage\"]")
        self.termination_at_companies_request_select = self.page.locator("[id=\"ho.applicant.termination_at_companies_request\"]")
        self.reason_for_termination_select = self.page.locator("[id=\"ho.applicant.reason_for_termination\"]")
        self.previous_wind_hail_select = self.page.locator("[id=\"ho.applicant.previous_wind_hail\"]")
        self.credit_history_select = self.page.locator("[id=\"ho.applicant.credit_history\"]")
        self.arson_and_fraud_conviction_select = self.page.locator("[id=\"ho.applicant.arson_and_fraud_conviction\"]")
        self.bankruptcy_select = self.page.locator("[id=\"ho.applicant.bankruptcy\"]")
        self.foreclosure_select = self.page.locator("[id=\"ho.applicant.foreclosure\"]")
        self.child_support_select = self.page.locator("[id=\"ho.applicant.child_support\"]")
        self.repossessions_select = self.page.locator("[id=\"ho.applicant.repossessions\"]")
        self.new_purchase_select = self.page.locator("[id=\"ho.applicant.new_purchase\"]")
        self.prior_foreclosure_select = self.page.locator("[id=\"ho.applicant.prior_foreclosure\"]")

        # --- Input Elements ---
        self.year_purchased_input = self.page.locator("[id=\"ho.applicant.year_purchased\"]")
        self.purchase_price_input = self.page.locator("[id=\"ho.applicant.purchase_price\"]")
        self.prior_carrier_input = self.page.locator("[id=\"ho.applicant.prior_carrier\"]")
        self.previous_expiration_input = self.page.locator("[id=\"ho.applicant.previous_expiration\"]")
        self.prior_premium_input = self.page.locator("[id=\"ho.applicant.prior_premium\"]")

        # --- Button Elements (Examples) ---
        # Added these based on your convention request for when you need action buttons
        self.submit_btn = self.page.locator("button[type=\"submit\"]")
        self.add_loss_payee_btn = self.page.locator("button:has-text(\"Add Loss Payee\")")


    def fill_applicant_info(self, params: HomeOwnersApplicantInfoParams):

        self.credit_history_select.select_option(params.credit_history)
        self.arson_and_fraud_conviction_select.select_option(params.arson_and_fraud)
        self.bankruptcy_select.select_option(params.bankruptcy)
        self.foreclosure_select.select_option(params.foreclosure)
        self.child_support_select.select_option(params.child_support)
        self.repossessions_select.select_option(params.repossessions)
        
        self.new_purchase_select.select_option(params.new_purchase)
        self.year_purchased_input.fill(str(params.year_purchased))
        
        self.prior_foreclosure_select.select_option(params.prior_foreclosure)
        
        self.purchase_price_input.click()
        self.purchase_price_input.fill(str(params.purchase_price))
        
        self.prior_insurance_select.select_option(params.prior_insurance)
        self.prior_commonwealth_select.select_option(params.prior_commonwealth)
        
        self.prior_carrier_input.fill(params.prior_carrier)
        
        self.previous_expiration_input.fill(params.previous_expiration)
        
        self.prior_premium_input.fill(str(params.prior_premium))
        
        self.new_agency_select.select_option(params.new_agency)
        self.lapse_of_coverage_select.select_option(params.lapse_of_coverage)
        self.termination_at_companies_request_select.select_option(params.termination_at_companies_request)
        self.reason_for_termination_select.select_option(params.reason_for_termination)
        self.previous_wind_hail_select.select_option(params.previous_wind_hail)

        self.page.pause()
        
