from playwright.sync_api import Page, expect, TimeoutError
from models.property_general_liability_info_params import GeneralLiabilityParams

class GLInformationPage:
    def __init__(self, page: Page):
        self.page = page
        self.limit_option_selection = self.page.get_by_role("combobox").first
        self.years_in_business_input = self.page.locator("[id=\"gl.years_business\"]")
        self.years_of_experience_input = self.page.locator("[id=\"gl.years_experience\"]")
        self.is_building_secured_from_unauthorized_entry_selection = self. page.locator("[id=\"gl.vacantbuilding.secured\"]")
        self.is_building_completely_vacant_selection = self.page.locator("[id=\"gl.vacantbuilding.vacant\"]")
        self.will_building_be_scheduled_demolish_policy_term_selection = self.page.locator("[id=\"gl.vacantbuilding.demolished\"]")
        self.building_currently_damaged_selection = self.page.locator("[id=\"gl.vacantbuilding.damaged\"]")
        self.any_additional_insureds_selection = self.page.locator("[id=\"gl.has_ais\"]")
        self.add_another_gl_classification_btn = self.page.get_by_role("button", name="Add Another GL Classification")       
        self.additional_questions_btn = self.page.get_by_role("button", name="Additional Questions")
        self.add_another_additional_insured_btn = self.page.get_by_role("button", name="Add Another Additional Insured")
        self.loading_screen = self.page.locator(".jss53")
    def gl_code_search_input(self, i: int):
        return self.page.locator(f"[id=\"gl.klasses.{i}._search\"]")
    def gl_code_selection(self, i: int):
        return self.page.locator(f"[id=\"gl.klasses.{i}.code\"]")
    def sq_feet_of_building_input(self, i: int):
        return self.page.locator(f"[id=\"gl.klasses.{i}.sqft\"]")
    def additional_insured_full_name_input(self, i: int):
        return self.page.locator(f"[id=\"gl.ais.{i}.name\"]")
    def type_of_AI_selection(self, i: int):
        return self.page.locator(f"[id=\"gl.ais.{i}.type\"]")
    def insured_street1_input(self, i: int):
        return self.page.get_by_text("Street Address 1Street").locator("input").nth(i * 4)
    def insured_street2_input(self, i: int):
        return self.page.get_by_text("Street Address 1Street").locator("input").nth(i * 4 + 1)
    def insured_city_input(self, i: int):
        return self.page.get_by_text("Street Address 1Street").locator("input").nth(i * 4 + 2)
    def insured_zip_input(self, i: int):
        return self.page.get_by_text("Street Address 1Street").locator("input").nth(i * 4 + 3)
    def insured_state_selection(self, i: int):
        return self.page.get_by_text("Street Address 1Street").locator("select").nth(i)
    def number_of_acres_input(self, i: int):
        return self.page.locator(f"[id=\"gl.klasses.{0}.acres\"]")
         

    def fill_general_liability_info(self, params: GeneralLiabilityParams):
        self.page.get_by_role("button", name="General Liability").click()         
        self.limit_option_selection.select_option(params.limit_option)
        self.check_loading()
        self.years_in_business_input.fill(params.years_in_business)
        self.check_loading()
        self.years_of_experience_input.fill(params.years_of_experience)
        self.check_loading()
        for i, classcode in enumerate(params.classification_codes):
            if i > 0:
                self.add_another_gl_classification_btn.click()
                self.check_loading()       
            self.gl_code_search_input(i).fill(classcode.class_code)
            self.check_loading()
            self.page.keyboard.press("Enter")
            self.gl_code_selection(i).click()
            self.page.keyboard.press("ArrowDown")
            self.page.keyboard.press("Enter")
            self.check_loading()
            self.page.wait_for_timeout(5000)
            if self.sq_feet_of_building_input(i).is_visible():
                self.sq_feet_of_building_input(i).fill(classcode.square_feet_of_building)
                self.check_loading()
            if self.number_of_acres_input(i).is_visible():
               self.number_of_acres_input(i).fill(classcode.no_of_acres)#not working  
        self.is_building_secured_from_unauthorized_entry_selection.select_option(params.is_the_building_secured_from_unauthorized_entry)
        self.is_building_completely_vacant_selection.select_option(params.is_the_building_completely_vacant)
        self.will_building_be_scheduled_demolish_policy_term_selection.select_option(params.will_building_scheduled_to_be_demolished_during_our_policy_term)
        self.building_currently_damaged_selection.select_option(params.is_the_building_currently_damaged)                      
        self.any_additional_insureds_selection.select_option("yes")

        for i, insured in enumerate(params.additional_insureds):
            if i > 0:
                self.add_another_additional_insured_btn.click()
                self.check_loading()       
            self.additional_insured_full_name_input(i).fill(insured.AI_name)
            self.check_loading()
            print(f"AI Form = '{insured.AI_form}'", flush=True)
            options = self.type_of_AI_selection(i).locator("option").evaluate_all(
                "(opts) => opts.map(o => ({label: o.textContent.trim(), value: o.value}))"
            )
            print(options, flush=True)
            self.type_of_AI_selection(i).select_option(insured.AI_form)
            self.check_loading()
            self.insured_street1_input(i).fill(insured.Street1)
            self.check_loading()
            self.insured_zip_input(i).fill(insured.ZIP)
            self.check_loading()
            self.insured_street2_input(i).fill(insured.Street2)
            self.check_loading()
            self.insured_city_input(i).fill(insured.City)
            self.check_loading()
            self.insured_state_selection(i).select_option(insured.State)
            self.check_loading()      

        expect(self.additional_questions_btn).to_be_visible()
        expect(self.additional_questions_btn).to_be_enabled()
        self.additional_questions_btn.click()

    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")   









