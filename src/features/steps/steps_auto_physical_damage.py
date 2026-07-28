import os

import pytest
from pytest_bdd import scenarios, given, when, then
from config import *
from models.apd_insured_info_params import APDInsuredInfoParams
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage
from page_objects.program_selection_page import ProgramSelectionPage
from page_objects.commercial_lines_basic_information_page import CommercialLinesBasicInformationPage
from page_objects.agency_information_page import AgencyInformationPage
from page_objects.apd_insured_information_page import APDInsuredInformationPage
from page_objects.finance_quote_page import FinanceQuotePage
from page_objects.print_your_quote_page import PrintYourQuotePage
from page_objects.inland_marine_page import InlandMarinePage
from page_objects.inland_marine_loss_history_page import InlandMarineLossHistoryPage
from models.agency_info_params import AgencyInfoParams


FEATURE_PATH = os.path.join(os.path.dirname(__file__), "..", "auto_physical_damage.feature")

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
    apd_insured_information_page = APDInsuredInformationPage(page)
    commercial_lines_basic_info_page = CommercialLinesBasicInformationPage(page)
    finance_quote_page = FinanceQuotePage(page)
    inland_marine_page = InlandMarinePage(page)
    inland_marine_loss_history_page = InlandMarineLossHistoryPage(page)


    agency_info = AgencyInfoParams(
        agency_name=test_data["Policy_Info"][0]["Agency Name"],
        agency_id_code=test_data["Policy_Info"][0]["Agency ID Code"],
        agent_full_name=test_data["Policy_Info"][0]["Agent's Full Name"],
        agent_email=test_data["Policy_Info"][0]["Agent E-Mail"],
        agent_phone=test_data["Policy_Info"][0]["Agent Phone"],
        agent_fax=test_data["Policy_Info"][0]["Agent Fax"],
        agent_commission=str(test_data["Policy_Info"][0]["Agent's Commission"]),
        address_street1=test_data["Policy_Info"][0]["Agent Address Street 1"],
        address_street2=test_data["Policy_Info"][0]["Agent Address Street 2"],
        city=test_data["Policy_Info"][0]["Agent Address City"],
        state=test_data["Policy_Info"][0]["Agent Address State"],
        zip_code=str(test_data["Policy_Info"][0]["Agent Address Zip"])
    )

    insured_info = APDInsuredInfoParams(
        insured_name=test_data["Policy_Info"][0]["Business / Insured Name"],
        entity_type=test_data["Policy_Info"][0]["Type of Entity"],
        insured_email=test_data["Policy_Info"][0]["Insured Email Address"],
        insured_phone=str(
            test_data["Policy_Info"][0]["Insured Phone Number"]
        ),
        mailing_street1=test_data["Policy_Info"][0]["Address  -  Street 1"],
        mailing_street2=test_data["Policy_Info"][0]["Address  -  Street 2"],
        mailing_city=test_data["Policy_Info"][0]["Address  -  City"],
        mailing_state=test_data["Policy_Info"][0]["Address  -  State"],
        mailing_zip=str(test_data["Policy_Info"][0]["Address  -  Zip"]),
        new_venture=test_data["Policy_Info"][0]["New Venture"],
        insured_icc=str(
            test_data["Policy_Info"][0]["Insured ICC Docket Number - MC#"]
        ),
        filings=test_data["Policy_Info"][0]["Filings Required"],
        all_owned_units=test_data["Policy_Info"][0][
            "Does this quote include all owned/operated units?"
        ],
        carrier_type=test_data["Policy_Info"][0]["Type of Company / Carrier"],
        own_goods=test_data["Policy_Info"][0][
            "Insured also carry their own goods?"
        ],
        garage_same=test_data["Policy_Info"][0][
            "Is Insured's physical address same as the mailing address?"
        ],
        carrier_details=test_data["Policy_Info"][0][
            "Describe Carrier Details "
        ],
        primary_garaging_street1=test_data["Policy_Info"][0][
            "Garaging Address Street 1"
        ],
        primary_garaging_street2=test_data["Policy_Info"][0][
            "Garaging Address Street 2"
        ],
        primary_garaging_city=test_data["Policy_Info"][0][
            "Garaging Address City"
        ],
        primary_garaging_state=test_data["Policy_Info"][0][
            "Garaging Address State"
        ],
        primary_garaging_zip=str(
            test_data["Policy_Info"][0]["Garaging Address Zip"]
        ),
        trustee_name=test_data["Policy_Info"][0]["Full Name"],
        trustee_street1=test_data["Policy_Info"][0][
            "Trustee Address -  Street 1"
        ],
        trustee_street2=test_data["Policy_Info"][0][
            "Trustee Address  -  Street 2"
        ],
        trustee_city=test_data["Policy_Info"][0]["Trustee Address  -  City"],
        trustee_state=test_data["Policy_Info"][0]["Trustee Address  -  State"],
        trustee_zip=str(
            test_data["Policy_Info"][0]["Trustee Address  -  Zip"]
        ),
    )


    home_page.click_new_quote_button()
    program_selection_page.select_commercial_lines_LOB()
    commercial_lines_basic_info_page.fill_commercial_line_basic_information_PD_form()
    agency_information_page.fill_agency_information_form(agency_info)
    apd_insured_information_page.fill_apd_insured_information_form(insured_info)
    # finance_quote_page.fill_finance_quote_form()


@then('the generated premium should be saved to excel')
def then_generated_premium_should_be_equal(page, test_data):
    print_your_quote_page = PrintYourQuotePage(page)
    print_your_quote_page.save_premium(test_data, "im_output", "01_Policy_Info")
