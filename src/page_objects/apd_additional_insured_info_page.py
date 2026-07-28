from playwright.sync_api import Page, expect, TimeoutError
from models.apd_additional_insured_info_params import APDAdditionalInsuredInformationParams

class APDAdditionalInsuredInformationPage:
    def __init__(self, page: Page):
        self.page = page
        self.has_applicant_ever_operated_under_different_name_select = self.page.locator("[id=\"cargo.insured.different_name\"]")
        self.does_applicant_have_other_carrier_operations_select = self.page.locator("[id=\"cargo.insured.other_ops\"]")
        self.does_insured_subcontract_to_other_parties_select = self.page.locator("[id=\"cargo.insured.has_subcon\"]")
        self.Subcontracting_basis_select = self.page.locator("[id=\"cargo.insured.subcon_lease\"]")
        self.subcontractors_responsible_for_cargo_loss_select = self.page.locator("[id=\"cargo.insured.subcon_insured\"]")
        self.maintains_copies_of_subcontractor_insurance_select = self.page.locator("[id=\"cargo.insured.subcon_forms\"]")
        self.is_the_owner_also_listed_as_driver_select = self.page.locator("[id=\"cargo.insured.owner_driver\"]")
        self.has_insured_had_coverage_in_the_last_3years_select = self.page.locator("[id=\"cargo.insured.has_prior_carrier\"]")
        self.prior_carrier_information_known_select = self.page.locator("[id=\"cargo.insured.pc_unknown\"]")
        self.any_insurer_canceled_non_renewed_in_last_3years_select = self.page.locator("[id=\"cargo.insured.non_renew\"]")
        self.insurance_placed_through_commonwealth_underwriters_select = self.page.locator("[id=\"cargo.insured.previous_customer\"]")
        self.prior_perils_form_select = self.page.locator("[id=\"cargo.insured.pc_form\"]")
        self.was_a_renewal_offer_made_select = self.page.locator("[id=\"cargo.insured.pc_renewal\"]")
        self.consecutive_coverage_greater_than_ot_equal_to_12months_select = self.page.locator("[id=\"cargo.insured.has_consecutive_coverage\"]")
        self.describe_other_operations_input = self.page.locator("[id=\"cargo.insured.other_operations\"]")
        self.non_renew_details_input = self.page.locator("[id=\"cargo.insured.non_renew_details\"]")
        self.prior_carrier_name_input = self.page.locator("[id=\"cargo.insured.pc_name\"]")
        self.prior_policy_premium_input = self.page.locator("[id=\"cargo.insured.pc_premium\"]")
        self.prior_policy_deductible_input = self.page.locator("[id=\"cargo.insured.pc_deductible\"]")
        self.prior_policy_limit_input = self.page.locator("[id=\"cargo.insured.pc_limit\"]")
        self.prior_policy_expiration_date_input = self.page.locator("[id=\"cargo.insured.pc_exp_date\"]")
        self.risk_info_btn = self.page.get_by_role("button", name="Risk Information")
        self.loading_screen = self.page.locator(".jss53")

    def fill_additional_insured_info(self, params: APDAdditionalInsuredInformationParams):
        self.has_applicant_ever_operated_under_different_name_select.select_option(params.has_applicant_ever_operated_under_different_name)
        self.check_loading()
        self.does_applicant_have_other_carrier_operations_select.select_option(params.does_applicant_have_other_carrier_operations)
        self.check_loading()
        if params.does_applicant_have_other_carrier_operations == "Yes":
            self.describe_other_operations_input.fill(params.describe_other_operations)
            self.check_loading()
        # self.does_insured_subcontract_to_other_parties_select.select_option(params.does_insured_subcontract_to_other_parties)
        # self.check_loading()         
        # if params.does_insured_subco]ntract_to_other_parties == "Yes":
        #     self.Subcontracting_basis_select.select_option(params.Subcontracting_basis)
        #     self.check_loading()
        #     self.subcontractors_responsible_for_cargo_loss_select.select_option(params.subcontractors_responsible_for_cargo_loss)
        #     self.check_loading()
        #     self.maintains_copies_of_subcontractor_insurance_select.select_option(params.subcontractors_responsible_for_cargo_loss)
        #     self.check_loading()      
        self.is_the_owner_also_listed_as_driver_select.select_option(params.is_the_owner_also_listed_as_driver)
        self.check_loading()
        self.has_insured_had_coverage_in_the_last_3years_select.select_option(params.has_insured_had_coverage_in_the_last_3years)
        self.check_loading()   
        self.insurance_placed_through_commonwealth_underwriters_select.select_option(params.insurance_placed_through_commonwealth_underwriters)
        self.check_loading()
        self.any_insurer_canceled_non_renewed_in_last_3years_select.select_option(params.any_insurer_canceled_non_renewed_in_last_3years)
        self.check_loading()      
        self.prior_carrier_information_known_select.select_option(params.prior_carrier_information_known)
        self.check_loading()
        if params.prior_carrier_information_known == "Yes":       
            self.prior_carrier_name_input.fill(params.prior_carrier_name)
            self.check_loading()
            self.prior_perils_form_select.select_option(params.prior_perils_form)
            self.check_loading()
            self.prior_policy_premium_input.fill(params.prior_policy_premium)
            self.check_loading()
            self.prior_policy_deductible_input.fill(params.prior_policy_deductible)
            self.check_loading()
            self.prior_policy_limit_input.fill(params.prior_policy_limit)
            self.check_loading()
            self.prior_policy_expiration_date_input.fill(params.prior_policy_expiration_date)
            self.check_loading()
            self.was_a_renewal_offer_made_select.select_option(params.was_a_renewal_offer_made)
            self.check_loading()
        self.consecutive_coverage_greater_than_ot_equal_to_12months_select.select_option(params.consecutive_coverage_greater_than_ot_equal_to_12months)
        self.check_loading()
        expect(self.risk_info_btn).to_be_visible()
        expect(self.risk_info_btn).to_be_enabled()
        self.risk_info_btn.click()

    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")