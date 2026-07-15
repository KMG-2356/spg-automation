import os

import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from config import *
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage
from page_objects.program_selection_page import ProgramSelectionPage
from page_objects.personal_line_basic_information_page import PersonalLinesBasicInformationPage
from page_objects.agency_information_page import AgencyInformationPage
from page_objects.location_page import LocationPage
from page_objects.insured_information_page import InsuredInformationPage
from page_objects.additional_questions_page import AdditionalQuestionPage
from page_objects.finance_quote_page import FinanceQuotePage
from page_objects.print_your_quote_page import PrintYourQuotePage
from models.agency_info_params import AgencyInfoParams
from models.insured_info_params import InsuredInfoParams


FEATURE_PATH = os.path.join(os.path.dirname(__file__), "..", "home_owners.feature")

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
    location_information_page = LocationPage(page)
    insured_information_page = InsuredInformationPage(page)
    additional_comments_page = AdditionalQuestionPage(page)
    finance_quote_page = FinanceQuotePage(page)

    agency_info = AgencyInfoParams(
        agency_name=test_data["01_Policy_Info"][0]["Agency Name"],
        agency_id_code=test_data["01_Policy_Info"][0]["Agency ID Code"],
        agent_full_name=test_data["01_Policy_Info"][0]["Agent Full Name"],
        agent_email=test_data["01_Policy_Info"][0]["Agent E-Mail"],
        agent_phone=test_data["01_Policy_Info"][0]["Agent Phone"],
        agent_fax=test_data["01_Policy_Info"][0]["Agent Fax"],
        agent_commission=str(test_data["01_Policy_Info"][0]["Agent's Commission %"]),
        address_street1=test_data["01_Policy_Info"][0]["Agency Address Street 1"],
        address_street2=test_data["01_Policy_Info"][0]["Agency Address Street 2"],
        city=test_data["01_Policy_Info"][0]["Agency Address City"],
        state=test_data["01_Policy_Info"][0]["Agency Address State"],
        zip_code=str(test_data["01_Policy_Info"][0]["Agency Address ZIP"])
    )

    insured_info = InsuredInfoParams(
        insured_full_name=test_data["01_Policy_Info"][0]["Insured Full Name"],
        insured_email=test_data["01_Policy_Info"][0]["Insured E-Mail"],
        insured_phone=str(test_data["01_Policy_Info"][0]["Insured Phone"]),
        insured_occupation=test_data["01_Policy_Info"][0]["Insured Occupation"],
        insured_employer=test_data["01_Policy_Info"][0]["Insured Employer"],
        mailing_street1=test_data["01_Policy_Info"][0]["Mailing Street 1"],
        mailing_street2=test_data["01_Policy_Info"][0]["Mailing Street 2"],
        mailing_zip=str(test_data["01_Policy_Info"][0]["Insured Address ZIP"]),
        mailing_city=test_data["01_Policy_Info"][0]["Insured Address City"],
        mailing_state=test_data["01_Policy_Info"][0]["Insured Address State"],
        type_of_entity=test_data["01_Policy_Info"][0]["Type of Entity"],
        
        additional_resident_or_spouse=test_data["01_Policy_Info"][0]["Additional Resident / Spouse?"],
        additional_resident_full_name=test_data["01_Policy_Info"][0]["Additional Resident Full Name"],
        additional_resident_occupation=test_data["01_Policy_Info"][0]["Additional Resident Occupation"],
        additional_resident_dob=str(test_data["01_Policy_Info"][0]["Additional Resident Date of Birth"]),
        additional_resident_employer=test_data["01_Policy_Info"][0]["Additional Resident Employer"],
        
        mailing_address_different=test_data["01_Policy_Info"][0]["Mailing Address Different from Insured?"],
        diff_mailing_zip=test_data["01_Policy_Info"][0]["Mailing ZIP"],
        diff_mailing_street1=test_data["01_Policy_Info"][0]["Mailing Street 1"],
        diff_mailing_street2=test_data["01_Policy_Info"][0]["Mailing Street 2"],
        diff_mailing_city=test_data["01_Policy_Info"][0]["Mailing City"],
        diff_mailing_state=test_data["01_Policy_Info"][0]["Mailing State"]
    )

    home_page.click_new_quote_button()
    program_selection_page.select_personal_lines_LOB()
    personal_lines_basic_information_page.fill_personal_line_basic_information_form(test_data)
    agency_information_page.fill_agency_information_form(agency_info)
    insured_information_page.fill_insured_information_form_for_ho(insured_info)
    # location_information_page.fill_location_information_form(test_data)
    # additional_comments_page.fill_additional_comments(test_data)
    # finance_quote_page.fill_finance_quote_form()


@then('the generated premium should be saved to excel')
def then_generated_premium_should_be_equal(page, test_data):
    print_your_quote_page = PrintYourQuotePage(page)
    print_your_quote_page.save_premium(test_data)
