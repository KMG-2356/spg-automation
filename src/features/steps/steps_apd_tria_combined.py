import os

import pytest
from pytest_bdd import scenarios, given, when, then
from config import *
from models.apd_insured_info_params import APDInsuredInfoParams
from models.apd_loss_payee_info_params import APDLossPayeeInfoParams
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage
from page_objects.program_selection_page import ProgramSelectionPage
from page_objects.commercial_lines_basic_information_page import CommercialLinesBasicInformationPage
from page_objects.agency_information_page import AgencyInformationPage
from page_objects.apd_insured_information_page import APDInsuredInformationPage
from page_objects.finance_quote_page import FinanceQuotePage
from page_objects.print_your_quote_page import PrintYourQuotePage
from page_objects.apd_additional_insured_info_page import APDAdditionalInsuredInformationPage
from page_objects.apd_risk_information_page import APDRiskInformationPage
from page_objects.apd_loss_payee_info_page import LossPayeeInformationPage
from page_objects.apd_coverages_page import APDCoveragesPage
from page_objects.apd_commodities_page import APDCommoditiesPage
from page_objects.apd_loss_history_info_page import LossHistoryInformationPage
from page_objects.apd_additional_info_page import APDAdditionalInformationPage
from page_objects.apd_loss_history_page import LossHistoryPage
from models.agency_info_params import AgencyInfoParams
from models.apd_additional_insured_info_params import APDAdditionalInsuredInformationParams
from models.apd_risk_info_params import RiskInfoParams
from models.apd_coverages_info_params import APDCoveragesParams
from models.apd_commodities_params import APDCommoditiesParams, CommodityRecord
from models.apd_loss_history_info_params import LossHistoryInfoParams, LossHistoryRecord
from models.apd_loss_history_params import APDLossHistoryParams, SubjectivityRecord, LossHistory2Record
from models.apd_additional_info_params import APDAdditionalInformationParams

FEATURE_PATH = os.path.join(os.path.dirname(__file__), "..", "apd_tria_combined.feature")

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
    apd_loss_payee_info_page = LossPayeeInformationPage(page)
    risk_info_page = APDRiskInformationPage(page)
    apd_coverages_page = APDCoveragesPage(page)
    apd_commodities_page = APDCommoditiesPage(page)
    apd_loss_history_info_page = LossHistoryInformationPage(page)
    apd_additional_info_page = APDAdditionalInformationPage(page)
    apd_loss_history_page = LossHistoryPage(page)
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
        work_experience=test_data["Cargo_APD_Insured_UW_Info"][0]["Years of experience in same type of work"],
        non_renewal_details=test_data["Cargo_APD_Insured_UW_Info"][0][" -> Details for reasons of non-renewal"],
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

    apd_loss_payee_info = APDLossPayeeInfoParams(
        has_loss_payee = test_data["Cargo_APD_LossPayees"][0]["Does Policy Have Loss Payees (PhysDam)?"],
        loss_payees = test_data["Cargo_APD_LossPayees"],
    )

    apd_coverages_info = APDCoveragesParams(
        refrigeration_breakdown=test_data["Cargo_APD_Coverages"][0]["Refrigeration breakdown coverage required?"],
        trailer_age=test_data["Cargo_APD_Coverages"][0]["  -> Any reefer trailers older than 10 years?"],
        reefer_trailer_serviced=test_data["Cargo_APD_Coverages"][0]["  -> Reefer trailer serviced at least every 30 days?"],
        seafood=test_data["Cargo_APD_Coverages"][0]["  -> Hauls seafood or shellfish?"],
        radius=test_data["Cargo_APD_Coverages"][0]["Radius of operations (applies to Cargo and APD)"],
        phys_dam_deductible=test_data["Cargo_APD_Coverages"][0]["Physical Damage Deductible"],
        ts_limit=test_data["Cargo_APD_Coverages"][0]["Towing and Storage Limit "],
    )

    apd_commodities_info = APDCommoditiesParams(
        cargo_includes_liquor_manufactured_tobacco=test_data["Cargo_APD_Commodities"][0]["Does cargo include liquor or manufactured tobacco?"],
        cargo_includes_oversized_overweight_commodities=test_data["Cargo_APD_Commodities"][0]["Does cargo include oversized / overweight commodities?"],
        cargo_includes_excluded_commodities=test_data["Cargo_APD_Commodities"][0]["Does cargo include excluded commodities?"],
        
        commodities=[
            CommodityRecord(
            commodity=row["Commodity Name"],
            percent_of_cargo=row["% of Cargo"],
            average_value_per_load=row["Avg Value/Load ($)"],
            maximum_value_per_load=row["Max Value/Load ($)"],
            )
            for row in test_data["Cargo_APD_Commodities"]
        ]
    )

    apd_loss_history_info = LossHistoryInfoParams(
        any_losses_in_the_past_3Years=test_data["Cargo_APD_LossHistory"][0]["Any Losses in the Past 3 Years?"],
 
        losses=[LossHistoryRecord(
                loss_year=row["Loss Year"],
                type_of_loss=row["Type of Loss"],
                premium_at_time_of_loss=row["Premium at Time of Loss ($)"],
                amount_paid=row["Amount Paid ($)"],
                amount_outstanding=row["Amount Outstanding ($)"],
                other_describe=row["Loss Description (if Other)"],
            )
            for row in test_data["Cargo_APD_LossHistory"]
        ]
    )

    apd_addition_info = APDAdditionalInformationParams(
        estimated_gross_revenue_for_coming_year=test_data["Cargo_APD_Add_Info"][0]["Estimated Gross Revenue for Coming Year ($)"],
        subcontracted_total=test_data["Cargo_APD_Add_Info"][0]["Subcontracted Total ($)"],
        own_haul_total=test_data["Cargo_APD_Add_Info"][0]["Own Haul Total ($)"],
    )

    apd_loss_info = APDLossHistoryParams(
            any_losses_in_the_past3_years=test_data["Cargo_APD_LossHistory"][0]["Any Losses in the Past 3 Years?"],
            any_unrepaired_damage_from_prior_losses=test_data["Cargo_APD_LossHistory"][0]["Any Unrepaired Damage from Prior Losses?"],
            add_extra_subjectivities=test_data["Cargo_APD_LossHistory"][0]["Add extra subjectivities?"],
            notes_about_the_insured=test_data["Cargo_APD_LossHistory"][0]["Notes about the Insured"],
            subjectivity=[SubjectivityRecord(
                subjectivity_text=row["Subjectivity Text"]
                )
                for row in test_data["Cargo_APD_LossHistory"]],
            losses2=[LossHistory2Record(
                details=row["Notes"],
                loss_date=row["Loss Date"],
                amount=row["Premium at Time of Loss ($)"],
                type_of_loss=row["Type of Loss"],
                )                
                
                for row in test_data["Cargo_APD_LossHistory"]]

    )

    home_page.click_new_quote_button()
    program_selection_page.select_commercial_lines_LOB()
    commercial_lines_basic_info_page.fill_commercial_line_basic_information_PD_TRIA_combined_form()
    agency_information_page.fill_agency_information_form(agency_info)
    apd_insured_information_page.fill_apd_insured_information_form(insured_info)
    apd_additional_insured_info_page.fill_additional_insured_info(apd_additional_insured_info)
    risk_info_page.fill_risk_information(risk_info)
    apd_loss_payee_info_page.fill_apd_loss_payee_info_form(apd_loss_payee_info)
    apd_coverages_page.fill_cargo_coverages(apd_coverages_info)
    apd_commodities_page.fill_commodities(apd_commodities_info)
    apd_loss_history_info_page.fill_loss_history_info(apd_loss_history_info)
    apd_additional_info_page.fill_additional_info(apd_addition_info)
    apd_loss_history_page.fill_loss_history2_info(apd_loss_info)
    finance_quote_page.fill_finance_quote_form()


@then('the generated premium should be saved to excel')
def then_generated_premium_should_be_equal(page, test_data):
    print_your_quote_page = PrintYourQuotePage(page)
    print_your_quote_page.save_premium(test_data, "apd_tria_combined_output", "Policy_Info")
