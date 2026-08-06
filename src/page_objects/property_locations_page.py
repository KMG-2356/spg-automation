import re
from playwright.sync_api import Page, Locator, expect, TimeoutError

from models.property_locations_params import PropertyLocationParams
from page_objects.property_buliding_page import BuildingInformationPage


class PropertyLocationsPage:
    def __init__(self, page: Page):
        self.page = page
        self.building_page = BuildingInformationPage(self.page)
        self.add_location_btn = self.page.get_by_role("button", name="Add Another Location")
        self.add_building_btn = self.page.get_by_role("button", name="Add Another Building").nth(-1)
        self.location_heading = self.page.get_by_role("heading", name="    Location")
        self.packaging_quote_gl_btn = self.page.get_by_role("button", name="Package Quote GL Suggestions")
        self.location_management_btn = self.page.get_by_role("button", name="Location Management")
        self.loading_screen = self.page.locator(".jss53")

    def building_btn(self, i):
        return self.page.get_by_role("button", name=f"Building {i+1}-")

    def city_input(self, i: int = 0) -> Locator:
        return self.page.locator(".MuiGrid-item").filter(has_text="City, state and zipcode of location").nth(4).locator("input").nth(0)

    def state_select(self, i: int = 0) -> Locator:
        return self.page.locator(".MuiGrid-item").filter(has_text="City, state and zipcode of location").nth(4).locator("select").nth(0)

    def zip_input(self, i: int = 0) -> Locator:
        return self.page.locator(".MuiGrid-item").filter(has_text="City, state and zipcode of location").nth(4).locator("input").nth(1)

    def coverage_form_select(self, i: int = 0) -> Locator:
        return self.page.locator(f'[id="property_.locations.{i}.coverage_form"]')

    def theft_sublimit_input(self, i: int = 0) -> Locator:
        return self.page.locator(f'[id="property_.locations.{i}.theft_sublimit"]')

    def protection_class_select(self, i: int = 0) -> Locator:
        return self.page.locator(f'[id="property_.locations.{i}.protection_class"]')

    def inspection_fee_select(self, i: int = 0) -> Locator:
        return self.page.locator(f'[id="property_.locations.{i}.inspection_fee"]')

    def is_coastal_select(self, i: int = 0) -> Locator:
        return self.page.locator(f'[id="property_.locations.{i}.is_coastal"]')

    def distance_coast_select(self, i: int = 0) -> Locator:
        return self.page.locator(f'[id="property_.locations.{i}.distance_coast_other"]')

    def distance_coast_nc_select(self, i: int = 0) -> Locator:
        return self.page.locator(f'[id="property_.locations.{i}.distance_coast_nc"]')
    
    def nc_island_select(self, i: int = 0) -> Locator:
        return self.page.locator(f'[id="property_.locations.{i}.nc_island"]')

    def exc_wh_cov_select(self, i: int = 0) -> Locator:
        return self.page.locator(f'[id="property_.locations.{i}.exc_wh_cov"]')

    def has_hazard_select(self, i: int = 0) -> Locator:
        return self.page.locator(f'[id="property_.locations.{i}.has_hazard"]')

    def hazard_desc_input(self, i: int = 0) -> Locator:
        return self.page.locator(f'[id="property_.locations.{i}.hazard_desc"]')

    def wh_tiv_percent_select(self, i: int = 0) -> Locator:
        return self.page.locator(f'[id="property_.locations.{i}.wh_tiv_percent"]')


    def fill_locations(self, locations: list[PropertyLocationParams]):
        for i, location in enumerate(locations):
            if i > 0:
                self.add_location_btn.click()
                self.check_loading()

            self.fill_property_location_details(location)
            self.check_loading()
            self.building_btn(i).click()
            self.check_loading()
            for j, building in enumerate(location.buildings):
                if j > 0:
                    self.add_building_btn.click()
                self.building_page.fill_building_information_form(building, i, j)
                self.check_loading()
                self.location_management_btn.click() # replace with fill_building_info method
        self.packaging_quote_gl_btn.click()

    def fill_property_location_details(self, params: PropertyLocationParams) -> None:
        expect(self.location_heading).to_be_visible()
        idx = params.index

        self.city_input(idx).fill(params.city)
        self.state_select(idx).select_option(params.state)
        self.check_loading()
        self.zip_input(idx).fill(params.zip_code)

        self.coverage_form_select(idx).select_option(params.coverage_form)
        self.check_loading()

        theft_input = self.theft_sublimit_input(idx)
        if theft_input.is_visible():
            theft_input.fill(params.theft_sublimit)

        self.protection_class_select(idx).select_option(params.protection_class)
        self.check_loading()
        self.inspection_fee_select(idx).select_option(params.inspection_fee)
        self.check_loading()
        coastal_select = self.is_coastal_select(idx)
        if coastal_select.is_visible():
            coastal_select.select_option(params.is_coastal)
            self.check_loading()


        dist_coast = self.distance_coast_select(idx)
        if dist_coast.is_visible():
            dist_coast.select_option(params.distance_coast)
            self.check_loading()

        if self.distance_coast_nc_select(idx).is_visible():
            self.distance_coast_nc_select(idx).select_option(params.distance_coast)
            self.check_loading()

        nc_island = self.nc_island_select(idx)
        if nc_island.is_visible():
            nc_island.select_option(params.nc_island)
            self.check_loading()

        self.exc_wh_cov_select(idx).select_option(params.exc_wh_cov)
        self.check_loading()
        self.has_hazard_select(idx).select_option(params.has_hazard)
        self.check_loading()

        hazard_desc = self.hazard_desc_input(idx)
        if hazard_desc.is_visible():
            hazard_desc.fill(params.hazard_desc)

        tiv_percent = self.wh_tiv_percent_select(idx)
        if tiv_percent.is_visible():
            tiv_percent.select_option(params.wh_tiv_percent)
            self.check_loading()


    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")