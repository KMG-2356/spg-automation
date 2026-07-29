from playwright.sync_api import Page, expect, TimeoutError
from models.cargo_additional_insured_info_params import CargoAdditionalInsuredInformationParams

class CargoAdditionalInsuredInformationPage:
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
        self.insure_work_exp_input = self.page.locator("[id=\"cargo.insured.work_experience\"]")
        self.is_prior_empoyement_known_selection = self.page.locator("[id=\"cargo.insured.prior_employment_known\"]")


        self.add_another_empoyer_btn = self.page.get_by_role("button", name="Add Another Employer")
        self.risk_info_btn = self.page.get_by_role("button", name="Risk Information")
        self.loading_screen = self.page.locator(".jss53")
        
    def employer_name_input(self, i: int):
        return self.page.locator(f"[id=\"cargo.insured.employers.{i}.employer_name\"]")
    def employer_phone_input(self, i: int):
        return self.page.locator(f"[id=\"cargo.insured.employers.{i}.employer_phone\"]")
    def employer_start_date_input(self, i: int):
        return self.page.locator(f"[id=\"cargo.insured.employers.{i}.employer_start_date\"]")
    def employer_end_date_input(self, i: int):
        return self.page.locator(f"[id=\"cargo.insured.employers.{i}.employer_end_date\"]")
    def employer_unit_type_input(self, i: int):
        return self.page.locator(f"[id=\"cargo.insured.employers.{i}.employer_unit_type\"]")
    def employer_commodities_input(self, i: int):
        return self.page.locator(f"[id=\"cargo.insured.employers.{i}.employer_commodities\"]")
    def employer_radius_selection(self, i: int):
        return self.page.locator(f"[id=\"cargo.insured.employers.{i}.employer_radius\"]")
    def is_employer_info_verified_selection(self, i: int):
        return self.page.locator(f"[id=\"cargo.insured.employers.{i}.info_verified\"]")
    def employer_street1_input(self, i: int):
        return (self.page.locator("text=Employer Address").locator("..").locator("input").nth(i * 4))
    def employer_street2_input(self, i: int):
        return (self.page.locator("text=Employer Address").locator("..").locator("input").nth(i * 4 + 1))
    def employer_city_input(self, i: int):
        return (self.page.locator("text=Employer Address").locator("..").locator("input").nth(i * 4 + 2))
    def employer_zip_input(self, i: int):
        return (self.page.locator("text=Employer Address").locator("..").locator("input").nth(i * 4 + 3))
    def employer_state_selection(self, i: int):
        return (self.page.locator("text=Employer Address").locator("..").locator("select").nth(i))

    def fill_cargo_additional_insured_info(self, params: CargoAdditionalInsuredInformationParams):
        
        self.has_applicant_ever_operated_under_different_name_select.select_option(params.has_applicant_ever_operated_under_different_name)
        self.check_loading()
        self.does_applicant_have_other_carrier_operations_select.select_option(params.does_applicant_have_other_carrier_operations)
        self.check_loading()
        if params.does_applicant_have_other_carrier_operations == "Yes":
            self.describe_other_operations_input.fill(params.describe_other_operations)
            self.check_loading()
        self.does_insured_subcontract_to_other_parties_select.select_option(params.does_insured_subcontract_to_other_parties)
        self.check_loading()         
        if params.does_insured_subcontract_to_other_parties == "Yes":
            self.Subcontracting_basis_select.select_option(params.Subcontracting_basis)
            self.check_loading()
            self.subcontractors_responsible_for_cargo_loss_select.select_option(params.subcontractors_responsible_for_cargo_loss)
            self.check_loading()
            self.maintains_copies_of_subcontractor_insurance_select.select_option(params.subcontractors_responsible_for_cargo_loss)
            self.check_loading()      
        self.is_the_owner_also_listed_as_driver_select.select_option(params.is_the_owner_also_listed_as_driver)
        self.check_loading()
        self.has_insured_had_coverage_in_the_last_3years_select.select_option(params.has_insured_had_coverage_in_the_last_3years)
        self.check_loading()   
        self.insurance_placed_through_commonwealth_underwriters_select.select_option(params.insurance_placed_through_commonwealth_underwriters)
        self.check_loading()   
        if self.prior_carrier_information_known_select.is_visible():
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
        if self.non_renew_details_input.is_visible():
            self.non_renew_details_input.fill(params.details_for_reasons_of_non_renewal)
        if self.consecutive_coverage_greater_than_ot_equal_to_12months_select.is_visible():
            self.consecutive_coverage_greater_than_ot_equal_to_12months_select.select_option(params.consecutive_coverage_greater_than_ot_equal_to_12months)
            self.check_loading()
        if self.is_prior_empoyement_known_selection.is_visible():
           self.is_prior_empoyement_known_selection.select_option(params.prior_employment_information_known)
           if params.prior_employment_information_known == "Yes":            
            for i, employer in enumerate(params.employers):
                if i > 0:
                    self.add_another_empoyer_btn.click()
                    self.check_loading()
                self.employer_name_input(i).fill(employer.employer_name)
                self.check_loading()
                self.employer_phone_input(i).fill(employer.phone)
                self.check_loading()
                self.employer_start_date_input(i).fill(employer.start_date)
                self.check_loading()
                self.employer_end_date_input(i).fill(employer.end_date)
                self.check_loading()
                self.employer_unit_type_input(i).fill(employer.unit_type_operated)
                self.check_loading()
                self.employer_commodities_input(i).fill(employer.commodities_hauled)
                self.check_loading()
                self.employer_radius_selection(i).select_option(employer.radius)
                self.check_loading()
                self.is_employer_info_verified_selection(i).select_option(employer.object_to_verification)
                self.check_loading()
                self.employer_street1_input(i).fill(employer.street1)
                self.check_loading()
                # self.employer_street2_input(i).fill(employer.street2)
                # self.check_loading()
                self.employer_city_input(i).fill(employer.city)
                self.check_loading()
                self.employer_state_selection(i).select_option(employer.state)
                self.check_loading()
                self.employer_zip_input(i).fill(employer.zip_code)
            self.check_loading()
        if self.insure_work_exp_input.is_visible():
            self.insure_work_exp_input.fill(params.years_of_experience_same_type_of_work)
        if self.any_insurer_canceled_non_renewed_in_last_3years_select.is_visible():
            self.any_insurer_canceled_non_renewed_in_last_3years_select.select_option(params.any_insurer_canceled_non_renewed_in_last_3years)
        expect(self.risk_info_btn).to_be_visible()
        expect(self.risk_info_btn).to_be_enabled()
        self.risk_info_btn.click()

    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")

    
   




