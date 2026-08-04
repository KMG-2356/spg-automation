import re
from playwright.sync_api import Page, Locator, expect, TimeoutError

from models.property_locations_params import PropertyLocationParams


class PropertyLocationsPage:
    def __init__(self, page: Page):
        self.page = page
        self.loading_screen = self.page.locator(".jss53")

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
                print(f"new location added")
                # self.fill_property_location_details(location)
            print(f"location_zip_code: {location.zip_code}")
            for j, building in enumerate(location.buildings):
                if i > 0:
                    print(f"new building added")
                print(f"building zip_code: {building.ZIP_code}")
                for k, loss_payee in enumerate(building.loss_payees):
                    if i > 0:
                        print(f"new loss payee added")
                    print(f"loss_payee zip_code: {loss_payee.zip_code}")

            


    def fill_property_location_details(self, params: PropertyLocationParams) -> None:
        idx = params.index

        self.city_input(idx).fill(params.city)
        self.state_select(idx).select_option(params.state)
        self.zip_input(idx).fill(params.zip_code)

        self.coverage_form_select(idx).select_option(params.coverage_form)

        theft_input = self.theft_sublimit_input(idx)
        if theft_input.is_visible():
            theft_input.fill(params.theft_sublimit)

        self.protection_class_select(idx).select_option(params.protection_class)
        self.inspection_fee_select(idx).select_option(params.inspection_fee)

        coastal_select = self.is_coastal_select(idx)
        if coastal_select.is_visible():
            coastal_select.select_option(params.is_coastal)

        dist_coast = self.distance_coast_select(idx)
        if dist_coast.is_visible():
            dist_coast.select_option(params.distance_coast)

        nc_island = self.nc_island_select(idx)
        if nc_island.is_visible():
            nc_island.select_option(params.nc_island)

        self.exc_wh_cov_select(idx).select_option(params.exc_wh_cov)
        self.has_hazard_select(idx).select_option(params.has_hazard)

        hazard_desc = self.hazard_desc_input(idx)
        if hazard_desc.is_visible():
            hazard_desc.fill(params.hazard_desc)

        tiv_percent = self.wh_tiv_percent_select(idx)
        if tiv_percent.is_visible():
            tiv_percent.select_option(params.wh_tiv_percent)

    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")