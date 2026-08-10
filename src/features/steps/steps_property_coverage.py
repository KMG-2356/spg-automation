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
from page_objects.property_buliding_page import BuildingInformationPage

from models.agency_info_params import AgencyInfoParams
from models.property_insured_params import InsuredInfoParams
from models.property_building_params import BuildingInfoParams, BuildingOccupancyParams
from models.property_loss_payee_params import PropertyLossPayeeParams
from models.property_general_liability_info_params import GeneralLiabilityParams, GLRecord, AdditionalInsuredRecord
from models.cargo_loss_history_info_params import LossHistoryParams,LossHistoryRecord
from models.cargo_loss_history2_params import SubjectivityRecord, LossHistory2Record,CargoLossHistory2Params


FEATURE_PATH = os.path.join(os.path.dirname(__file__), "..", "property_coverage.feature")

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
        policy_term="12 Months"
    )
            
    # general_liability_info = GeneralLiabilityParams(
    #     limit_option=test_data["GL_ClassCodes_Atrium"][0]["Limit Option"],
    #     years_in_business=test_data["GL_ClassCodes_Atrium"][0]["Years in Business"],
    #     years_of_experience=test_data["GL_ClassCodes_Atrium"][0]["Years of Experience"],  
    #     reno_cost=test_data["GL_VacantBuildingQ"][0]["What is the total cost of renovation? "],
    #     is_building_completely_vacant=test_data["GL_VacantBuildingQ"][0]["Is the building completely vacant? "],
    #     is_building_secured_from_unauthorized_entry=test_data["GL_VacantBuildingQ"][0]["Is the building secured from unauthorized entry? "],
    #     will_building_be_scheduled_demolish_policy_term=test_data["GL_VacantBuildingQ"][0]["Will the building be scheduled to be demolished during our policy term? "],
    #     building_currently_damaged=test_data["GL_VacantBuildingQ"][0]["Is the building currently damaged (fire or otherwise)? "],
    #     classification_codes=[GLRecord(class_code=row["Class Code"],
    #         square_feet_of_building=row["Square feet of building"],
    #         no_of_acres=row["No.Of Acres"]
    #         )
    #         for row in test_data["GL_ClassCodes_Atrium"]
    #         ],
    #     additional_insureds=[AdditionalInsuredRecord(
    #         AI_form=row["AI Form"],
    #         AI_name=row["AI Name"],
    #         Street1=row["Street 1"],
    #         Street2=row["Street 2"],
    #         City=row["City"],
    #         State=row["State"],
    #         ZIP=row["ZIP"],
    #         )
    #         for row in test_data["GL_AddlInsureds"]
    #         ]    
    # )
    
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
                    retail_antiques=building["Antiques? (Retail only)"],
                    retail_refrigeration=building["Refrigeration? (Retail/Warehouse)"],
                    warehouse_refrigeration=building["Refrigeration? (Retail/Warehouse)"],
                    type_of_manufacturing=building["Mfg Type (Manufacturer only)"],                          
                    desc_other_occupancy=building["Describe Occupancy (Other only)"],
                    rate_as_occupancy=building["Rate As (Other only)"],
                    renters_ins=building["Renters Ins?"],
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
                        manufacturer_desc_of_manufacturing_options=str(test_data["CP_OccupancyQ"][0]["Manufacturer — Describe the type of manufacturing:"]),
                        manufacturer_does_manufacturer_do_any_welding="No",
                        manufacturer_does_manufacturer_do_any_woodwork="No",
                        manufacturer_does_manufacturer_use_any_flammable_chemicals=str(test_data["CP_OccupancyQ"][0]["Manufacturer — Are flammable or hazardous materials used in production?"]),
                        
                        # Church
                        church_cooking=str(test_data["CP_OccupancyQ"][0]["Church — Does the church have a kitchen / cooking facilities?"]),
                        church_grills="No",
                        church_auto_extinguish="No",
                        

                        # Builders Risk
                        brisk_new_construction=str(test_data["CP_OccupancyQ"][0]["Builder's Risk — Is this new construction or renovation?"]),
                        brisk_floors_above="4",
                        brisk_floors_below="1",
                        brisk_start_date=str(test_data["CP_OccupancyQ"][0]["Builder's Risk — Estimated completion date:"]),
                        brisk_end_date=str(test_data["CP_OccupancyQ"][0]["Builder's Risk — Estimated completion date:"]),
                        brisk_lift_tilt_proto="No",
                        brisk_filled_land=str(test_data["CP_OccupancyQ"][0]["Builder's Risk — Is the building enclosed (roof and walls)?"]),
                        brisk_pilings=str(test_data["CP_OccupancyQ"][0]["Builder's Risk — Is the building occupied during construction?"]),
                        brisk_project_desc=str(test_data["CP_OccupancyQ"][0]["Builder's Risk — Name of general contractor:"]),
                        brisk_standpipe="No",
                        brisk_existing_structure=str(test_data["CP_OccupancyQ"][0]["Builder's Risk — Are subcontractors used?"]),

                        # Grocery Store
                        grocery_gas_station=str(test_data["CP_OccupancyQ"][0]["Grocery Store — Is there an in-store deli / prepared foods section?"]),
                        grocery_cooking="No",
                        # grocery_limited_cooking=str(test_data["CP_OccupancyQ"][0]["No"]),
                        # grocery_grills=str(test_data["CP_OccupancyQ"][0]["Grocery Store — (If Yes to Q8) Is there a hood suppression system for cooking equipment?"]),
                        grocery_liquor_sales="55",
                        grocery_auto_extinguish="No",
                        grocery_operations=str(test_data["CP_OccupancyQ"][0]["Grocery Store — Is this a national/regional chain or independent?"]),
                        grocery_pct_occupied="65",
                        grocery_flammable_materials="No",
                        # grocery_flammable_desc=str(test_data["CP_OccupancyQ"][0]["Grocery Store — (If Independent) Annual gross receipts ($):"]),
                        grocery_denied_insurance="No",

                        apartment_how_many_units_in_building=str(test_data["CP_OccupancyQ"][0]["Apartment — How many units in the building?"]),
                        warehouse_are_any_flammable_or_hazardous_materials_stored=str(test_data["CP_OccupancyQ"][0]["Warehouse — Are any flammable or hazardous materials stored?"]),
                        # does_this_warehouse_has_refrigerating_units=str(test_data["CP_OccupancyQ"][0]["Warehouse — Does the warehouse have refrigeration units?"]),
                        office_describe_the_type_of_office_use=str(test_data["CP_OccupancyQ"][0]["Office — Describe the type of office use:"]),
                        hotels_are_rooms_rented_on_a_longterm_basis=str(test_data["CP_OccupancyQ"][0]["Hotel — Are any units used as long-term rentals (30+ days)?"]),
                        dwelling_number_of_families=str(test_data["CP_OccupancyQ"][0]["Dwelling — Number of families:"]),                  
                        Condominium_How_many_units_in_the_building=str(test_data["CP_OccupancyQ"][0]["Condominium — How many units are currently rented?"])
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

    home_page.click_new_quote_button()
    program_selection_page.select_commercial_lines_LOB()
    commercial_line_basic_info_page.fill_commercial_line_basic_information_Prop_ceb_form(test_data)
    agency_information_page.fill_agency_information_form(agency_info)
    insured_information_page.fill_insured_information_form(insured_info)
    property_location_page.fill_locations_property(locations_info)
    property_additional_questions_page.fill_additional_question_information_form(additional_questions_info)
    cargo_loss_histor2_page.fill_loss_history2_info(cpgl_loss_history2_info)
    finance_quote_page.fill_finance_quote_form()



@then('the generated premium should be saved to excel')
def then_generated_premium_should_be_equal(page, test_data):
    print_your_quote_page = PrintYourQuotePage(page)
    print_your_quote_page.save_premium(test_data, "cp_output","Policy_Info")
