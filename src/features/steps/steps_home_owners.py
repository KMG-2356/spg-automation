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
from page_objects.home_owners_dwelling_information_page import HomeOwnersDwellingInformationPage
from page_objects.home_owners_applicant_information_page import HomeOwnerApplicantInformationPage
from models.agency_info_params import AgencyInfoParams
from models.insured_info_params import InsuredInfoParams
from models.home_owners_dwelling_info_params import HomeOwnersDwellingInfoParams
from models.home_owners_applicant_info_params import HomeOwnersApplicantInfoParams


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
    home_owners_dwelling_information_page = HomeOwnersDwellingInformationPage(page)
    home_owner_applicant_information_page = HomeOwnerApplicantInformationPage(page)

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

    insured_info = InsuredInfoParams(
        insured_full_name=test_data["Policy_Info"][0]["Insured Full Name"],
        insured_email=test_data["Policy_Info"][0]["Insured E-Mail"],
        insured_phone=str(test_data["Policy_Info"][0]["Insured Phone"]),
        insured_occupation=test_data["Policy_Info"][0]["Insured Occupation"],
        insured_employer=test_data["Policy_Info"][0]["Insured Employer"],
        insured_dob=test_data["Policy_Info"][0]["Insured Date of Birth"],
        insured_street1=test_data["Policy_Info"][0]["Insured Address Street 1"],
        insured_street2=test_data["Policy_Info"][0]["Insured Address Street 2"],
        insured_address_zip=test_data["Policy_Info"][0]["Insured Address ZIP"],
        mailing_street1=test_data["Policy_Info"][0]["Mailing Street 1"],
        mailing_street2=test_data["Policy_Info"][0]["Mailing Street 2"],
        mailing_zip=str(test_data["Policy_Info"][0]["Mailing ZIP"]),
        mailing_city=test_data["Policy_Info"][0]["Insured Address City"],
        mailing_state=test_data["Policy_Info"][0]["Insured Address State"],
        type_of_entity=test_data["Policy_Info"][0]["Type of Entity"],
        
        additional_resident_or_spouse=test_data["Policy_Info"][0]["Additional Resident / Spouse?"],
        additional_resident_full_name=test_data["Policy_Info"][0]["Additional Resident Full Name"],
        additional_resident_occupation=test_data["Policy_Info"][0]["Additional Resident Occupation"],
        additional_resident_dob=str(test_data["Policy_Info"][0]["Additional Resident Date of Birth"]),
        additional_resident_employer=test_data["Policy_Info"][0]["Additional Resident Employer"],
        
        mailing_address_different=test_data["Policy_Info"][0]["Mailing Address Different from Insured?"],
        diff_mailing_zip=test_data["Policy_Info"][0]["Mailing ZIP"],
        diff_mailing_street1=test_data["Policy_Info"][0]["Mailing Street 1"],
        diff_mailing_street2=test_data["Policy_Info"][0]["Mailing Street 2"],
        diff_mailing_city=test_data["Policy_Info"][0]["Mailing City"],
        diff_mailing_state=test_data["Policy_Info"][0]["Mailing State"]
    )

    dwelling_info = HomeOwnersDwellingInfoParams(
        protection_class=test_data["HO_Dwelling"][0]["Protection Class"],
        adequate_water=test_data["HO_Dwelling"][0]["Within 1,000 ft of Adequate Water Source?"],
        response_time=test_data["HO_Dwelling"][0]["Fire Dept Response < 15 Min?"],
        accessible_property=test_data["HO_Dwelling"][0]["Easily Accessible Year Round?"],
        single_family=test_data["HO_Dwelling"][0]["Is Single Family Residence?"],
        owner_occupied=test_data["HO_Dwelling"][0]["Is Dwelling Owner Occupied?"],
        dwelling_type=test_data["HO_Dwelling"][0]["Type of Dwelling (Primary / Secondary)"],
        manufactured_home=test_data["HO_Dwelling"][0]["Is Dwelling a Manufactured Home?"],
        
        # Numeric Inputs & Details
        stories=str(test_data["HO_Dwelling"][0]["Number of Stories"]),
        year_built=str(test_data["HO_Dwelling"][0]["Year Built"]),
        dwelling_area=str(test_data["HO_Dwelling"][0]["Square Footage"]),
        
        # Condition & Construction
        good_condition=test_data["HO_Dwelling"][0]["Is Dwelling in Good Condition?"],
        existing_damage=test_data["HO_Dwelling"][0]["Does Dwelling Have Existing Damage?"],
        renovation_or_construction=test_data["HO_Dwelling"][0]["Is Dwelling Undergoing Renovation?"],
        type_of_construction=test_data["HO_Dwelling"][0]["Type of Siding Material"],
        type_of_foundation=test_data["HO_Dwelling"][0]["Type of Foundation"],
        
        # Utilities & Plumbing
        central_heating=test_data["HO_Dwelling"][0]["Central Heating by Licensed Professional?"],
        wood_burning_stove=test_data["HO_Dwelling"][0]["Wood Burning Stove?"],
        polybutylene_or_qwest_plumbing=test_data["HO_Dwelling"][0]["Polybutylene / Qwest Plumbing?"],
        prim_heat_source=test_data["HO_Dwelling"][0]["Is Wood Stove Primary Heating Source?"],
        water_heater=str(test_data["HO_Dwelling"][0]["Year of Last Water Heater Replacement"]),
        
        # Roof & Siding
        roofing_material=test_data["HO_Dwelling"][0]["Type of Roofing Material"],
        flat_roof=test_data["HO_Dwelling"][0]["Is the Roof Flat?"],
        roof_year=str(test_data["HO_Dwelling"][0]["Year of Last Roof Replacement"]),
        siding_material=test_data["HO_Dwelling"][0]["Type of Siding Material"],
        
        # Property & Liabilities
        over_two_acres=test_data["HO_Dwelling"][0]["Located on More Than 2 Acres?"],
        over_ten_acres=test_data["HO_Dwelling"][0]["Located on More Than 10 Acres?"],
        unfenced_pool=test_data["HO_Dwelling"][0]["Unfenced Swimming Pool or Body of Water?"],
        close_to_tidal_water=test_data["HO_Dwelling"][0]["Within 1,000 ft of Ocean / Bay / Sound?"],
        horses=test_data["HO_Dwelling"][0]["Horses on Premises?"],
        bite_history=test_data["HO_Dwelling"][0]["Animals With Bite History?"],
        business_pursuits=test_data["HO_Dwelling"][0]["Business Pursuits on Premises?"],
        has_loss_payees=test_data["HO_Dwelling"][0]["Is Dwelling Rented to Others?"],

        update_years_electricty_years = test_data["HO_Dwelling"][0]["Electrical Last Update Year"],
        update_years_plumbing_years = test_data["HO_Dwelling"][0]["Plumbing Last Update Year"],
        update_years_heating_ac_years = test_data["HO_Dwelling"][0]["Heating / AC Last Update Year"],
        update_years_updated_electrical = test_data["HO_Dwelling"][0]["Electrical Service Upgraded to 100 Amp+?"],
        update_years_has_fuse_box = test_data["HO_Dwelling"][0]["Any Fuse Boxes?"],
        update_years_has_knob_tube = test_data["HO_Dwelling"][0]["Knob and Tube Wiring?"],
        update_years_has_aluminium_wiring = test_data["HO_Dwelling"][0]["Aluminum Wiring?"],
        update_years_has_lead_plumbing = test_data["HO_Dwelling"][0]["Lead Plumbing?"],

        # Loss Payee Information
        loss_payee_full_name=test_data["HO_LossPayees"][0]["Full Name"],
        loss_payee_street_address1=test_data["HO_LossPayees"][0]["Street 1"],
        loss_payee_street_address2=test_data["HO_LossPayees"][0]["Street 2"],
        loss_payee_city=test_data["HO_LossPayees"][0]["City"],
        loss_payee_state=test_data["HO_LossPayees"][0]["State"],
        loss_payee_zip=str(test_data["HO_LossPayees"][0]["ZIP"]),
        is_loss_payee_mortgage=test_data["HO_LossPayees"][0]["Is Mortgagee?"],
        are_mortgage_payments_current=test_data["HO_LossPayees"][0]["Mortgage Current?"],
        loss_payee_loan_number=str(test_data["HO_LossPayees"][0]["Loan Number"]),
        loss_payees=len(test_data["HO_LossPayees"])
    )

    applicant_info = HomeOwnersApplicantInfoParams(
        # --- Dwelling Info (Not present in the list, defaulted to empty strings) ---
        protection_class="",
        adequate_water="",
        response_time="",
        accessible_property="",
        single_family="",
        owner_occupied="",
        dwelling_type="",
        manufactured_home="",

        # --- Applicant Info ---
        credit_history=test_data["HO_Policy"][0]["Insured Credit History"],
        arson_and_fraud=test_data["HO_Policy"][0]["Any Arson / Fraud Convictions?"],
        bankruptcy=test_data["HO_Policy"][0]["Bankruptcy in Last Year?"],
        foreclosure=test_data["HO_Policy"][0]["Foreclosure in Last 5 Years?"],
        child_support=test_data["HO_Policy"][0]["Any Past Due Child Support?"],
        repossessions=test_data["HO_Policy"][0]["Repossessions in Last 3 Years?"],
        
        # --- Purchase Details ---
        new_purchase=test_data["HO_Policy"][0]["Is Dwelling a New Purchase?"],
        year_purchased=str(test_data["HO_Policy"][0]["Year Purchased"]),
        prior_foreclosure=test_data["HO_Policy"][0]["Was Dwelling Foreclosed When Purchased?"],
        purchase_price=str(test_data["HO_Policy"][0]["Purchase Price ($)"]),
        
        # --- Insurance History ---
        prior_insurance=test_data["HO_Policy"][0]["Prior Insurance on This Account?"],
        prior_commonwealth=test_data["HO_Policy"][0]["Previously with Commonwealth Underwriters?"],
        prior_carrier=test_data["HO_Policy"][0]["Prior Carrier Name"],
        previous_expiration=test_data["HO_Policy"][0]["Expiration Date of Prior Insurance"],
        prior_premium=str(test_data["HO_Policy"][0]["Prior Insurance Premium ($)"]),
        
        # --- Agency & Coverage Details ---
        new_agency=test_data["HO_Policy"][0]["Risk New to Agency?"],
        lapse_of_coverage=test_data["HO_Policy"][0]["Lapse > 30 Days?"],
        termination_at_companies_request=test_data["HO_Policy"][0]["Terminated at Company Request?"],
        reason_for_termination=test_data["HO_Policy"][0]["Reason for Termination"],
        previous_wind_hail=test_data["HO_Policy"][0]["Previous Wind / Hail Deductible"]
    )

    home_page.click_new_quote_button()
    program_selection_page.select_personal_lines_LOB()
    personal_lines_basic_information_page.fill_personal_line_basic_information_form(test_data)
    agency_information_page.fill_agency_information_form(agency_info)
    insured_information_page.fill_insured_information_form_for_ho(insured_info)
    home_owners_dwelling_information_page.fill_home_owners_dwelling_information_form(dwelling_info, test_data)
    home_owner_applicant_information_page.fill_applicant_info(applicant_info)
    # location_information_page.fill_location_information_form(test_data)
    # additional_comments_page.fill_additional_comments(test_data)
    # finance_quote_page.fill_finance_quote_form()


@then('the generated premium should be saved to excel')
def then_generated_premium_should_be_equal(page, test_data):
    print_your_quote_page = PrintYourQuotePage(page)
    print_your_quote_page.save_premium(test_data)
