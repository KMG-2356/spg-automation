from playwright.sync_api import Page, expect, TimeoutError
from models.DF_coverage_params import DFcoverageParams

class DFCoveragesPage:
    def __init__(self, page: Page):
        self.page = page
        self.CoverageELLimitofLiability_select = self.page.locator("[id=\"df.coverages.df_limit_of_liability\"]")
        self.LossofRentsCoverageD_select = self.page.locator("[id=\"df.coverages.df_loss_of_rents\"]")
        self.OwnersContentsCoverageC_select = self.page.locator("[id=\"df.coverages.df_owner_contents_coverage\"]")
        self.OwnersContentsBurglaryCoverage_select = self.page.locator("[id=\"df.coverages.df_burglary_coverage\"]")
        self.HomeSystemsProtection_select = self.page.locator("[id=\"df.coverages.df_home_systems_protection\"]")
        self.ServiceLineCoverage_select = self.page.locator("[id=\"df.coverages.df_service_line\"]")
        self.IdentityTheftCoverage_select = self.page.locator("[id=\"df.coverages.df_identity_theft_recovery\"]")

        self.HigherDeductibleAOP_select = self.page.locator("[id=\"ho.coverages.service_line\"]")
        self.CentralStationAlarms_select = self.page.locator("[id=\"ho.coverages.identity_theft\"]")
        self.RoofValuationEndorsement_select = self.page.locator("[id=\"ho.coverages.water_backup\"]")
        self.additional_comments_input = self.page.locator("[id=\"ho.coverages.extended_repl_cost_dwell\"]")
        
        self.DF_addition_questions_btn = self.page.get_by_role("button", name="Dwelling Fire Additional")
        self.loading_screen = self.page.locator(".jss53")


    def fill_DFcoverages_info(self, params: DFcoverageParams):
        
        self.CoverageELLimitofLiability_select.select_option(params.Coverage_E_L_Limitof_Liability)
        self.check_loading()
        self.LossofRentsCoverageD_select.select_option(params.Loss_of_Rents_CoverageD)
        self.check_loading()
        self.OwnersContentsCoverageC_select.select_option(params.Owners_Contents_CoverageC)
        self.check_loading()         
        self.OwnersContentsBurglaryCoverage_select.select_option(params.Owners_Contents_Burglary_Coverage)
        self.check_loading()
        self.HomeSystemsProtection_select.select_option(params.Home_Systems_Protection)
        self.check_loading()            
        self.ServiceLineCoverage_select.select_option(params.Service_Line_Coverage)
        self.check_loading()
        self.IdentityTheftCoverage_select.select_option(params.Identity_Theft_Coverage)
        self.check_loading()
        # self.HigherDeductibleAOP_select.select_option(params.HigherDeductibleAOP)
        # self.check_loading()
        # self.CentralStationAlarms_select.select_option(params.CentralStationAlarms)
        # self.check_loading()
        # self.RoofValuationEndorsement_select.select_option(params.RoofValuationEndorsement)
        # self.check_loading()
        # self.RoofValuationEndorsement_select.select_option(params.RoofValuationEndorsement)
        # self.check_loading()
        # self.additional_comments_input.select_option(params.AdditionalComments)
        self.check_loading()

        expect(self.DF_addition_questions_btn).to_be_visible()
        expect(self.DF_addition_questions_btn).to_be_enabled()
        self.DF_addition_questions_btn.click()

    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")