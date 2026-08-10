import re
from playwright.sync_api import Page, expect

class CommercialLinesBasicInformationPage:
    def __init__(self, page: Page):
        self.page = page
        self.commercial_lines_basic_information_heading = self.page.get_by_role("heading", name="    Commercial Lines")
        self.underwriter_select = self.page.locator("[id=\"basics.assignments.underwriter\"]")
        self.assistant_select = self.page.locator("[id=\"basics.assignments.assistant\"]")
        self.property_coverage_lob_btn = self.page.get_by_text("Property Coverage")
        self.general_liability_coverage_lob_btn = self.page.get_by_text("General Liability Coverage")
        self.cargo_coverage_lob_btn = self.page.get_by_text("Cargo Coverage")
        self.physical_damage_coverage_lob_btn = self.page.get_by_text("Physical Damage Coverage")
        self.inland_marine_coverage_lob_btn = self.page.get_by_text("Inland Marine Coverage")
        self.terrorism_coverage_lob_btn = self.page.get_by_text("Terrorism Coverage")
        self.commercial_equipment_breakdown_lob_btn = self.page.get_by_text("Commercial Equipment Breakdown Coverage")
        self.home_health_care_agencies_instant_quote_general_liability_and_professional_liability_package_lob_btn = self.page.get_by_text("Home Health Care Agencies")
        self.is_this_a_renewal_select = self.page.locator("[id=\"basics.renewal.is_renewal\"]")
        self.generate_new_application_select = self.page.locator("[id=\"basics.renewal.app_required\"]")
        self.agency_information_btn = self.page.get_by_role("button", name="Agency Information")
        self.cargo_coverage_lob_radio = self.page.get_by_text("Cargo Coverage")
        self.effective_date_input = self.page.locator("#effective_date")
    
    def fill_commercial_line_basic_information_form(self,data):
        expect(self.commercial_lines_basic_information_heading).to_be_visible()
        self.underwriter_select.select_option("49") # Amy Nelson
        self.assistant_select.select_option("120") # Ashley O Neal
        self.is_this_a_renewal_select.select_option("no")
        self.generate_new_application_select.select_option("yes")
        # self.effective_date_input.fill(str(data["Policy_Info"][0]["Effective Date"]))
        self.cargo_coverage_lob_radio.click()
        expect(self.agency_information_btn).to_be_visible()
        expect(self.agency_information_btn).to_be_enabled()
        self.agency_information_btn.click()

    def fill_commercial_line_basic_information_Cargo_plus_TRIA_form(self,data):
        expect(self.commercial_lines_basic_information_heading).to_be_visible()
        self.underwriter_select.select_option("49") # Amy Nelson
        self.assistant_select.select_option("120") # Ashley O Neal
        self.is_this_a_renewal_select.select_option("no")
        self.generate_new_application_select.select_option("yes")
        # self.effective_date_input.fill(str(data["Policy_Info"][0]["Effective Date"]))
        self.cargo_coverage_lob_radio.click()
        self.terrorism_coverage_lob_btn.click()
        expect(self.agency_information_btn).to_be_visible()
        expect(self.agency_information_btn).to_be_enabled()
        self.agency_information_btn.click()

    def fill_commercial_line_basic_information_Prop_plus_GL_form(self,data):
        expect(self.commercial_lines_basic_information_heading).to_be_visible()
        self.underwriter_select.select_option("49") # Amy Nelson
        self.assistant_select.select_option("120") # Ashley O Neal
        self.is_this_a_renewal_select.select_option("no")
        self.generate_new_application_select.select_option("yes")
        # self.effective_date_input.fill(str(data["Policy_Info"][0]["Effective Date"]))
        self.property_coverage_lob_btn.click()
        self.general_liability_coverage_lob_btn.click()
        expect(self.agency_information_btn).to_be_visible()
        expect(self.agency_information_btn).to_be_enabled()
        self.agency_information_btn.click()

    def fill_commercial_line_basic_information_Property_form(self,data):
        expect(self.commercial_lines_basic_information_heading).to_be_visible()
        self.underwriter_select.select_option("49") # Amy Nelson
        self.assistant_select.select_option("120") # Ashley O Neal
        self.is_this_a_renewal_select.select_option("no")
        self.generate_new_application_select.select_option("yes")
        self.property_coverage_lob_btn.click()
        expect(self.agency_information_btn).to_be_visible()
        expect(self.agency_information_btn).to_be_enabled()
        self.agency_information_btn.click()

    def fill_commercial_line_basic_information_Property_tria_combined_form(self,data):
        expect(self.commercial_lines_basic_information_heading).to_be_visible()
        self.underwriter_select.select_option("49") # Amy Nelson
        self.assistant_select.select_option("120") # Ashley O Neal
        self.is_this_a_renewal_select.select_option("no")
        self.generate_new_application_select.select_option("yes")
        self.property_coverage_lob_btn.click()
        self.terrorism_coverage_lob_btn.click()
        expect(self.agency_information_btn).to_be_visible()
        expect(self.agency_information_btn).to_be_enabled()
        self.agency_information_btn.click()

    def fill_commercial_line_basic_information_IM_form(self):
        expect(self.commercial_lines_basic_information_heading).to_be_visible()
        self.underwriter_select.select_option("49") # Amy Nelson
        self.assistant_select.select_option("120") # Ashley O Neal
        self.is_this_a_renewal_select.select_option("no")
        self.generate_new_application_select.select_option("yes")
        self.inland_marine_coverage_lob_btn.click()
        expect(self.agency_information_btn).to_be_visible()
        expect(self.agency_information_btn).to_be_enabled()
        self.agency_information_btn.click()

    def fill_commercial_line_basic_information_PD_form(self):
        expect(self.commercial_lines_basic_information_heading).to_be_visible()
        self.underwriter_select.select_option("49") # Amy Nelson
        self.assistant_select.select_option("120") # Ashley O Neal
        self.is_this_a_renewal_select.select_option("no")
        self.generate_new_application_select.select_option("yes")
        self.physical_damage_coverage_lob_btn.click()
        expect(self.agency_information_btn).to_be_visible()
        expect(self.agency_information_btn).to_be_enabled()
        self.agency_information_btn.click()

    def fill_commercial_line_basic_information_PD_TRIA_combined_form(self):
        expect(self.commercial_lines_basic_information_heading).to_be_visible()
        self.underwriter_select.select_option("49") # Amy Nelson
        self.assistant_select.select_option("120") # Ashley O Neal
        self.is_this_a_renewal_select.select_option("no")
        self.generate_new_application_select.select_option("yes")
        self.physical_damage_coverage_lob_btn.click()
        self.terrorism_coverage_lob_btn.click()
        expect(self.agency_information_btn).to_be_visible()
        expect(self.agency_information_btn).to_be_enabled()
        self.agency_information_btn.click()

    def fill_commercial_line_basic_information_cargo_pd_combined_form(self):
        expect(self.commercial_lines_basic_information_heading).to_be_visible()
        self.underwriter_select.select_option("49") # Amy Nelson
        self.assistant_select.select_option("120") # Ashley O Neal
        self.is_this_a_renewal_select.select_option("no")
        self.generate_new_application_select.select_option("yes")
        self.physical_damage_coverage_lob_btn.click()
        self.cargo_coverage_lob_btn.click()
        expect(self.agency_information_btn).to_be_visible()
        expect(self.agency_information_btn).to_be_enabled()
        self.agency_information_btn.click()

    def fill_commercial_line_basic_information_cargo_pd_tria_combined_form(self):
        expect(self.commercial_lines_basic_information_heading).to_be_visible()
        self.underwriter_select.select_option("49") # Amy Nelson
        self.assistant_select.select_option("120") # Ashley O Neal
        self.is_this_a_renewal_select.select_option("no")
        self.generate_new_application_select.select_option("yes")
        self.physical_damage_coverage_lob_btn.click()
        self.cargo_coverage_lob_btn.click()
        self.terrorism_coverage_lob_btn.click()
        expect(self.agency_information_btn).to_be_visible()
        expect(self.agency_information_btn).to_be_enabled()
        self.agency_information_btn.click()

    def fill_commercial_line_basic_information_Prop_GL_tria_form(self,data):
        expect(self.commercial_lines_basic_information_heading).to_be_visible()
        self.underwriter_select.select_option("49") # Amy Nelson
        self.assistant_select.select_option("120") # Ashley O Neal
        self.is_this_a_renewal_select.select_option("no")
        self.generate_new_application_select.select_option("yes")
        # self.effective_date_input.fill(str(data["Policy_Info"][0]["Effective Date"]))
        self.property_coverage_lob_btn.click()
        self.general_liability_coverage_lob_btn.click()
        self.terrorism_coverage_lob_btn.click()
        expect(self.agency_information_btn).to_be_visible()
        expect(self.agency_information_btn).to_be_enabled()
        self.agency_information_btn.click()

    def fill_commercial_line_basic_information_Prop_GL_ceb_form(self,data):
        expect(self.commercial_lines_basic_information_heading).to_be_visible()
        self.underwriter_select.select_option("49") # Amy Nelson
        self.assistant_select.select_option("120") # Ashley O Neal
        self.is_this_a_renewal_select.select_option("no")
        self.generate_new_application_select.select_option("yes")
        # self.effective_date_input.fill(str(data["Policy_Info"][0]["Effective Date"]))
        self.property_coverage_lob_btn.click()
        self.commercial_equipment_breakdown_lob_btn.click()
        self.general_liability_coverage_lob_btn.click()                
        expect(self.agency_information_btn).to_be_visible()
        expect(self.agency_information_btn).to_be_enabled()
        self.agency_information_btn.click()

    def fill_commercial_line_basic_information_Prop_GL_ceb_tria_form(self,data):
            expect(self.commercial_lines_basic_information_heading).to_be_visible()
            self.underwriter_select.select_option("49") # Amy Nelson
            self.assistant_select.select_option("120") # Ashley O Neal
            self.is_this_a_renewal_select.select_option("no")
            self.generate_new_application_select.select_option("yes")
            # self.effective_date_input.fill(str(data["Policy_Info"][0]["Effective Date"]))
            self.property_coverage_lob_btn.click()
            self.commercial_equipment_breakdown_lob_btn.click()
            self.general_liability_coverage_lob_btn.click()            
            self.terrorism_coverage_lob_btn.click()
            expect(self.agency_information_btn).to_be_visible()
            expect(self.agency_information_btn).to_be_enabled()
            self.agency_information_btn.click()
            
    def fill_commercial_line_basic_information_Prop_ceb_form(self,data):
            expect(self.commercial_lines_basic_information_heading).to_be_visible()
            self.underwriter_select.select_option("49") # Amy Nelson
            self.assistant_select.select_option("120") # Ashley O Neal
            self.is_this_a_renewal_select.select_option("no")
            self.generate_new_application_select.select_option("yes")
            self.property_coverage_lob_btn.click()
            self.commercial_equipment_breakdown_lob_btn.click()
            expect(self.agency_information_btn).to_be_visible()
            expect(self.agency_information_btn).to_be_enabled()
            self.agency_information_btn.click()

    def fill_commercial_line_basic_information_cpgl_cargo_apd_combined_form(self,data):
        expect(self.commercial_lines_basic_information_heading).to_be_visible()
        self.underwriter_select.select_option("49") # Amy Nelson
        self.assistant_select.select_option("120") # Ashley O Neal
        self.is_this_a_renewal_select.select_option("no")
        self.generate_new_application_select.select_option("yes")
        self.property_coverage_lob_btn.click()
        self.general_liability_coverage_lob_btn.click()
        self.cargo_coverage_lob_btn.click()
        self.physical_damage_coverage_lob_btn.click()
        expect(self.agency_information_btn).to_be_visible()
        expect(self.agency_information_btn).to_be_enabled()
        self.agency_information_btn.click()
