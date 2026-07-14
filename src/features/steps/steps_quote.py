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


FEATURE_PATH = os.path.join(os.path.dirname(__file__), "..", "quote.feature")

scenarios(FEATURE_PATH)

@pytest.fixture
def login_page(page, test_data):
    return LoginPage(page)


@given('the home page is open')
def given_home_page_open(login_page, base_url, test_data):
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
    print_your_quote_page = PrintYourQuotePage(page)

    home_page.click_new_quote_button()
    program_selection_page.select_monoline_wind_LOB()
    commercial_lines_basic_information_page.fill_commercial_line_basic_information_form()
    agency_information_page.fill_agency_information_form(test_data)
    insured_information_page.fill_insured_information_form(test_data)
    location_information_page.fill_location_information_form(test_data)
    additional_comments_page.fill_additional_comments(test_data)
    finance_quote_page.fill_finance_quote_form()
    print_your_quote_page.save_premium(test_data)


@then('the generated premium should be equal to excel rater premium')
def then_generated_premium_should_be_equal(page, test_data):
    pass