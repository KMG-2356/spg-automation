import os
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from config import *
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage
from page_objects.program_selection_page import ProgramSelectionPage
from page_objects.personal_line_basic_information_page import PersonalLinesBasicInformationPage
from page_objects.commercial_lines_basic_information_page import CommercialLinesBasicInformationPage
from page_objects.agency_information_page import AgencyInformationPage
from page_objects.cargo_additional_insured_info_page import CargoAdditionalInsuredInformationPage
from page_objects.cargo_insured_info_page import CargoInsuredInformationPage

from page_objects.finance_quote_page import FinanceQuotePage
from page_objects.print_your_quote_page import PrintYourQuotePage

from models.agency_info_params import AgencyInfoParams
from models.cargo_insured_info_params import CargoInsuredInformationParams
from models.cargo_additional_insured_info_params import CargoAdditionalInsuredInformationParams
from models.DF_location_params import DFlocationParams
from models.DF_coverage_params import DFcoverageParams
from models.DF_additional_questions_params import DFadditionalQuestionsParams
from models.DF_applicant_info_params import DFapplicantInfoParams
from models.DF_loss_payee_params import DFlossPayeeParams


FEATURE_PATH = os.path.join(os.path.dirname(__file__), "..", "cargo_coverage.feature")

scenarios(FEATURE_PATH)

@pytest.fixture
def login_page(page):
    return LoginPage(page)


@given('the login page is open')
def given_login_page_open(login_page, base_url):
    login_page.navigate(base_url)
    login_page.login(USERNAME, PASSWORD)


@when('the user generates a premium')
def when_user_generates_premium(page, test_data):
    home_page = HomePage(page)
    program_selection_page = ProgramSelectionPage(page)
    commercial_line_basic_info_page = CommercialLinesBasicInformationPage(page)
    agency_information_page = AgencyInformationPage(page)
    cargo_additional_insured_info_page = CargoAdditionalInsuredInformationPage(page)
    insured_information_page = CargoInsuredInformationPage(page)
    # finance_quote_page = FinanceQuotePage(page)
    # df_loss_history_page = DFLossHistoryPage(page)
    # df_coverage_page = DFCoveragesPage(page)
    # df_applicant_info_page = DFApplicantInfoPage(page)
    # df_additional_questions_page = DFAdditionalQusetionsPage(page)
    # df_loss_payee_page = DFLossPayeePage(page)

    agency_info = AgencyInfoParams(
        agency_name=test_data["01_Policy_Info"][0]["Agency Name"],
        agency_id_code=test_data["01_Policy_Info"][0]["Agency ID Code"],
        agent_full_name=test_data["01_Policy_Info"][0]["Agent's Full Name"],
        agent_email=test_data["01_Policy_Info"][0]["Agent E-Mail"],
        agent_phone=test_data["01_Policy_Info"][0]["Agent Phone"],
        agent_fax=test_data["01_Policy_Info"][0]["Agent Fax"],
        agent_commission=str(test_data["01_Policy_Info"][0]["Agent's Commission"]),
        address_street1=test_data["01_Policy_Info"][0]["Agent Address Street 1"],
        address_street2=test_data["01_Policy_Info"][0]["Agent Address Street 2"],
        city=test_data["01_Policy_Info"][0]["Agent Address City"],
        state=test_data["01_Policy_Info"][0]["Agent Address State"],
        zip_code=str(test_data["01_Policy_Info"][0]["Agent Address Zip"])
    )                                                

    insured_info = CargoInsuredInformationParams(
        business_insured_name=test_data["01_Policy_Info"][0]["Business / Insured Name"],
        type_of_entity=test_data["01_Policy_Info"][0]["Type of Entity"],
        email_address=test_data["01_Policy_Info"][0]["Email Address"],
        phone_number=str(test_data["01_Policy_Info"][0]["Phone Number"]),
        address_street1=test_data["01_Policy_Info"][0]["Address  -  Street 1"],
        address_street2=test_data["01_Policy_Info"][0]["Address  -  Street 2"],
        address_city=test_data["01_Policy_Info"][0]["Address  -  City"],
        address_state=test_data["01_Policy_Info"][0]["Address  -  State"],
        address_zip=test_data["01_Policy_Info"][0]["Address  -  Zip"],
        new_venture=test_data["01_Policy_Info"][0]["New Venture"],
        insured_ICC_docket_number_MC=test_data["01_Policy_Info"][0]["Insured ICC Docket Number - MC#"],
        filings_required=test_data["01_Policy_Info"][0]["Filings Required"],
        # include_all_owned_operated_units=test_data["Policy_Info"][0]["Additional Resident / Spouse?"],
        type_of_company_carrier=test_data["01_Policy_Info"][0]["Type of Company / Carrier"],
        garaging_address_street1=test_data["01_Policy_Info"][0]["Garaging Address Street 1"],
        garaging_address_street2=test_data["01_Policy_Info"][0]["Garaging Address Street 2"],
        garaging_address_city=test_data["01_Policy_Info"][0]["Garaging Address City"],
        garaging_address_state=test_data["01_Policy_Info"][0]["Garaging Address State"],
        garaging_address_zip=test_data["01_Policy_Info"][0]["Garaging Address Zip"],
    )
    cargo_additional_insured_info = CargoAdditionalInsuredInformationParams(
        has_applicant_ever_operated_under_different_name=test_data["02_Cargo_Additional_Insured_UW"][0]["Has applicant ever operated under a different name?"],
        does_applicant_have_other_carrier_operations=test_data["02_Cargo_Additional_Insured_UW"][0]["Does applicant have other carrier operations?"],
        describe_other_operations=test_data["02_Cargo_Additional_Insured_UW"][0]["Describe other operations"],
        does_insured_subcontract_to_other_parties=test_data["02_Cargo_Additional_Insured_UW"][0]["Does insured subcontract to other parties?"],
        Subcontracting_basis=test_data["02_Cargo_Additional_Insured_UW"][0]["Subcontracting basis"],
        subcontractors_responsible_for_cargo_loss=test_data["02_Cargo_Additional_Insured_UW"][0]["Subcontractors responsible for cargo loss?"],
        maintains_copies_of_subcontractor_insurance=test_data["02_Cargo_Additional_Insured_UW"][0]["Maintains copies of subcontractor insurance?"],
        is_the_owner_also_listed_as_driver=test_data["02_Cargo_Additional_Insured_UW"][0]["Is the owner also listed as a driver?"],
        has_insured_had_coverage_in_the_last_3years=test_data["02_Cargo_Additional_Insured_UW"][0]["Has insured had coverage in the last 3 years?"],
        insurance_placed_through_commonwealth_underwriters=test_data["02_Cargo_Additional_Insured_UW"][0]["Insurance placed through Commonwealth Underwriters?"],
        any_insurer_canceled_non_renewed_in_last_3years=test_data["02_Cargo_Additional_Insured_UW"][0]["Any insurer canceled / non-renewed in last 3 years?"],
        prior_carrier_information_known=test_data["02_Cargo_Additional_Insured_UW"][0]["Prior carrier information known?"],
        prior_carrier_name=test_data["02_Cargo_Additional_Insured_UW"][0]["Prior carrier name"],
        prior_perils_form=test_data["02_Cargo_Additional_Insured_UW"][0]["Prior perils form"],
        prior_policy_premium=test_data["02_Cargo_Additional_Insured_UW"][0]["Prior policy premium ($)"],
        prior_policy_deductible=test_data["02_Cargo_Additional_Insured_UW"][0]["Prior policy deductible ($)"],
        prior_policy_limit=test_data["02_Cargo_Additional_Insured_UW"][0]["Prior policy limit ($)"],
        prior_policy_expiration_date=test_data["02_Cargo_Additional_Insured_UW"][0]["Prior policy expiration date"],
        was_a_renewal_offer_made=test_data["02_Cargo_Additional_Insured_UW"][0]["Was a renewal offer made?"],
        consecutive_coverage_greater_than_ot_equal_to_12months=test_data["02_Cargo_Additional_Insured_UW"][0]["Consecutive coverage >= 12 months?"],
)
    # location_info = DFlocationParams(
    #      locations=test_data["DF_Locations"]
    # )
    # loss_payee_info = DFlossPayeeParams(
    #      loss_payee=test_data["DF_LossPayees"]
    # )

    # loss_history_info = DFLossHistoryParams(
    #     any_open_claims=test_data["DF_LossHistory"][0]["Any Open Claims?"],
    #     has_loss=test_data["DF_LossHistory"][0]["Any Losses in Past 5 Years?"],
    #     unrepairedDamage=test_data["DF_LossHistory"][0]["Unrepaired Damage from Prior Losses?"],
    #     losses=test_data["HO_LossHistory"]
    # )

    # applicant_info = DFapplicantInfoParams(
    #         insured_credit_history = test_data["DF_Policy"][0]["Insured Credit History"],
    #         Any_Arson_Fraud_convictions = test_data["DF_Policy"][0]["Any Arson / Fraud Convictions?"],
    #         Bankruptcy_Last_Year = test_data["DF_Policy"][0]["Bankruptcy in Last Year?"],
    #         Foreclosure_Last_5Years = test_data["DF_Policy"][0]["Foreclosure in Last 5 Years?"],
    #         AnyPast_Due_Child_Support = test_data["DF_Policy"][0]["Any Past Due Child Support?"],
    #         Repossessions_Last_3Years = test_data["DF_Policy"][0]["Repossessions in Last 3 Years?"],
    #         Prior_Insuranceon_This_Account = test_data["DF_Policy"][0]["Prior Insurance on This Account?"],
    #         Prior_CarrierName = test_data["DF_Policy"][0]["Prior Carrier Name"],
    #         Expiration_Date_of_Prior_Insurance = test_data["DF_Policy"][0]["Expiration Date of Prior Insurance"],
    #         Prior_Policy_Number = test_data["DF_Policy"][0]["Prior Policy Number"],
    #         Prior_Insurance_Premium = test_data["DF_Policy"][0]["Prior Insurance Premium ($)"],
    #         Risk_New_to_Agency = test_data["DF_Policy"][0]["Risk New to Agency?"],
    #         Lapse_30_Days = test_data["DF_Policy"][0]["Lapse > 30 Days?"],
    #         Terminate_at_Company_Request = test_data["DF_Policy"][0]["Terminated at Company Request?"],
    #         Reason_for_Termination = test_data["DF_Policy"][0]["Reason for Termination"],
    #         Previous_WindHail_Dedductible = test_data["DF_Policy"][0]["Previous Wind / Hail Deductible"],
                             
    # )


    # coverages_info = DFcoverageParams(
    #         Coverage_E_L_Limitof_Liability = test_data["DF_Coverages"][0]["Coverage E / L — Limit of Liability"],
    #         Loss_of_Rents_CoverageD = test_data["DF_Coverages"][0]["Loss of Rents — Coverage D ($)"],
    #         Owners_Contents_CoverageC = test_data["DF_Coverages"][0]["Owners Contents — Coverage C ($)"],
    #         Owners_Contents_Burglary_Coverage = test_data["DF_Coverages"][0]["Owners Contents Burglary Coverage"],
    #         Home_Systems_Protection = test_data["DF_Coverages"][0]["Home Systems Protection?"],
    #         Service_Line_Coverage = test_data["DF_Coverages"][0]["Service Line Coverage?"],
    #         Identity_Theft_Coverage = test_data["DF_Coverages"][0]["Identity Theft Coverage?"],
            
    # )

    # additional_questions_info = DFadditionalQuestionsParams(
    #         higher_deductible_AOP = test_data["DF_Coverages"][0]["Higher Deductible (AOP)"],
    #         central_station_alarms = test_data["DF_Coverages"][0]["Central Station Alarms?"],
    #         roof_valuation_endorsement = test_data["DF_Coverages"][0]["Roof Valuation Endorsement"],
    #         additional_comments = test_data["DF_Coverages"][0]["Additional Comments"],

    # )

    home_page.click_new_quote_button()
    program_selection_page.select_commercial_lines_LOB()
    commercial_line_basic_info_page.fill_commercial_line_basic_information_form(test_data)
    agency_information_page.fill_agency_information_form(agency_info)
    insured_information_page.fill_cargo_insured_info(insured_info)
    cargo_additional_insured_info_page.fill_cargo_additional_insured_info(cargo_additional_insured_info)
    # location_information_page.fill_df_location_information(location_info)
    # df_loss_payee_page.fill_df_loss_payee_information(loss_payee_info)
    # df_applicant_info_page.fill_applicant_info(applicant_info)
    # df_loss_history_page.fill_loss_history(loss_history_info)
    # df_coverage_page.fill_DFcoverages_info(coverages_info)
    # df_additional_questions_page.fill_DF_additional_questions_info(additional_questions_info)
    # finance_quote_page.fill_finance_quote_form()


@then('the generated premium should be saved to excel')
def then_generated_premium_should_be_equal(page, test_data):
    print_your_quote_page = PrintYourQuotePage(page)
    print_your_quote_page.save_premium(test_data, "ho_output")
