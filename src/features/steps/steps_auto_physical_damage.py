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
from page_objects.apd_additional_insured_info_page import APDAdditionalInsuredInformationPage
from page_objects.apd_risk_information_page import APDRiskInformationPage
from models.agency_info_params import AgencyInfoParams
from models.apd_additional_insured_info_params import APDAdditionalInsuredInformationParams
from models.apd_risk_info_params import RiskInfoParams

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
    apd_additional_insured_info_page = APDAdditionalInsuredInformationPage(page)
    finance_quote_page = FinanceQuotePage(page)
    inland_marine_page = InlandMarinePage(page)
    risk_info_page = APDRiskInformationPage(page)
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
            "Describe Carrier Details"
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
        has_secondary_garage = test_data["Policy_Info"][0]["Secondary garaging address?"],
        secondary_garages=[test_data["Policy_Info"][0][f"Garage Address#{i}"] for i in range(1, 6)],
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

    apd_additional_insured_info = APDAdditionalInsuredInformationParams(
        has_applicant_ever_operated_under_different_name=test_data["Cargo_APD_Insured_UW_Info"][0]["Has applicant ever operated under a different name?"],
        does_applicant_have_other_carrier_operations=test_data["Cargo_APD_Insured_UW_Info"][0]["Does applicant have other carrier operations?"],
        describe_other_operations=test_data["Cargo_APD_Insured_UW_Info"][0]["Describe other operations"],
        is_the_owner_also_listed_as_driver=test_data["Cargo_APD_Insured_UW_Info"][0]["Is the owner also listed as a driver?"],
        has_insured_had_coverage_in_the_last_3years=test_data["Cargo_APD_Insured_UW_Info"][0]["Has insured had coverage in the last 3 years?"],
        insurance_placed_through_commonwealth_underwriters=test_data["Cargo_APD_Insured_UW_Info"][0]["Insurance placed through Commonwealth Underwriters?"],
        any_insurer_canceled_non_renewed_in_last_3years=test_data["Cargo_APD_Insured_UW_Info"][0]["Any insurer canceled / non-renewed in last 3 years?"],
        prior_carrier_information_known=test_data["Cargo_APD_Insured_UW_Info"][0]["Prior carrier information known?"],
        prior_carrier_name=test_data["Cargo_APD_Insured_UW_Info"][0]["Prior carrier name"],
        prior_perils_form=test_data["Cargo_APD_Insured_UW_Info"][0]["Prior perils form"],
        prior_policy_premium=test_data["Cargo_APD_Insured_UW_Info"][0]["Prior policy premium ($)"],
        prior_policy_deductible=test_data["Cargo_APD_Insured_UW_Info"][0]["Prior policy deductible ($)"],
        prior_policy_limit=test_data["Cargo_APD_Insured_UW_Info"][0]["Prior policy limit ($)"],
        prior_policy_expiration_date=test_data["Cargo_APD_Insured_UW_Info"][0]["Prior policy expiration date"],
        was_a_renewal_offer_made=test_data["Cargo_APD_Insured_UW_Info"][0]["Was a renewal offer made?"],
        consecutive_coverage_greater_than_ot_equal_to_12months=test_data["Cargo_APD_Insured_UW_Info"][0]["Consecutive coverage >= 12 months?"],
    )

    risk_info = RiskInfoParams(
        hiring_process=test_data["Cargo_APD_Drivers"][0]["Steps taken in employing new drivers"],
        firing_process=test_data["Cargo_APD_Drivers"][0]["Grounds for firing a driver?"],
        rented_equipment=test_data["Cargo_APD_Insured_UW_Info"][0]["Does insured lease / loan / rent equipment to others?"],
        rented_each_job=test_data["Cargo_APD_Insured_UW_Info"][0]["Vehicles rented for each job?"],
        titled_vehicles=test_data["Cargo_APD_Insured_UW_Info"][0]["All vehicles titled under named insured?"],
        secure_vehicle=test_data["Cargo_APD_Insured_UW_Info"][0]["Steps taken to secure vehicles"],
        owner_driven=test_data["Cargo_APD_Insured_UW_Info"][0]["Any vehicles driven by an owner? (PhysDam Only)"],
        inspected_vehicles=test_data["Cargo_APD_Insured_UW_Info"][0]["Equipment regularly inspected and serviced? (PhysDam Only)"],
        exemption_reason=test_data["Cargo_APD_Insured_UW_Info"][0]["     -> Reasons for not requesting Insurance (PhysDam Only)"],
        has_extra_equipment=test_data["Cargo_APD_Insured_UW_Info"][0]["Owns equipment other than vehicles listed?"],
        inspection_interval=test_data["Cargo_APD_Insured_UW_Info"][0]["     -> Interval (PhysDam Only)"],
        gvw=test_data["Cargo_APD_Insured_UW_Info"][0]["Gross Vehicle Weight of any Unit greater than 26,000 lbs?"],
        driver_experience=test_data["Cargo_APD_Insured_UW_Info"][0][" -> Any drivers have less than 2 years with a Commercial Driver's License Class A (CDL-A)?"],
        drivers=test_data["Cargo_APD_Drivers"],
        vehicles=test_data["Cargo_APD_Vehicles"],
        trailers=test_data["Cargo_APD_Trailers"],
    )

    home_page.click_new_quote_button()
    program_selection_page.select_commercial_lines_LOB()
    commercial_lines_basic_info_page.fill_commercial_line_basic_information_PD_form()
    agency_information_page.fill_agency_information_form(agency_info)
    apd_insured_information_page.fill_apd_insured_information_form(insured_info)
    apd_additional_insured_info_page.fill_additional_insured_info(apd_additional_insured_info)
    risk_info_page.fill_risk_information(risk_info)
    # finance_quote_page.fill_finance_quote_form()


@then('the generated premium should be saved to excel')
def then_generated_premium_should_be_equal(page, test_data):
    print_your_quote_page = PrintYourQuotePage(page)
    print_your_quote_page.save_premium(test_data, "im_output", "01_Policy_Info")
