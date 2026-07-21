import os
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from config import *
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage
from page_objects.program_selection_page import ProgramSelectionPage
from page_objects.personal_line_basic_information_page import PersonalLinesBasicInformationPage
from page_objects.agency_information_page import AgencyInformationPage
from page_objects.DF_locations_page import DFLocationPage
from page_objects.DF_insured_info_page import DFInsuredInformationPage
from page_objects.finance_quote_page import FinanceQuotePage
from page_objects.print_your_quote_page import PrintYourQuotePage
from page_objects.DF_loss_history_page import DFLossHistoryPage
from page_objects.DF_coverages_page import DFCoveragesPage
from page_objects.DF_loss_payee_page import DFLossPayeePage
from page_objects.DF_additional_questions_page import DFAdditionalQusetionsPage
from page_objects.DF_Applicant_Info_page import DFApplicantInfoPage
from models.agency_info_params import AgencyInfoParams
from models.DF_insured_info_params import DFinsuredInfoParams
from models.DF_loss_history_params import DFLossHistoryParams
from models.DF_location_params import DFlocationParams
from models.DF_coverage_params import DFcoverageParams
from models.DF_additional_questions_params import DFadditionalQuestionsParams
from models.DF_applicant_info_params import DFapplicantInfoParams
from models.DF_loss_payee_params import DFlossPayeeParams


FEATURE_PATH = os.path.join(os.path.dirname(__file__), "..", "dwelling_fire.feature")

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
    personal_lines_basic_information_page = PersonalLinesBasicInformationPage(page)
    agency_information_page = AgencyInformationPage(page)
    location_information_page = DFLocationPage(page)
    insured_information_page = DFInsuredInformationPage(page)
    finance_quote_page = FinanceQuotePage(page)
    df_loss_history_page = DFLossHistoryPage(page)
    df_coverage_page = DFCoveragesPage(page)
    df_applicant_info_page = DFApplicantInfoPage(page)
    df_additional_questions_page = DFAdditionalQusetionsPage(page)
    df_loss_payee_page = DFLossPayeePage(page)

    agency_info = AgencyInfoParams(
        agency_name=test_data["Policy_Info"][0]["Agency Name"],
        agency_id_code=test_data["Policy_Info"][0]["Agency ID Code"],
        agent_full_name=test_data["Policy_Info"][0]["Agent Full Name"],
        agent_email=test_data["Policy_Info"][0]["Agent E-Mail"],
        agent_phone=test_data["Policy_Info"][0]["Agent Phone"],
        agent_fax=test_data["Policy_Info"][0]["Agent Fax"],
        agent_commission=str(test_data["Policy_Info"][0]["Agent Commission"]),
        address_street1=test_data["Policy_Info"][0]["Agency Address Street 1"],
        address_street2=test_data["Policy_Info"][0]["Agency Address Street 2"],
        city=test_data["Policy_Info"][0]["Agency Address City"],
        state=test_data["Policy_Info"][0]["Agency Address State"],
        zip_code=str(test_data["Policy_Info"][0]["Agency Address ZIP"])
    )

    insured_info = DFinsuredInfoParams(
        insured_full_name=test_data["Policy_Info"][0]["Insured Full Name"],
        type_of_entity=test_data["Policy_Info"][0]["Type of Entity"],
        insured_email=test_data["Policy_Info"][0]["Insured E-Mail"],
        insured_phone=str(test_data["Policy_Info"][0]["Insured Phone"]),
        insured_occupation=test_data["Policy_Info"][0]["Insured Occupation"],
        insured_employer=test_data["Policy_Info"][0]["Insured Employer"],
        insured_dob=test_data["Policy_Info"][0]["Insured Date of Birth"],
        additional_resident_or_spouse=test_data["Policy_Info"][0]["Additional Resident / Spouse?"],
        additional_resident_full_name=test_data["Policy_Info"][0]["Additional Resident Full Name"],
        additional_resident_occupation=test_data["Policy_Info"][0]["Additional Resident Occupation"],
        additional_resident_dob=test_data["Policy_Info"][0]["Additional Resident Date of Birth"],
        addition_resident_employer=test_data["Policy_Info"][0]["Additional Resident Employer"],
        insured_address_street1=test_data["Policy_Info"][0]["Insured Address Street 1"],
        insured_address_street2=test_data["Policy_Info"][0]["Insured Address Street 2"],
        insured_address_city=test_data["Policy_Info"][0]["Insured Address City"],
        insured_address_state=test_data["Policy_Info"][0]["Insured Address State"],
        insured_address_zip=test_data["Policy_Info"][0]["Insured Address ZIP"],
        # mailing_street1=test_data["Policy_Info"][0]["Mailing Street 1"],
        # mailing_street2=test_data["Policy_Info"][0]["Mailing Street 2"],
        # mailing_zip=str(test_data["Policy_Info"][0]["Mailing ZIP"]),
        # mailing_city=test_data["Policy_Info"][0]["Insured Address City"],
        # mailing_state=test_data["Policy_Info"][0]["Insured Address State"],
        
        
    )
    
    location_info = DFlocationParams(
         locations=test_data["DF_Locations"]
    )
    loss_payee_info = DFlossPayeeParams(
         loss_payee=test_data["DF_LossPayees"]
    )

    loss_history_info = DFLossHistoryParams(
        any_open_claims=test_data["DF_LossHistory"][0]["Any Open Claims?"],
        has_loss=test_data["DF_LossHistory"][0]["Any Losses in Past 5 Years?"],
        unrepairedDamage=test_data["DF_LossHistory"][0]["Unrepaired Damage from Prior Losses?"],
        losses=test_data["HO_LossHistory"]
    )

    applicant_info = DFapplicantInfoParams(
            insured_credit_history = test_data["DF_Policy"][0]["Insured Credit History"],
            Any_Arson_Fraud_convictions = test_data["DF_Policy"][0]["Any Arson / Fraud Convictions?"],
            Bankruptcy_Last_Year = test_data["DF_Policy"][0]["Bankruptcy in Last Year?"],
            Foreclosure_Last_5Years = test_data["DF_Policy"][0]["Foreclosure in Last 5 Years?"],
            AnyPast_Due_Child_Support = test_data["DF_Policy"][0]["Any Past Due Child Support?"],
            Repossessions_Last_3Years = test_data["DF_Policy"][0]["Repossessions in Last 3 Years?"],
            Prior_Insuranceon_This_Account = test_data["DF_Policy"][0]["Prior Insurance on This Account?"],
            Prior_CarrierName = test_data["DF_Policy"][0]["Prior Carrier Name"],
            Expiration_Date_of_Prior_Insurance = test_data["DF_Policy"][0]["Expiration Date of Prior Insurance"],
            Prior_Policy_Number = test_data["DF_Policy"][0]["Prior Policy Number"],
            Prior_Insurance_Premium = test_data["DF_Policy"][0]["Prior Insurance Premium ($)"],
            Risk_New_to_Agency = test_data["DF_Policy"][0]["Risk New to Agency?"],
            Lapse_30_Days = test_data["DF_Policy"][0]["Lapse > 30 Days?"],
            Terminate_at_Company_Request = test_data["DF_Policy"][0]["Terminated at Company Request?"],
            Reason_for_Termination = test_data["DF_Policy"][0]["Reason for Termination"],
            Previous_WindHail_Dedductible = test_data["DF_Policy"][0]["Previous Wind / Hail Deductible"],
                             
    )


    coverages_info = DFcoverageParams(
            Coverage_E_L_Limitof_Liability = test_data["DF_Coverages"][0]["Coverage E / L — Limit of Liability"],
            Loss_of_Rents_CoverageD = test_data["DF_Coverages"][0]["Loss of Rents — Coverage D ($)"],
            Owners_Contents_CoverageC = test_data["DF_Coverages"][0]["Owners Contents — Coverage C ($)"],
            Owners_Contents_Burglary_Coverage = test_data["DF_Coverages"][0]["Owners Contents Burglary Coverage"],
            Home_Systems_Protection = test_data["DF_Coverages"][0]["Home Systems Protection?"],
            Service_Line_Coverage = test_data["DF_Coverages"][0]["Service Line Coverage?"],
            Identity_Theft_Coverage = test_data["DF_Coverages"][0]["Identity Theft Coverage?"],
            
    )

    additional_questions_info = DFadditionalQuestionsParams(
            higher_deductible_AOP = test_data["DF_Coverages"][0]["Higher Deductible (AOP)"],
            central_station_alarms = test_data["DF_Coverages"][0]["Central Station Alarms?"],
            roof_valuation_endorsement = test_data["DF_Coverages"][0]["Roof Valuation Endorsement"],
            additional_comments = test_data["DF_Coverages"][0]["Additional Comments"],

    )

    home_page.click_new_quote_button()
    program_selection_page.select_personal_lines_LOB()
    personal_lines_basic_information_page.fill_personal_line_basic_information_form(test_data)
    agency_information_page.fill_agency_information_form(agency_info)
    insured_information_page.fill_DF_insured_info(insured_info)
    location_information_page.fill_df_location_information(location_info)
    df_loss_payee_page.fill_df_loss_payee_information(loss_payee_info)
    df_applicant_info_page.fill_applicant_info(applicant_info)
    df_loss_history_page.fill_loss_history(loss_history_info)
    df_coverage_page.fill_DFcoverages_info(coverages_info)
    df_additional_questions_page.fill_DF_additional_questions_info(additional_questions_info)
    finance_quote_page.fill_finance_quote_form()


@then('the generated premium should be saved to excel')
def then_generated_premium_should_be_equal(page, test_data):
    print_your_quote_page = PrintYourQuotePage(page)
    print_your_quote_page.save_premium(test_data, "ho_output")
