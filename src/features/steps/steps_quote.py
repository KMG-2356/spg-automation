import os

import pytest
from pytest_bdd import scenario, given, when, then, parsers
from config import *
from page_objects.home_page import HomePage
from page_objects.program_selection_page import ProgramSelectionPage
from page_objects.commercial_lines_basic_information_page import CommercialLinesBasicInformationPage
from page_objects.agency_information_page import AgencyInformationPage
from page_objects.location_page import LocationPage
from page_objects.insured_information_page import InsuredInformationPage
from page_objects.additional_questions_page import AdditionalQuestionPage


FEATURE_PATH = os.path.join(os.path.dirname(__file__), "..", "quote.feature")

# scenarios(FEATURE_PATH)

@scenario(FEATURE_PATH, "Rater Premium and Excel Premium are equal for Windhail LOB")
def test_rater_premium_and_excel_premium_are_equal_for_windhail_lob(test_data):
    """This function explicitly accepts 'test_data' so pytest can parameterize it."""
    pass

@pytest.fixture
def home_page(page, test_data):
    pass
    # return HomePage(page)


@given('the home page is open')
def given_home_page_open(home_page, base_url, test_data):
    pass
    # home_page.navigate(base_url)
    # return home_page


@when('the user generates a premium')
def when_user_generates_premium(home_page, page, test_data):
    print(test_data)
    # program_selection_page = ProgramSelectionPage(page)
    # commercial_lines_basic_information_page = CommercialLinesBasicInformationPage(page)
    # agency_information_page = AgencyInformationPage(page)
    # location_information_page = LocationPage(page)
    # insured_information_page = InsuredInformationPage(page)
    # additional_comments_page = AdditionalQuestionPage(page)

    # home_page.click_new_quote_button()
    # program_selection_page.select_monoline_wind_LOB()
    # commercial_lines_basic_information_page.click_agency_information_button()
    # agency_information_page.fill_agency_information_form(test_data)
    # insured_information_page.fill_insured_information(test_data)
    # location_information_page.fill_location_information_form(test_data)
    # additional_comments_page.fill_additional_comments(test_data)


@then('the generated premium should be equal to excel rater premium')
def then_generated_premium_should_be_equal(page, test_data):
    pass