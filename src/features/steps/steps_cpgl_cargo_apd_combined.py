import os
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from config import *
from features.steps.steps_apd_cargo_combined import EmployerRecord, LossHistoryInformationPage
from models.apd_additional_info_params import APDAdditionalInformationParams
from models.apd_commodities_params import APDCommoditiesParams, CommodityRecord
from models.apd_insured_info_params import APDInsuredInfoParams
from models.apd_loss_history_info_params import LossHistoryInfoParams, LossHistoryRecord
from models.apd_loss_payee_info_params import APDLossPayeeInfoParams
from models.apd_risk_info_params import RiskInfoParams
from models.cargo_additional_insured_info_params import CargoAdditionalInsuredInformationParams
from models.cargo_coverage_params import CargoCoverageParams
from models.property_locations_params import PropertyLocationParams
from page_objects.apd_additional_info_page import APDAdditionalInformationPage
from page_objects.apd_commodities_page import APDCommoditiesPage
from page_objects.apd_insured_information_page import APDInsuredInformationPage
from page_objects.apd_loss_payee_info_page import LossPayeeInformationPage
from page_objects.apd_risk_information_page import APDRiskInformationPage
from page_objects.cargo_additional_insured_info_page import CargoAdditionalInsuredInformationPage
from page_objects.cargo_coverage_info_page import CargoCoveragesInformationPage
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
from page_objects.property_buliding_page import BuildingInformationPage

from models.agency_info_params import AgencyInfoParams
from models.property_insured_params import InsuredInfoParams
from models.property_building_params import BuildingInfoParams, BuildingOccupancyParams
from models.property_loss_payee_params import PropertyLossPayeeParams
from models.property_general_liability_info_params import GeneralLiabilityParams, GLRecord, AdditionalInsuredRecord
from models.cargo_loss_history2_params import SubjectivityRecord, LossHistory2Record,CargoLossHistory2Params


FEATURE_PATH = os.path.join(os.path.dirname(__file__), "..", "cpgl_cargo_apd_combined.feature")

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
    apd_insured_information_page = APDInsuredInformationPage(page)
    property_additional_questions_page = AdditionalQuestionsPage(page)
    property_location_page = PropertyLocationsPage(page)
    cargo_loss_histor2_page = LossHistoryInformation2Page(page)
    cargo_additional_insured_info_page = CargoAdditionalInsuredInformationPage(page)
    apd_loss_payee_info_page = LossPayeeInformationPage(page)
    risk_info_page = APDRiskInformationPage(page)
    cargo_coverages_page = CargoCoveragesInformationPage(page)
    apd_commodities_page = APDCommoditiesPage(page)
    apd_loss_history_info_page = LossHistoryInformationPage(page)
    apd_additional_info_page = APDAdditionalInformationPage(page)
    finance_quote_page = FinanceQuotePage(page)

    policy_row = test_data["Policy_Info"][0]
    insured_uw_row = test_data["Cargo_APD_Insured_UW_Info"][0]
    driver_row = test_data["Cargo_APD_Drivers"][0]
    coverage_row = test_data["Cargo_APD_Coverages"][0]
    commodity_row = test_data["Cargo_APD_Commodities"][0]
    loss_history_row = test_data["Cargo_APD_LossHistory"][0]
    add_info_row = test_data["Cargo_APD_Add_Info"][0]


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
        mailing_address_different=test_data["Policy_Info"][0]["Is Insured's physical address same as the mailing address?"],
        new_venture=policy_row["New Venture"],
        insured_icc=str(policy_row["Insured ICC Docket Number - MC#"]),
        filings=policy_row["Filings Required"],
        all_owned_units=policy_row["Does this quote include all owned/operated units?"],
        carrier_type=policy_row["Type of Company / Carrier"],
        own_goods=policy_row[" Insured also carry their own goods?"],
        garage_same=policy_row["Is Insured's physical address same as the mailing address?"],
        carrier_details=policy_row["Describe Carrier Details"],
        has_secondary_garage=policy_row["Secondary garaging address?"],
        secondary_garages=[policy_row[f"Garage Address#{i}"] for i in range(1, 6)],
        trustee_name=policy_row["Full Name"],
        trustee_street1=policy_row["Trustee Address -  Street 1"],
        trustee_street2=policy_row["Trustee Address  -  Street 2"],
        trustee_zip=str(policy_row["Trustee Address  -  Zip"]),
    )

    # insured_info = APDInsuredInfoParams(
    #     insured_name=policy_row["Business / Insured Name"],
    #     entity_type=policy_row["Type of Entity"],
    #     insured_email=policy_row["Insured Email Address"],
    #     insured_phone=str(policy_row["Insured Phone Number"]),
    #     mailing_street1=policy_row["Address  -  Street 1"],
    #     mailing_street2=policy_row["Address  -  Street 2"],
    #     mailing_city=policy_row["Address  -  City"],
    #     mailing_state=policy_row["Address  -  State"],
    #     mailing_zip=str(policy_row["Address  -  Zip"]),
    #     new_venture=policy_row["New Venture"],
    #     insured_icc=str(policy_row["Insured ICC Docket Number - MC#"]),
    #     filings=policy_row["Filings Required"],
    #     all_owned_units=policy_row["Does this quote include all owned/operated units?"],
    #     carrier_type=policy_row["Type of Company / Carrier"],
    #     own_goods=policy_row[" Insured also carry their own goods?"],
    #     garage_same=policy_row["Is Insured's physical address same as the mailing address?"],
    #     carrier_details=policy_row["Describe Carrier Details"],
    #     primary_garaging_street1=policy_row["Garaging Address Street 1"],
    #     primary_garaging_street2=policy_row["Garaging Address Street 2"],
    #     primary_garaging_city=policy_row["Garaging Address City"],
    #     primary_garaging_state=policy_row["Garaging Address State"],
    #     primary_garaging_zip=str(policy_row["Garaging Address Zip"]),
    #     has_secondary_garage=policy_row["Secondary garaging address?"],
    #     secondary_garages=[policy_row[f"Garage Address#{i}"] for i in range(1, 6)],
    #     trustee_name=policy_row["Full Name"],
    #     trustee_street1=policy_row["Trustee Address -  Street 1"],
    #     trustee_street2=policy_row["Trustee Address  -  Street 2"],
    #     trustee_city=policy_row["Trustee Address  -  City"],
    #     trustee_state=policy_row["Trustee Address  -  State"],
    #     trustee_zip=str(policy_row["Trustee Address  -  Zip"]),
    # )

    additional_questions_info = InsuredInfoParams(
        same_as_insured=test_data["Policy_Info"][0]["Same as Insured?"],
        contact_full_name=test_data["Policy_Info"][0]["Contact Full Name"],
        contact_email=test_data["Policy_Info"][0]["Contact Email"],
        contact_phone=test_data["Policy_Info"][0]["Contact Phone"],
        policy_term="12 Months"
    )
            
    general_liability_info = GeneralLiabilityParams(
        limit_option=test_data["GL_ClassCodes_Atrium"][0]["Limit Option"],
        years_in_business=test_data["GL_ClassCodes_Atrium"][0]["Years in Business"],
        years_of_experience=test_data["GL_ClassCodes_Atrium"][0]["Years of Experience"],  
        reno_cost=test_data["GL_VacantBuildingQ"][0]["What is the total cost of renovation? "],
        is_building_completely_vacant=test_data["GL_VacantBuildingQ"][0]["Is the building completely vacant? "],
        is_building_secured_from_unauthorized_entry=test_data["GL_VacantBuildingQ"][0]["Is the building secured from unauthorized entry? "],
        will_building_be_scheduled_demolish_policy_term=test_data["GL_VacantBuildingQ"][0]["Will the building be scheduled to be demolished during our policy term? "],
        building_currently_damaged=test_data["GL_VacantBuildingQ"][0]["Is the building currently damaged (fire or otherwise)? "],
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
            any_unrepaired_damage_from_prior_losses=test_data["CP_GL_LossHistory"][0]["Any unrepaired damage from prior losses?"],
            add_extra_subjectivities=test_data["CP_GL_LossHistory"][0]["Would you like to add extra subjectivities to the application?"],
            notes_about_the_insured=test_data["CP_GL_LossHistory"][0]["Notes"],
            subjectivity=[SubjectivityRecord(
                subjectivity_text=row["Subjectivity Text"]
                )
                for row in test_data["CP_GL_LossHistory"]],
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
            theft_sublimit=row["Theft Sublimit"],
            exc_wh_cov=row["Exclude Wind/Hail Coverage?"],
            wh_tiv_percent=row["Percentage for TIV for Wind/Hail Deductible "],
            buildings=[
                BuildingInfoParams(
                    street=building["Street Address"],
                    ZIP_code=str(building["ZIP Code"]),
                    Suite_Unit_floor=str(building["Suite/Unit/Floor"]),
                    stories_Sq_Ft=str(building["Stories"]),
                    area_sq_ft=str(building["Sq Ft"]),
                    year_built=str(building["Year Built"]),
                    construction=str(building["Construction"]),
                    slate_Wood_shake_roof=str(building["Slate/Wood Shake Roof?"]),
                    occupancy=str(building["Occupancy"]),
                    building_value=str(building["Building Value ($)"]),
                    good_condition=str(building["Good Condition?"]),
                    valuation=str(building["Valuation"]),
                    coinsurance=str(building["Coinsurance"]),
                    deductible=str(building["Deductible"]),
                    risk_uninsured=building["Is Risk Currently Uninsured?"],
                    risk_new_buidling=building["Risk New Purchase?"],
                    risk_prior_carrier=building["Prior Carrier"],
                    risk_prior_expiration_date=building["Prior Expiry Date"],
                    risk_days_wo_insurance=building["No.of Days without Insurance"],
                    unfenced_pool="No",
                    hydrant_Dist=str(building["Hydrant Dist."]),
                    dist_unit=str(building["Dist. Unit"]),
                    fire_dept=str(building["Fire Dept"]),
                    sprinkler=str(building["Sprinkler?"]),
                    central_Alarm=str(building["Central Alarm?"]),
                    roof_updated_year=str(building["Roof Updated Year"]),
                    electrical_updated_year=str(building["Electrical Updated Year"]),
                    plumbing_updated_year=str(building["Plumbing Updated Year"]),
                    HVAC_updated_year=str(building["HVAC Updated Year"]),
                    awning_limit=str(test_data["CP_OptCoverages"][i]["Awning Limit($)"]),
                    awning_valuation=str(test_data["CP_OptCoverages"][i]["Awning Valuation"]),
                    awning_coinsurance=str(test_data["CP_OptCoverages"][i]["Awning Coinsurance"]),
                    sign_limit=str(test_data["CP_OptCoverages"][i]["Sign Limit($)"]),
                    sign_valuation=str(test_data["CP_OptCoverages"][i]["Sign Valuation"]),
                    sign_coinsurance=str(test_data["CP_OptCoverages"][i]["Sign Coinsurance"]),
                    business_interruption_limit=str(test_data["CP_OptCoverages"][i]["BI Limit ($)"]),
                    business_interruption_valuation="Actual Loss Sustained",
                    business_personal_property_limit=str(test_data["CP_OptCoverages"][i]["BPP Limit ($)"]),
                    business_personal_property_valuation=str(test_data["CP_OptCoverages"][i]["BPP Valuation"]),
                    business_personal_property_coinsurance=str(test_data["CP_OptCoverages"][i]["BPP Coinsurance"]),
                    pump_and_canopy_limit=str(test_data["CP_OptCoverages"][i]["Pump and Canopy Limit($)"]),
                    pump_and_canopy_valuation=str(test_data["CP_OptCoverages"][i]["Pump and Canopy Valuation"]),
                    pump_and_canopy_coinsurance=str(test_data["CP_OptCoverages"][i]["Pump and Canopy Coinsurance"]),
                    loss_of_rents_limit=str(test_data["CP_OptCoverages"][i]["LOR Limit ($)"]),
                    loss_of_rents_valuation="Actual Loss Sustained",
                    renovation_limit=str(test_data["CP_OptCoverages"][i]["Renovation Limit($)"]),
                    renovation_valuation=str(test_data["CP_OptCoverages"][i]["Renaovation Valuation"]),
                    renovation_coinsurance=str(test_data["CP_OptCoverages"][i]["Renovation Coinsurance"]),
                    will_the_building_be_demolished=str(test_data["CP_OptCoverages"][i]["Will the building demolished?"]),
                    building_plans=str(test_data["CP_OptCoverages"][i]["Building Plans"]),
                    renovation_start_date=str(test_data["CP_OptCoverages"][i]["Renovation Start Date"]),
                    renovation_end_date=str(test_data["CP_OptCoverages"][i]["Renovation End Date"]),
                    spoilage_limit=str(test_data["CP_OptCoverages"][i]["Spoilage Limit"]),
                    spoilage_deductible=str(test_data["CP_OptCoverages"][i]["Spoilage Deductible($)"]),
                    spoilage_contamination=str(test_data["CP_OptCoverages"][i]["Spoilage Contamination?"]),
                    spoilage_power_outage=str(test_data["CP_OptCoverages"][i]["Spoilage Power Outage?"]),
                    refrigeration_maintenance_agreement=str(test_data["CP_OptCoverages"][i]["Refrigiration Maintainance Agreement"]),
                    notes=str(test_data["CP_OptCoverages"][i]["Notes"]),
                    building_occupancy=BuildingOccupancyParams(
                        vacant_is_building_100_percent_vacant=str(test_data["CP_OccupancyQ"][0][f"{BuildingInformationPage.get_vacant_prefix(building["Occupancy"])}Is the building 100% vacant?"]),
                        vacant_how_long_building_vacant=str(test_data["CP_OccupancyQ"][0][f"{BuildingInformationPage.get_vacant_prefix(building["Occupancy"])}How long has the building been vacant?"]),
                        vacant_prior_occupancy=str(test_data["CP_OccupancyQ"][0][f"{BuildingInformationPage.get_vacant_prefix(building["Occupancy"])}What was the prior occupancy?"]),
                        vacant_intended_disposition=str(test_data["CP_OccupancyQ"][0][f"{BuildingInformationPage.get_vacant_prefix(building["Occupancy"])}Intended disposition:"]),
                        vacant_building_secured=str(test_data["CP_OccupancyQ"][0][f"{BuildingInformationPage.get_vacant_prefix(building["Occupancy"])}Is the building secured (locked doors and windows)?"]),
                        vacant_building_boarded_up=str(test_data["CP_OccupancyQ"][0][f"{BuildingInformationPage.get_vacant_prefix(building["Occupancy"])}Is the building boarded up?"]),
                        vacant_building_fenced=str(test_data["CP_OccupancyQ"][0][f"{BuildingInformationPage.get_vacant_prefix(building["Occupancy"])}Is the building fenced?"]),
                        vacant_electricity_turned_off=str(test_data["CP_OccupancyQ"][0][f"{BuildingInformationPage.get_vacant_prefix(building["Occupancy"])}Has the electricity been turned off?"]),
                        vacant_gas_turned_off=str(test_data["CP_OccupancyQ"][0][f"{BuildingInformationPage.get_vacant_prefix(building["Occupancy"])}Has the gas been turned off?"]),
                        vacant_water_turned_off=str(test_data["CP_OccupancyQ"][0][f"{BuildingInformationPage.get_vacant_prefix(building["Occupancy"])}Has the water been turned off?"]),
                        vacant_plumbing_drained=str(test_data["CP_OccupancyQ"][0][f"{BuildingInformationPage.get_vacant_prefix(building["Occupancy"])}Has the plumbing been drained?"]),
                        vacant_structural_issues_or_damage=str(test_data["CP_OccupancyQ"][0][f"{BuildingInformationPage.get_vacant_prefix(building["Occupancy"])}Are there any structural issues or damage?"]),
                        vacant_undergoing_renovation_or_demolition=str(test_data["CP_OccupancyQ"][0][f"{BuildingInformationPage.get_vacant_prefix(building["Occupancy"])}Is the building undergoing renovation or demolition?"]),
                        vacant_new_purchase=str(test_data["CP_OccupancyQ"][0][f"{BuildingInformationPage.get_vacant_prefix(building["Occupancy"])}Was this a new purchase?"]),
                        vacant_purchase_date=str(test_data["CP_OccupancyQ"][0][f"{BuildingInformationPage.get_vacant_prefix(building["Occupancy"])}(If Yes to Q14) Date of purchase:"]),
                        vacant_actively_shown_or_marketed=str(test_data["CP_OccupancyQ"][0][f"{BuildingInformationPage.get_vacant_prefix(building["Occupancy"])}Is the building being actively shown / marketed?"]),
                        vacant_hazardous_materials_remaining=str(test_data["CP_OccupancyQ"][0]["Vacant Commercial — Are there hazardous materials remaining from prior use?"]) if not "residential" in str(building["Occupancy"]).lower() else "",
                        vacant_active_heating=str(test_data["CP_OccupancyQ"][0][f"{BuildingInformationPage.get_vacant_prefix(building["Occupancy"])}Is there any active heating in the building?"]),
                        vacant_estate_owned_or_in_probate=str(test_data["CP_OccupancyQ"][0]["Vacant Residential — Is the property estate-owned or in probate?"]) if "residential" in str(building["Occupancy"]).lower() else "",
                    ),
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
        details_for_reasons_of_non_renewal=insured_uw_row["Details for reasons of non-renewal"],
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
    

    home_page.click_new_quote_button()
    program_selection_page.select_commercial_lines_LOB()
    program_selection_page.save_quote_number("cp_gl_output", "Policy_Info", test_data)
    commercial_line_basic_info_page.fill_commercial_line_basic_information_cpgl_cargo_apd_combined_form(test_data)
    agency_information_page.fill_agency_information_form(agency_info)
    insured_information_page.fill_insured_information_cargo_additional_form(insured_info)
    # apd_insured_information_page.fill_apd_insured_information_form(insured_info)
    cargo_additional_insured_info_page.fill_cargo_additional_insured_info(cargo_additional_insured_info)
    risk_info_page.fill_risk_information(risk_info)
    apd_loss_payee_info_page.fill_apd_loss_payee_info_form(apd_loss_payee_info)
    cargo_coverages_page.fill_cargo_coverages_info_for_combined_apd(cargo_coverages_info)
    apd_commodities_page.fill_commodities(apd_commodities_info)
    apd_loss_history_info_page.fill_loss_history_info(apd_loss_history_info)
    apd_additional_info_page.fill_additional_info_cpgl_cargo_apd_combined(apd_addition_info)
    property_location_page.fill_locations(locations_info)
    general_information_page.fill_general_liability_info(general_liability_info)
    property_additional_questions_page.fill_additional_question_information_form(additional_questions_info)
    cargo_loss_histor2_page.fill_loss_history2_info(cpgl_loss_history2_info)
    finance_quote_page.fill_finance_quote_form()


@then('the generated premium should be saved to excel')
def then_generated_premium_should_be_equal(page, test_data):
    print_your_quote_page = PrintYourQuotePage(page)
    print_your_quote_page.save_premium(test_data, "cpgl_cargo_apd_combined_output","Policy_Info")
