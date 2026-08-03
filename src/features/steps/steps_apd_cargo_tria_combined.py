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
from page_objects.cargo_additional_insured_info_page import CargoAdditionalInsuredInformationPage
from page_objects.cargo_coverage_info_page import CargoCoveragesInformationPage
from models.agency_info_params import AgencyInfoParams
from models.apd_additional_insured_info_params import APDAdditionalInsuredInformationParams
from models.apd_risk_info_params import RiskInfoParams
from models.apd_coverages_info_params import APDCoveragesParams
from models.apd_commodities_params import APDCommoditiesParams, CommodityRecord
from models.apd_loss_history_info_params import LossHistoryInfoParams, LossHistoryRecord
from models.apd_loss_history_params import APDLossHistoryParams, SubjectivityRecord, LossHistory2Record
from models.apd_additional_info_params import APDAdditionalInformationParams
from models.cargo_additional_insured_info_params import CargoAdditionalInsuredInformationParams, EmployerRecord
from models.cargo_coverage_params import CargoCoverageParams

FEATURE_PATH = os.path.join(os.path.dirname(__file__), "..", "apd_cargo_tria_combined.feature")

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
    cargo_additional_insured_info_page = CargoAdditionalInsuredInformationPage(page)
    apd_loss_payee_info_page = LossPayeeInformationPage(page)
    risk_info_page = APDRiskInformationPage(page)
    cargo_coverages_page = CargoCoveragesInformationPage(page)
    apd_commodities_page = APDCommoditiesPage(page)
    apd_loss_history_info_page = LossHistoryInformationPage(page)
    apd_additional_info_page = APDAdditionalInformationPage(page)
    apd_loss_history_page = LossHistoryPage(page)
    finance_quote_page = FinanceQuotePage(page)


    policy_row = test_data["Policy_Info"][0]
    insured_uw_row = test_data["Cargo_APD_Insured_UW_Info"][0]
    driver_row = test_data["Cargo_APD_Drivers"][0]
    coverage_row = test_data["Cargo_APD_Coverages"][0]
    commodity_row = test_data["Cargo_APD_Commodities"][0]
    loss_history_row = test_data["Cargo_APD_LossHistory"][0]
    add_info_row = test_data["Cargo_APD_Add_Info"][0]

    agency_info = AgencyInfoParams(
        agency_name=policy_row["Agency Name"],
        agency_id_code=policy_row["Agency ID Code"],
        agent_full_name=policy_row["Agent's Full Name"],
        agent_email=policy_row["Agent E-Mail"],
        agent_phone=policy_row["Agent Phone"],
        agent_fax=policy_row["Agent Fax"],
        agent_commission=str(policy_row["Agent's Commission"]),
        address_street1=policy_row["Agent Address Street 1"],
        address_street2=policy_row["Agent Address Street 2"],
        city=policy_row["Agent Address City"],
        state=policy_row["Agent Address State"],
        zip_code=str(policy_row["Agent Address Zip"]),
    )

    insured_info = APDInsuredInfoParams(
        insured_name=policy_row["Business / Insured Name"],
        entity_type=policy_row["Type of Entity"],
        insured_email=policy_row["Insured Email Address"],
        insured_phone=str(policy_row["Insured Phone Number"]),
        mailing_street1=policy_row["Address  -  Street 1"],
        mailing_street2=policy_row["Address  -  Street 2"],
        mailing_city=policy_row["Address  -  City"],
        mailing_state=policy_row["Address  -  State"],
        mailing_zip=str(policy_row["Address  -  Zip"]),
        new_venture=policy_row["New Venture"],
        insured_icc=str(policy_row["Insured ICC Docket Number - MC#"]),
        filings=policy_row["Filings Required"],
        all_owned_units=policy_row["Does this quote include all owned/operated units?"],
        carrier_type=policy_row["Type of Company / Carrier"],
        own_goods=policy_row[" Insured also carry their own goods?"],
        garage_same=policy_row["Is Insured's physical address same as the mailing address?"],
        carrier_details=policy_row["Describe Carrier Details"],
        primary_garaging_street1=policy_row["Garaging Address Street 1"],
        primary_garaging_street2=policy_row["Garaging Address Street 2"],
        primary_garaging_city=policy_row["Garaging Address City"],
        primary_garaging_state=policy_row["Garaging Address State"],
        primary_garaging_zip=str(policy_row["Garaging Address Zip"]),
        has_secondary_garage=policy_row["Secondary garaging address?"],
        secondary_garages=[policy_row[f"Garage Address#{i}"] for i in range(1, 6)],
        trustee_name=policy_row["Full Name"],
        trustee_street1=policy_row["Trustee Address -  Street 1"],
        trustee_street2=policy_row["Trustee Address  -  Street 2"],
        trustee_city=policy_row["Trustee Address  -  City"],
        trustee_state=policy_row["Trustee Address  -  State"],
        trustee_zip=str(policy_row["Trustee Address  -  Zip"]),
    )

    cargo_additional_insured_info = CargoAdditionalInsuredInformationParams(
        has_applicant_ever_operated_under_different_name=insured_uw_row["Has applicant ever operated under a different name?"],
        does_applicant_have_other_carrier_operations=insured_uw_row["Does applicant have other carrier operations?"],
        does_insured_subcontract_to_other_parties=insured_uw_row["Does insured subcontract to other parties?"],
        describe_other_operations=insured_uw_row["Describe other operations"],
        describe_subcontracting_lease_basis = insured_uw_row["Subcontracting basis"],
        descirbe_other_subcontrating_lease_basis = insured_uw_row["Describe other subcontracting basis"],
        years_of_experience_same_type_of_work=insured_uw_row["Years of experience in same type of work"],
        prior_employment_information_known=insured_uw_row["Prior employment information known?"],
        subcontractors_responsible_for_cargo_loss = insured_uw_row["Subcontractors responsible for cargo loss?"],
        maintains_copies_of_subcontractor_insurance=insured_uw_row["Maintains copies of subcontractor insurance?"],
        is_the_owner_also_listed_as_driver=insured_uw_row["Is the owner also listed as a driver?"],
        has_insured_had_coverage_in_the_last_3years=insured_uw_row["Has insured had coverage in the last 3 years?"],
        insurance_placed_through_commonwealth_underwriters=insured_uw_row["Insurance placed through Commonwealth Underwriters?"],
        any_insurer_canceled_non_renewed_in_last_3years=insured_uw_row["Any insurer canceled / non-renewed in last 3 years?"],
        prior_carrier_information_known=insured_uw_row["Prior carrier information known?"],
        # work_experience=insured_uw_row["Years of experience in same type of work"],
        # non_renewal_details=insured_uw_row["Details for reasons of non-renewal"],
        prior_carrier_name=insured_uw_row["Prior carrier name"],
        prior_perils_form=insured_uw_row["Prior perils form"],
        prior_policy_premium=insured_uw_row["Prior policy premium ($)"],
        prior_policy_deductible=insured_uw_row["Prior policy deductible ($)"],
        prior_policy_limit=insured_uw_row["Prior policy limit ($)"],
        prior_policy_expiration_date=insured_uw_row["Prior policy expiration date"],
        was_a_renewal_offer_made=insured_uw_row["Was a renewal offer made?"],
        consecutive_coverage_greater_than_ot_equal_to_12months=insured_uw_row["Consecutive coverage >= 12 months?"],
        employers = [EmployerRecord(
                employer_name=row["Employer Name"],
                phone=row["Phone"],
                street1=cargo_additional_insured_info_page.parse_us_address(row["Address"])["street_address"],
                city=cargo_additional_insured_info_page.parse_us_address(row["Address"])["city"],
                state=cargo_additional_insured_info_page.parse_us_address(row["Address"])["state"],
                zip_code=cargo_additional_insured_info_page.parse_us_address(row["Address"])["zip_code"],
                start_date=row["Start Date"],
                end_date=row["End Date"],
                unit_type_operated=row["Unit Type Operated"],
                commodities_hauled=row["Commodities Hauled"],
                radius=row["Radius"],
                object_to_verification=row["Object to Verification?"],
        )
        for row in test_data["Cargo_APD_Insured_UW_Info"]]
    )

    risk_info = RiskInfoParams(
        hiring_process=driver_row["Steps taken in employing new drivers"],
        firing_process=driver_row["Grounds for firing a driver?"],
        rented_equipment=insured_uw_row["Does insured lease / loan / rent equipment to others?"],
        rented_each_job=insured_uw_row["Vehicles rented for each job?"],
        titled_vehicles=insured_uw_row["All vehicles titled under named insured?"],
        secure_vehicle=insured_uw_row["Steps taken to secure vehicles"],
        owner_driven=insured_uw_row["Any vehicles driven by an owner? (PhysDam Only)"],
        inspected_vehicles=insured_uw_row["Equipment regularly inspected and serviced? (PhysDam Only)"],
        exemption_reason=insured_uw_row["Reasons for not requesting Insurance (PhysDam Only)"],
        has_extra_equipment=insured_uw_row["Owns equipment other than vehicles listed?"],
        inspection_interval=insured_uw_row["Interval (PhysDam Only)"],
        gvw=insured_uw_row["Gross Vehicle Weight of any Unit greater than 26,000 lbs?"],
        driver_experience=insured_uw_row["Any drivers have less than 2 years with a Commercial Driver's License Class A (CDL-A)"],
        drivers=test_data["Cargo_APD_Drivers"],
        vehicles=test_data["Cargo_APD_Vehicles"],
        trailers=test_data["Cargo_APD_Trailers"],
        owners=test_data["Cargo_APD_Drivers"],
    )

    apd_loss_payee_info = APDLossPayeeInfoParams(
        has_loss_payee=test_data["Cargo_APD_LossPayees"][0]["Does Policy Have Loss Payees (PhysDam)?"],
        loss_payees=test_data["Cargo_APD_LossPayees"],
    )

    cargo_coverages_info = CargoCoverageParams(
        terminal_coverage_required=test_data["Cargo_APD_Coverages"][0]["Terminal coverage required?"],
        trailer_interchange_coverage_required=test_data["Cargo_APD_Coverages"][0]["Trailer Interchange (TI) coverage required?"],
        TI_limit=test_data["Cargo_APD_Coverages"][0]["TI Limit ($)"],	
        written_TI_agreement_in_place=test_data["Cargo_APD_Coverages"][0]["Written TI agreement in place?"],
        refrigeration_breakdown_coverage_required=test_data["Cargo_APD_Coverages"][0]["Refrigeration breakdown coverage required?"],
        any_refer_trailers_older_than_10years=test_data["Cargo_APD_Coverages"][0]["Any reefer trailers older than 10 years?"],
        refer_trailer_serviced_at_least_every_30days=test_data["Cargo_APD_Coverages"][0]["Reefer trailer serviced at least every 30 days?"],
        hauls_seafood_or_shellfish=test_data["Cargo_APD_Coverages"][0]["Hauls seafood or shellfish?"],
        cargo_limit_per_unit=test_data["Cargo_APD_Coverages"][0]["Cargo limit per unit ($)"],	
        average_exposure_per_unit=test_data["Cargo_APD_Coverages"][0]["Average exposure per unit ($)"],
        maximum_exposure_per_unit=test_data["Cargo_APD_Coverages"][0]["Maximum exposure per unit ($)"],
        loads_ever_exceed_cargo_insurance_limit=test_data["Cargo_APD_Coverages"][0]["Loads ever exceed cargo insurance limit?"],
        cargo_deductible=test_data["Cargo_APD_Coverages"][0]["Cargo deductible"],
        radius_of_operations=test_data["Cargo_APD_Coverages"][0]["Radius of operations (applies to Cargo and APD)"],
        physical_damage_deductible=coverage_row["Physical Damage deductible (PhysDam only)"]
    )

    apd_commodities_info = APDCommoditiesParams(
        cargo_includes_liquor_manufactured_tobacco=commodity_row["Cargo Includes Liquor / Manufactured Tobacco?"],
        cargo_includes_oversized_overweight_commodities=commodity_row["Cargo Includes Oversized / Overweight Commodities?"],
        cargo_includes_excluded_commodities=commodity_row["Cargo Includes Excluded Commodities?"],
        commodities=[
            CommodityRecord(
                commodity=row["Commodity (Select from list)"],
                percent_of_cargo=row["Percent of Cargo (%)"],
                average_value_per_load=row["Average Value per Load ($)"],
                maximum_value_per_load=row["Maximum Value per Load ($)"],
            )
            for row in test_data["Cargo_APD_Commodities"]
        ],
    )

    apd_loss_history_info = LossHistoryInfoParams(
        any_losses_in_the_past_3Years=loss_history_row["Any Losses in the Past 3 Years?"],
        losses=[
            LossHistoryRecord(
                loss_year=row["Loss Year"],
                type_of_loss=row["Type of Loss"],
                premium_at_time_of_loss=row["Premium at Time of Loss ($)"],
                amount_paid=row["Amount Paid ($)"],
                amount_outstanding=row["Amount Outstanding ($)"],
                other_describe=row["Loss Description (if Other)"],
            )
            for row in test_data["Cargo_APD_LossHistory"]
        ],
    )

    apd_addition_info = APDAdditionalInformationParams(
        estimated_gross_revenue_for_coming_year=add_info_row["Estimated Gross Revenue for Coming Year ($)"],
        subcontracted_total=add_info_row["Subcontracted Total ($)"],
        own_haul_total=add_info_row["Own Haul Total ($)"],
    )

    apd_loss_info = APDLossHistoryParams(
        any_losses_in_the_past3_years=loss_history_row["Any Losses in the Past 3 Years?"],
        any_unrepaired_damage_from_prior_losses=loss_history_row["Any Unrepaired Damage from Prior Losses?"],
        add_extra_subjectivities=loss_history_row["Add extra subjectivities?"],
        notes_about_the_insured=loss_history_row["Notes about the Insured"],
        subjectivity=[
            SubjectivityRecord(subjectivity_text=row["Subjectivity Text"])
            for row in test_data["Cargo_APD_LossHistory"]
        ],
        losses2=[
            LossHistory2Record(
                details=row["Notes"],
                loss_date=row["Loss Date"],
                amount=row["Premium at Time of Loss ($)"],
                type_of_loss=row["Type of Loss"],
            )
            for row in test_data["Cargo_APD_LossHistory"]
        ],
    )

    home_page.click_new_quote_button()
    program_selection_page.select_commercial_lines_LOB()
    commercial_lines_basic_info_page.fill_commercial_line_basic_information_cargo_pd_tria_combined_form()
    agency_information_page.fill_agency_information_form(agency_info)
    apd_insured_information_page.fill_apd_insured_information_form(insured_info)
    cargo_additional_insured_info_page.fill_cargo_additional_insured_info(cargo_additional_insured_info)
    risk_info_page.fill_risk_information(risk_info)
    apd_loss_payee_info_page.fill_apd_loss_payee_info_form(apd_loss_payee_info)
    cargo_coverages_page.fill_cargo_coverages_info_for_combined_apd(cargo_coverages_info)
    apd_commodities_page.fill_commodities(apd_commodities_info)
    apd_loss_history_info_page.fill_loss_history_info(apd_loss_history_info)
    apd_additional_info_page.fill_additional_info(apd_addition_info)
    apd_loss_history_page.fill_loss_history2_info(apd_loss_info)
    finance_quote_page.fill_finance_quote_form()


@then('the generated premium should be saved to excel')
def then_generated_premium_should_be_equal(page, test_data):
    print_your_quote_page = PrintYourQuotePage(page)
    print_your_quote_page.save_premium(test_data, "apd_cargo_tria_combined_output", "Policy_Info")
