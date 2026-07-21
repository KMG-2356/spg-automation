import os

import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from config import *
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage
from page_objects.program_selection_page import ProgramSelectionPage
from page_objects.commercial_lines_basic_information_page import CommercialLinesBasicInformationPage
from page_objects.agency_information_page import AgencyInformationPage
from page_objects.insured_information_page import InsuredInformationPage
from page_objects.finance_quote_page import FinanceQuotePage
from page_objects.print_your_quote_page import PrintYourQuotePage
from page_objects.inland_marine_page import InlandMarinePage
from page_objects.inland_marine_loss_history_page import InlandMarineLossHistoryPage
from models.agency_info_params import AgencyInfoParams
from models.insured_info_params import InsuredInfoParams
from models.inland_marine_params import InlandMarineParams
from models.inland_marine_loss_history_params import InlandMarineLossHistoryParams


FEATURE_PATH = os.path.join(os.path.dirname(__file__), "..", "inland_marine.feature")

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
    agency_information_page = AgencyInformationPage(page)
    insured_information_page = InsuredInformationPage(page)
    commercial_lines_basic_info_page = CommercialLinesBasicInformationPage(page)
    finance_quote_page = FinanceQuotePage(page)
    inland_marine_page = InlandMarinePage(page)
    inland_marine_loss_history_page = InlandMarineLossHistoryPage(page)


    agency_info = AgencyInfoParams(
        agency_name=test_data["01_Policy_Info"][0]["Agency Name"],
        agency_id_code=test_data["01_Policy_Info"][0]["Agency ID Code"],
        agent_full_name=test_data["01_Policy_Info"][0]["Agent Full Name"],
        agent_email=test_data["01_Policy_Info"][0]["Agent E-Mail"],
        agent_phone=test_data["01_Policy_Info"][0]["Agent Phone"],
        agent_fax=test_data["01_Policy_Info"][0]["Agent Fax"],
        agent_commission=str(test_data["01_Policy_Info"][0]["Agent Commission %"]),
        address_street1=test_data["01_Policy_Info"][0]["Address - Street 1"],
        address_street2=test_data["01_Policy_Info"][0]["Address - Street 2"],
        city=test_data["01_Policy_Info"][0]["Address - City"],
        state=test_data["01_Policy_Info"][0]["Address - State"],
        zip_code=str(test_data["01_Policy_Info"][0]["Address - Zip"])
    )

    insured_info = InsuredInfoParams(
        insured_email=test_data["01_Policy_Info"][0]["Email Address"],
        insured_full_name=test_data["01_Policy_Info"][0]["Business / Insured Name"],
        insured_phone=str(test_data["01_Policy_Info"][0]["Phone Number"]),
        mailing_street1=test_data["01_Policy_Info"][0]["Mailing Street 1"],
        mailing_zip=test_data["01_Policy_Info"][0]["Mailing Zip"],
        mailing_city=test_data["01_Policy_Info"][0]["Mailing City"],
        mailing_state=test_data["01_Policy_Info"][0]["Mailing State"],
        type_of_entity=test_data["01_Policy_Info"][0]["Type of Entity"],
        coverage_street_address1=test_data["01_Policy_Info"][0]["Garaging Street 1"],
        coverage_street_address2=test_data["01_Policy_Info"][0]["Garaging Street 2"],
        coverage_city=test_data["01_Policy_Info"][0]["Garaging City"],
        coverage_state=test_data["01_Policy_Info"][0]["Garaging State"],
        coverage_zip=test_data["01_Policy_Info"][0]["Garaging Zip"],
        mailing_address_different=test_data["01_Policy_Info"][0]["Is Mailing Address Different?"]
    )

    inland_marine_info = InlandMarineParams(
        miscellaneous_article_coverage=test_data["04_IM_MiscArticles"][0]["Enable Miscellaneous Articles?"],
        used_for_logging=test_data["03_IM_Equipment"][0]["Is any scheduled equipment used for logging?"],
        total_value_of_misc_items=test_data["04_IM_MiscArticles"][0]["Total Value of Miscellaneous Articles ($)"],
        loss_payees=test_data["05_IM_LossPayees"],
        has_loss_payees=test_data["05_IM_LossPayees"][0]["Has Loss Payees?  (Yes / No)"],
        equipments=test_data["03_IM_Equipment"],
    )

    inland_marine_loss_history_info = InlandMarineLossHistoryParams(

    )

    home_page.click_new_quote_button()
    program_selection_page.select_commercial_lines_LOB()
    commercial_lines_basic_info_page.fill_commercial_line_basic_information_IM_form()
    agency_information_page.fill_agency_information_form(agency_info)
    insured_information_page.fill_insured_information_form_for_IM(insured_info)
    inland_marine_page.fill_inland_marine_form(inland_marine_info)
    inland_marine_loss_history_page.fill_loss_history_form(inland_marine_loss_history_info)
    finance_quote_page.fill_finance_quote_form()


@then('the generated premium should be saved to excel')
def then_generated_premium_should_be_equal(page, test_data):
    print_your_quote_page = PrintYourQuotePage(page)
    print_your_quote_page.save_premium(test_data, "im_output", "01_Policy_Info")
