from playwright.sync_api import Page, expect, TimeoutError
from models.DF_applicant_info_params import DFapplicantInfoParams

class DFApplicantInfoPage:
    def __init__(self, page: Page):
        self.page = page

        self.insured_credit_history_select = self.page.locator("[id=\"df.applicant.df_credit_history\"]")
        self.any_arson_fraud_conviction_select = self.page.locator("[id=\"df.applicant.df_arson_and_fraud_conviction\"]")
        self.bankruptcy_in_last_year_select = self.page.locator("[id=\"df.applicant.df_bankruptcy\"]")
        self.foreclosure_in_last_5_years_select = self.page.locator("[id=\"df.applicant.df_foreclosure\"]")
        self.any_past_due_child_support_select = self.page.locator("[id=\"df.applicant.df_child_support\"]")
        self.repossessions_in_3_years_select = self.page.locator("[id=\"df.applicant.df_repossessions\"]")
        self.prior_insurance_on_this_account_select = self.page.locator("[id=\"df.applicant.df_prior_insurance\"]")
        self.prior_carrier_name_name_input = self.page.locator("[id=\"df.applicant.df_prior_carrier\"]")
        self.prior_insurance_date_input = self.page.locator("[id=\"df.applicant.df_previous_expiration\"]")
        self.prior_policy_number_input = self.page.locator("[id=\"df.applicant.df_previous_policy\"]")
        self.prior_insurance_premium_input = self.page.locator("[id=\"df.applicant.df_prior_premium\"]")
        self.risk_new_to_agency_select = self.page.locator("[id=\"df.applicant.df_new_agency\"]")
        self.lapse_30_days_select = self.page.locator("[id=\"df.applicant.df_lapse_of_coverage\"]")
        self.policy_terminated_at_company_request_select = self.page.locator("[id=\"df.applicant.df_termination_at_companies_request\"]")
        self.previous_wind_hail_deductible_select = self.page.locator("[id=\"df.applicant.df_previous_wind_hail\"]")
        self.reason_for_termination_select = self.page.locator("[id=\"df.applicant.df_reason_for_termination\"]")
        self.loading_screen = self.page.locator(".jss53")

        self.dwelling_fire_loss_history_btn = self.page.get_by_role("button", name="Dwelling Fire Loss History")

    def fill_applicant_info(self, params: DFapplicantInfoParams):

        self.insured_credit_history_select.select_option(params.InsuredCreditHistory)
        self.check_loading()
        self.any_arson_fraud_conviction_select.select_option(params.AnyArsonFraudConvictions)
        self.check_loading()
        self.bankruptcy_in_last_year_select.select_option(params.BankruptcyLastYear)
        self.check_loading()        
        self.foreclosure_in_last_5_years_select.select_option(params.ForeclosureLast5Years)
        self.check_loading()
        self.any_past_due_child_support_select.select_option(params.AnyPastDueChildSupport)
        self.check_loading()            
        self.repossessions_in_3_years_select.select_option(params.RepossessionsLast3Years)
        self.check_loading()
        self.prior_insurance_on_this_account_select.select_option(params.PriorInsuranceonThisAccount)
        self.check_loading()
        if params.PriorInsuranceonThisAccount == "Yes":

            self.prior_carrier_name_name_input.fill(params.PriorCarrierName)
            self.check_loading()
            self.prior_insurance_date_input.fill(params.ExpirationDateofPriorInsurance)
            self.check_loading()
            self.prior_policy_number_input.fill(params.PriorPolicyNumber)
            self.check_loading()
            self.prior_insurance_premium_input.fill(params.PriorInsurancePremium)
            self.check_loading()
            self.risk_new_to_agency_select.select_option(params.RiskNewtoAgency)
            self.check_loading()
            self.lapse_30_days_select.select_option(params.Lapse30Days)
            self.check_loading()
            self.policy_terminated_at_company_request_select.select_option(params.TerminatedatCompanyRequest)
            self.check_loading()
            self.previous_wind_hail_deductible_select.select_option(params.PreviousWindHailDedductible)
            self.check_loading()
            self.reason_for_termination_select.select_option(params.ReasonforTermination)
            self.check_loading()

        expect(self.dwelling_fire_loss_history_btn_btn).to_be_visible()
        expect(self.dwelling_fire_loss_history_btn_btn).to_be_enabled()
        self.dwelling_fire_loss_history_btn.click()

    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")