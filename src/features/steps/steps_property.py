import os
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from config import *
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage
from page_objects.program_selection_page import ProgramSelectionPage
from page_objects.commercial_lines_basic_information_page import CommercialLinesBasicInformationPage
from page_objects.agency_information_page import AgencyInformationPage
from page_objects.general_liability_info_page import GLInformationPage
from page_objects.property_insured_page import InsuredInformationPage
from page_objects.cargo_loss_history_page import LossHistoryInformationPage
from page_objects.cargo_loss_history2_page import LossHistoryInformation2Page
from page_objects.finance_quote_page import FinanceQuotePage
from page_objects.print_your_quote_page import PrintYourQuotePage

from models.agency_info_params import AgencyInfoParams
from models.property_insured_params import InsuredInfoParams
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
    # cargo_loss_history_info = LossHistoryParams(
    #     any_losses_in_the_past_3Years=test_data["Cargo_APD_LossHistory"][0]["Any Losses in the Past 3 Years?"],
 
    #     losses=[LossHistoryRecord(
    #         loss_year=row["Loss Year"],
    #         type_of_loss=row["Type of Loss"],
    #         premium_at_time_of_loss=row["Premium at Time of Loss ($)"],
    #         amount_paid=row["Amount Paid ($)"],
    #         amount_outstanding=row["Amount Outstanding ($)"],
    #     )
    #     for row in test_data["Cargo_APD_LossHistory"]
    # ]

    # )
    

    
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

    home_page.click_new_quote_button()
    program_selection_page.select_commercial_lines_LOB()
    commercial_line_basic_info_page.fill_commercial_line_basic_information_Prop_plus_GL_form(test_data)
    agency_information_page.fill_agency_information_form(agency_info)
    insured_information_page.fill_insured_information_form(insured_info)
    general_information_page.fill_general_liability_info(general_liability_info)
    cargo_loss_histor2_page.fill_loss_history2_info(cpgl_loss_history2_info)
    finance_quote_page.fill_finance_quote_form()



@then('the generated premium should be saved to excel')
def then_generated_premium_should_be_equal(page, test_data):
    print_your_quote_page = PrintYourQuotePage(page)
    print_your_quote_page.save_premium(test_data, "cargo_output","Policy_Info")
