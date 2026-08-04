import os
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from config import *
from models.property_locations_params import PropertyLocationParams
from page_objects.cargo_loss_history_page import LossHistoryInformationPage
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage
from page_objects.program_selection_page import ProgramSelectionPage
from page_objects.commercial_lines_basic_information_page import CommercialLinesBasicInformationPage
from page_objects.agency_information_page import AgencyInformationPage
from page_objects.general_liability_info_page import GLInformationPage
from page_objects.property_insured_page import InsuredInformationPage
from page_objects.property_additional_questions_page import AdditionalQuestionsPage
from page_objects.cargo_loss_history2_page import LossHistoryInformation2Page
from page_objects.finance_quote_page import FinanceQuotePage
from page_objects.print_your_quote_page import PrintYourQuotePage
from page_objects.property_locations_page import PropertyLocationsPage

from models.agency_info_params import AgencyInfoParams
from models.property_insured_params import InsuredInfoParams
from models.property_building_params import BuildingInfoParams
from models.property_loss_payee_params import PropertyLossPayeeParams
from models.general_liability_info_params import GeneralLiabilityParams, GLRecord, AdditionalInsuredRecord
from models.cargo_loss_history_info_params import LossHistoryParams,LossHistoryRecord
from models.cargo_loss_history2_params import SubjectivityRecord, LossHistory2Record,CargoLossHistory2Params


FEATURE_PATH = os.path.join(os.path.dirname(__file__), "..", "property.feature")

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
    commercial_line_basic_info_page = CommercialLinesBasicInformationPage(page)
    agency_information_page = AgencyInformationPage(page)
    general_information_page = GLInformationPage(page)
    insured_information_page = InsuredInformationPage(page)
    property_additional_questions_page = AdditionalQuestionsPage(page)
    property_location_page = PropertyLocationsPage(page)
    cargo_loss_history_info_page = LossHistoryInformationPage(page)
    cargo_loss_histor2_page = LossHistoryInformation2Page(page)
    finance_quote_page = FinanceQuotePage(page)


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

    insured_info = InsuredInfoParams(
        insured_email=test_data["Policy_Info"][0]["Insured Email Address"],
        insured_full_name=test_data["Policy_Info"][0]["Business / Insured Name"],
        insured_phone=str(test_data["Policy_Info"][0]["Insured Phone Number"]),
        insured_street1=test_data["Policy_Info"][0]["Address  -  Street 1"],
        insured_street2=test_data["Policy_Info"][0]["Address  -  Street 2"],
        insured_address_zip=test_data["Policy_Info"][0]["Address  -  Zip"],
        insured_city=test_data["Policy_Info"][0]["Address  -  City"],
        insured_state=test_data["Policy_Info"][0]["Address  -  State"],
        type_of_entity=test_data["Policy_Info"][0]["Type of Entity"],
        physical_street1=test_data["Policy_Info"][0]["Insured Pysical Address  -  Street 1"],
        physical_street2=test_data["Policy_Info"][0]["Insured Pysical Address  -  Street 2"],
        physical_zip=test_data["Policy_Info"][0]["Insured Physical Address  -  Zip"],
        physical_city=test_data["Policy_Info"][0]["Insured Physical Address  -  City"],
        physical_state=test_data["Policy_Info"][0]["Insured Physical Address  -  State"],
        trustee_full_name=test_data["Policy_Info"][0]["Full Name"],
        trustee_street_address1=test_data["Policy_Info"][0]["Trustee Address -  Street 1"],
        trustee_street_address2=test_data["Policy_Info"][0]["Trustee Address  -  Street 2"],
        trustee_street_zip=test_data["Policy_Info"][0]["Trustee Address  -  Zip"],
        trustee_state=test_data["Policy_Info"][0]["Trustee Address  -  State"],
        trustee_city=test_data["Policy_Info"][0]["Trustee Address  -  City"],
        mailing_address_different=test_data["Policy_Info"][0]["Is Insured's physical address same as the mailing address?"]
    )

    additional_questions_info = InsuredInfoParams(
            same_as_insured=test_data["Policy_Info"][0]["Same as Insured?"],
            contact_full_name=test_data["Policy_Info"][0]["Contact Full Name"],
            contact_email=test_data["Policy_Info"][0]["Contact Email"],
            contact_phone=test_data["Policy_Info"][0]["Contact Phone"],
    )
            
    general_liability_info = GeneralLiabilityParams(
        limit_option=test_data["GL_ClassCodes_Atrium"][0]["Limit Option"],
        years_in_business=test_data["GL_ClassCodes_Atrium"][0]["Years in Business"],
        years_of_experience=test_data["GL_ClassCodes_Atrium"][0]["Years of Experience"],        
        classification_codes=[GLRecord(class_code=row["Class Code"],
            square_feet_of_building=row["Square feet of building"],
            no_of_acres=row["No.Of Acres"]
            )
            for row in test_data["GL_ClassCodes_Atrium"]
            ],
        additional_insureds=[AdditionalInsuredRecord(
            AI_form=row["AI Form"],
            AI_name=row["AI Name"],
            Street1=row["Street 1"],
            Street2=row["Street 2"],
            City=row["City"],
            State=row["State"],
            ZIP=row["ZIP"],
            )
            for row in test_data["GL_AddlInsureds"]
            ]    
    )
    
    cpgl_loss_history2_info = CargoLossHistory2Params(
            any_losses_in_the_past3_years=test_data["CP_GL_LossHistory"][0]["Any Losses in the Past 3 Years?"],
            # any_unrepaired_damage_from_prior_losses=test_data["CP_GL_LossHistory"][0]["Any Unrepaired Damage from Prior Losses?"],
            # add_extra_subjectivities=test_data["CP_GL_LossHistory"][0]["Add extra subjectivities?"],
            # notes_about_the_insured=test_data["CP_GL_LossHistory"][0]["Notes about the Insured"],
            # subjectivity=[SubjectivityRecord(
            #     subjectivity_text=row["Subjectivity Text"]
            #     )
                # for row in test_data["CP_GL_LossHistory"]],
            losses2=[LossHistory2Record(
                details=row["Description"],
                loss_date=row["Loss Date"],
                amount=row["Amount"],
                type_of_loss=row["Type of Loss"],
                
                )                
                
                for row in test_data["CP_GL_LossHistory"]]
        
    )

    location_buildings = [
        [
            building_row
            for building_row in test_data["CP_Buildings"]
            if str(building_row["Loc #"]).strip() == str(location_index + 1)
        ]
        for location_index, _ in enumerate(test_data["CP_Locations"])
    ]

    locations_info = [
        PropertyLocationParams(
            index=i,
            city=row["City"],
            state=row["State"],
            zip_code=str(row["ZIP"]),
            coverage_form=row["Coverage Form"],
            protection_class=str(row["Protection Class"]),
            inspection_fee=row["Inspection Fee"],
            is_coastal=row["Within 20mi of Coast?"],
            distance_coast=row["Coastal Distance"],
            nc_island=row["Barrier Island?"],
            has_hazard=row["Hazardous Exposure?"],
            hazard_desc=row["Hazard Description"],
            theft_sublimit="10",
            exc_wh_cov="No",
            wh_tiv_percent="0%",
            buildings=[
                BuildingInfoParams(
                    ZIP_code=str(building["ZIP Code"]),
                    Suite_Unit_floor=str(building["Suite/Unit/Floor"]),
                    stories_Sq_Ft=str(building["Stories"]),
                    year_built=str(building["Year Built"]),
                    construction=str(building["Construction"]),
                    slate_Wood_shake_roof=str(building["Slate/Wood Shake Roof?"]),
                    occupancy=str(building["Occupancy"]),
                    building_value=str(building["Building Value ($)"]),
                    good_condition=str(building["Good Condition?"]),
                    valuation=str(building["Valuation"]),
                    coinsurance_deductible=str(building["Coinsurance"]),
                    hydrant_Dist=str(building["Hydrant Dist."]),
                    dist_unit=str(building["Dist. Unit"]),
                    fire_dept=str(building["Fire Dept"]),
                    sprinkler=str(building["Sprinkler?"]),
                    central_Alarm=str(building["Central Alarm?"]),
                    roof_updated_year=str(building["Roof Updated Year"]),
                    electrical_updated_year=str(building["Electrical Updated Year"]),
                    plumbing_updated_year=str(building["Plumbing Updated Year"]),
                    HVAC_updated_year=str(building["HVAC Updated Year"]),
                    loss_payees=[
                        PropertyLossPayeeParams(
                            full_name=str(payee["Full Name"]),
                            street1=str(payee["Street 1"]) if payee["Street 1"] is not None else "",
                            street2=str(payee["Street 2"]) if payee["Street 2"] is not None else "",
                            city=str(payee["City"]),
                            state=str(payee["State"]),
                            zip_code=str(payee["ZIP"]),
                            mortgagee=str(payee["Mortgagee?"]),
                            loan_number=str(payee["Loan Number"]) if payee["Loan Number"] is not None else "",
                            relationship=str(payee["Relationship"]),
                            financial_interest=str(payee["Financial Interest?"]),
                            notes=str(payee["Notes"]) if payee["Notes"] is not None else "",
                        )
                        for payee in test_data["CP_LossPayees"]
                        if (payee.get("Test ID") or "") == (row.get("Test ID") or "")
                        and str(payee["Bldg #"]).strip() == str(building_number)
                    ],
                )
                for building_number, building in enumerate(location_buildings[i], start=1)
            ],
        )
        for i, row in enumerate(test_data["CP_Locations"])
    ]

    home_page.click_new_quote_button()
    program_selection_page.select_commercial_lines_LOB()
    commercial_line_basic_info_page.fill_commercial_line_basic_information_Prop_plus_GL_form(test_data)
    agency_information_page.fill_agency_information_form(agency_info)
    insured_information_page.fill_insured_information_form(insured_info)
    property_location_page.fill_locations(locations_info)
    general_information_page.fill_general_liability_info(general_liability_info)
    property_additional_questions_page.fill_additional_question_information_form(additional_questions_info)
    cargo_loss_histor2_page.fill_loss_history2_info(cpgl_loss_history2_info)
    finance_quote_page.fill_finance_quote_form()



@then('the generated premium should be saved to excel')
def then_generated_premium_should_be_equal(page, test_data):
    print_your_quote_page = PrintYourQuotePage(page)
    print_your_quote_page.save_premium(test_data, "cargo_output","Policy_Info")
