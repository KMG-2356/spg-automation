import os

import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from config import *
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage
from page_objects.program_selection_page import ProgramSelectionPage
from page_objects.commercial_lines_basic_information_page import CommercialLinesBasicInformationPage
from page_objects.agency_information_page import AgencyInformationPage
from page_objects.location_page import LocationPage
from page_objects.insured_information_page import InsuredInformationPage
from page_objects.additional_questions_page import AdditionalQuestionPage
from page_objects.finance_quote_page import FinanceQuotePage
from page_objects.print_your_quote_page import PrintYourQuotePage
from models.agency_info_params import AgencyInfoParams


FEATURE_PATH = os.path.join(os.path.dirname(__file__), "..", "windhail.feature")

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
    commercial_lines_basic_information_page = CommercialLinesBasicInformationPage(page)
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
        address_street1=test_data["01_Policy_Info"][0]["Address - Street 1"],
        address_street2=test_data["01_Policy_Info"][0]["Address - Street 2"],
        city=test_data["01_Policy_Info"][0]["Address - City"],
        state=test_data["01_Policy_Info"][0]["Address - State"],
        zip_code=str(test_data["01_Policy_Info"][0]["Address - Zip"])
    )


    home_page.click_new_quote_button()
    program_selection_page.select_monoline_wind_LOB()
    commercial_lines_basic_information_page.fill_commercial_line_basic_information_form()
    agency_information_page.fill_agency_information_form(agency_info)
    insured_information_page.fill_insured_information_form(test_data)
    location_information_page.fill_location_information_form(test_data)
    additional_comments_page.fill_additional_comments(test_data)
    finance_quote_page.fill_finance_quote_form()


@then('the generated premium should be saved to excel')
def then_generated_premium_should_be_equal(page, test_data):
    print_your_quote_page = PrintYourQuotePage(page)
    print_your_quote_page.save_premium(test_data)
