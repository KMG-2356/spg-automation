import os

import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from config import *
from page_objects.home_page import HomePage
from page_objects.program_selection_page import ProgramSelectionPage
from page_objects.commercial_lines_basic_information_page import CommercialLinesBasicInformationPage

FEATURE_PATH = os.path.join(os.path.dirname(__file__), "..", "quote.feature")

scenarios(FEATURE_PATH)

@pytest.fixture
def home_page(page, test_data):
    return HomePage(page)


@given('the home page is open')
def given_home_page_open(home_page, base_url, test_data):
    home_page.navigate(base_url)
    return home_page


@when('the user generates a premium')
def when_user_generates_premium(home_page, page, test_data):
    program_selection_page = ProgramSelectionPage(page)
    commercial_lines_basic_information_page = CommercialLinesBasicInformationPage(page)

    home_page.click_new_quote_button()
    program_selection_page.select_monoline_wind_LOB()
    commercial_lines_basic_information_page.click_agency_information_button()


@then('the generated premium should be equal to excel rater premium')
def then_generated_premium_should_be_equal(page, test_data):
    pass