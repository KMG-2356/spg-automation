import os
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from config import *
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage
from page_objects.program_selection_page import ProgramSelectionPage
from page_objects.commercial_lines_basic_information_page import CommercialLinesBasicInformationPage
from page_objects.agency_information_page import AgencyInformationPage
from page_objects.cargo_additional_insured_info_page import CargoAdditionalInsuredInformationPage
from page_objects.cargo_insured_info_page import CargoInsuredInformationPage
from page_objects.cargo_risk_info_page import CragoRiskInformationPage
from page_objects.cargo_coverage_info_page import CargoCoveragesInformationPage
from page_objects.cargo_commodities_page import CargoCommoditiesPage
from page_objects.cargo_additional_info_page import CargoAdditionalInformationPage
from page_objects.cargo_loss_history_page import LossHistoryInformationPage
from page_objects.cargo_loss_history2_page import LossHistoryInformation2Page
from page_objects.finance_quote_page import FinanceQuotePage
from page_objects.print_your_quote_page import PrintYourQuotePage

from models.agency_info_params import AgencyInfoParams
from models.cargo_insured_info_params import CargoInsuredInformationParams
from models.cargo_additional_insured_info_params import CargoAdditionalInsuredInformationParams, EmployerRecord
from models.cargo_coverage_params import CargoCoverageParams
from models.cargo_commodities_params import CargoCommoditiesParams,CommodityRecord
from models.cargo_additional_info_params import CargoAdditionalInformationParams
from models.cargo_loss_history_info_params import LossHistoryParams,LossHistoryRecord
from models.cargo_loss_history2_params import SubjectivityRecord, LossHistory2Record,CargoLossHistory2Params
from models.cargo_risk_info_params import RiskInfoParams

FEATURE_PATH = os.path.join(os.path.dirname(__file__), "..", "cargo_coverage.feature")

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
    cargo_additional_insured_info_page = CargoAdditionalInsuredInformationPage(page)
    cargo_risk_info_page = CragoRiskInformationPage(page)
    insured_information_page = CargoInsuredInformationPage(page)
    cargo_coverages_page = CargoCoveragesInformationPage(page)
    cargo_commodities_page = CargoCommoditiesPage(page)
    cargo_additional_info_page = CargoAdditionalInformationPage(page)
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

    insured_info = CargoInsuredInformationParams(
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

    cargo_additional_insured_info = CargoAdditionalInsuredInformationParams(
        has_applicant_ever_operated_under_different_name=test_data["Cargo_APD_Insured_UW_Info"][0]["Has applicant ever operated under a different name?"],
        does_applicant_have_other_carrier_operations=test_data["Cargo_APD_Insured_UW_Info"][0]["Does applicant have other carrier operations?"],
        describe_other_operations=test_data["Cargo_APD_Insured_UW_Info"][0]["Describe other operations"],
        does_insured_subcontract_to_other_parties=test_data["Cargo_APD_Insured_UW_Info"][0]["Does insured subcontract to other parties?"],
        Subcontracting_basis=test_data["Cargo_APD_Insured_UW_Info"][0]["Subcontracting basis"],
        describe_subcontracting_lease_basis=test_data["Cargo_APD_Insured_UW_Info"][0]["Describe other subcontracting basis"],
        subcontractors_responsible_for_cargo_loss=test_data["Cargo_APD_Insured_UW_Info"][0]["Subcontractors responsible for cargo loss?"],
        maintains_copies_of_subcontractor_insurance=test_data["Cargo_APD_Insured_UW_Info"][0]["Maintains copies of subcontractor insurance?"],
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
        prior_employment_information_known=test_data["Cargo_APD_Insured_UW_Info"][0]["Prior employment information known?"],
        years_of_experience_same_type_of_work=test_data["Cargo_APD_Insured_UW_Info"][0]["Years of experience in same type of work"],
        details_for_reasons_of_non_renewal=test_data["Cargo_APD_Insured_UW_Info"][0]["Details for reasons of non-renewal"],
        employers = [EmployerRecord(
                employer_name=row["Employer Name"],
                phone=row["Phone"],
                street1=row["Street"],
                city=row["City"],
                state=row["State"],
                zip_code=row["ZIP"],
                start_date=row["Start Date"],
                end_date=row["End Date"],
                unit_type_operated=row["Unit Type Operated"],
                commodities_hauled=row["Commodities Hauled"],
                radius=row["Radius"],
                object_to_verification=row["Object to Verification?"],
        )
        for row in test_data["Cargo_APD_Insured_UW_Info"]]
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
    )

    cargo_commodities_info = CargoCommoditiesParams(
        cargo_includes_liquor_manufactured_tobacco=test_data["Cargo_APD_Commodities"][0]["Does cargo include liquor or manufactured tobacco?"],
        cargo_includes_oversized_overweight_commodities=test_data["Cargo_APD_Commodities"][0]["Does cargo include oversized / overweight commodities?"],
        cargo_includes_excluded_commodities=test_data["Cargo_APD_Commodities"][0]["Does cargo include excluded commodities?"],
        
        commodities=[CommodityRecord(
            commodity=row["Commodity Name"],
            percent_of_cargo=row["% of Cargo"],
            average_value_per_load=row["Avg Value/Load ($)"],
            maximum_value_per_load=row["Max Value/Load ($)"],
        )
        for row in test_data["Cargo_APD_Commodities"]
    ]
    )
    cargo_loss_history_info = LossHistoryParams(
        any_losses_in_the_past_3Years=test_data["Cargo_APD_LossHistory"][0]["Any Losses in the Past 3 Years?"],
 
        losses=[LossHistoryRecord(
            loss_year=row["Loss Year"],
            type_of_loss=row["Type of Loss"],
            premium_at_time_of_loss=row["Premium at Time of Loss ($)"],
            amount_paid=row["Amount Paid ($)"],
            amount_outstanding=row["Amount Outstanding ($)"],
        )
        for row in test_data["Cargo_APD_LossHistory"]
    ]

    )
    cargo_loss_history2_info = CargoLossHistory2Params(
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
                amount=row["Amount"],
                type_of_loss=row["Type of Loss"],
                
                )                
                
                for row in test_data["Cargo_APD_LossHistory"]]
        
    )

    cargo_add_info = CargoAdditionalInformationParams(
        own_haul_total=test_data["Cargo_APD_Add_Info"][0]["Own Haul Total ($)"],
        subcontracted_total=test_data["Cargo_APD_Add_Info"][0]["Subcontracted Total ($)"],
        estimated_gross_revenue_for_coming_year=test_data["Cargo_APD_Add_Info"][0]["Estimated Gross Revenue for Coming Year ($)"]
    )

    risk_info = RiskInfoParams(
        hiring_process=test_data["Cargo_APD_Drivers"][0]["Steps taken in employing new drivers"],
        firing_process=test_data["Cargo_APD_Drivers"][0]["Grounds for firing a driver?"],
        rented_equipment=test_data["Cargo_APD_Insured_UW_Info"][0]["Does insured lease / loan / rent equipment to others?"],
        rented_each_job=test_data["Cargo_APD_Insured_UW_Info"][0]["Vehicles rented for each job?"],
        titled_vehicles=test_data["Cargo_APD_Insured_UW_Info"][0]["All vehicles titled under named insured?"],
        secure_vehicle=test_data["Cargo_APD_Insured_UW_Info"][0]["Steps taken to secure vehicles"],
        # owner_driven=test_data["Cargo_APD_Insured_UW_Info"][0]["Any vehicles driven by an owner? (PhysDam Only)"],
        # inspected_vehicles=test_data["Cargo_APD_Insured_UW_Info"][0]["Equipment regularly inspected and serviced? (PhysDam Only)"],
        # exemption_reason=test_data["Cargo_APD_Insured_UW_Info"][0]["     -> Reasons for not requesting Insurance (PhysDam Only)"],
        has_extra_equipment=test_data["Cargo_APD_Insured_UW_Info"][0]["Owns equipment other than vehicles listed?"],
        # inspection_interval=test_data["Cargo_APD_Insured_UW_Info"][0]["     -> Interval (PhysDam Only)"],
        gvw=test_data["Cargo_APD_Insured_UW_Info"][0]["Gross Vehicle Weight of any Unit greater than 26,000 lbs?"],
        driver_experience=test_data["Cargo_APD_Insured_UW_Info"][0]["Any drivers have less than 2 years with a Commercial Driver's License Class A (CDL-A)"],
        owners=test_data["Cargo_APD_Drivers"],
        drivers=test_data["Cargo_APD_Drivers"],
        vehicles=test_data["Cargo_APD_Vehicles"],
    )


    home_page.click_new_quote_button()
    program_selection_page.select_commercial_lines_LOB()
    commercial_line_basic_info_page.fill_commercial_line_basic_information_form(test_data)
    agency_information_page.fill_agency_information_form(agency_info)
    insured_information_page.fill_cargo_insured_info(insured_info)
    cargo_additional_insured_info_page.fill_cargo_additional_insured_info(cargo_additional_insured_info)
    cargo_risk_info_page.fill_risk_information(risk_info)
    cargo_coverages_page.fill_cargo_coverages_info(cargo_coverages_info)
    cargo_commodities_page.fill_commodities(cargo_commodities_info)
    cargo_loss_history_info_page.fill_loss_history_info(cargo_loss_history_info)
    cargo_additional_info_page.fill_additional_info(cargo_add_info)
    cargo_loss_histor2_page.fill_loss_history2_info(cargo_loss_history2_info)
    finance_quote_page.fill_finance_quote_form()



@then('the generated premium should be saved to excel')
def then_generated_premium_should_be_equal(page, test_data):
    print_your_quote_page = PrintYourQuotePage(page)
    print_your_quote_page.save_premium(test_data, "cargo_output","Policy_Info")
