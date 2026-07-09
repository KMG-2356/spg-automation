import re
from playwright.sync_api import Page, expect

class LocationPage:
    def __init__(self, page: Page):

            self.StreetAddress1_input = self.page.get_by_role("textbox").first
            self.StreetAddress2_input = self.page.get_by_role("textbox").nth(1)
            self.city_input = self.page.get_by_role("textbox").nth(2)
            self.state_selection = self.page.get_by_role("combobox").first
            self.zip_input = self.page.get_by_role("textbox").nth(3)
            self.interest_in_property_selection = self.page.locator('[id="wd.locations.0.interest"]')
            self.value_of_the_property_input = self.page.locator("[id=\"wd.locations.0.dwelling_value\"]")
            self.content_limits_input = self.page.locator("[id=\"wd.locations.0.contents_limit\"]")
            self.business_interruption_limit_input = self.page.get_by_role("textbox", description="Business Interruption Limit?", exact=True)
            self.construction_type_selection = self.page.locator("[id=\"wd.locations.0.construction\"]")
            self.is_building_residential_selection = self.page.get_by_role("combobox").nth(3)
            self.distance_to_the_coast_selection = self.page.get_by_role("combobox").nth(4)
            self.year_of_last_roof_update_input = self.page.locator("[id=\"wd.locations.0.roof_update\"]")
            self.protection_class_selection = self.page.locator("[id=\"wd.locations.0.protection_class\"]")
            self.number_of_stories_input = self.page.get_by_role("spinbutton", description="Number of Stories?", exact=True)
            self.area_of_property_input = self.page.get_by_role("spinbutton", description="Area of Property?", exact=True)
            self.year_built_input = self.page.get_by_role("spinbutton", description="Year Built?", exact=True)
            self.any_prior_losses_selection = self.page.locator("[id=\"wd.locations.0.losses\"]")
            

    def fill_location_information_form(self):
            self.StreetAddress1_input.fill("streets")
            self.StreetAddress2_input.fill("street2")
            self.city_input.fill("city")
            self.state_selection.select_option("KY")
            self.zip_input.fill("1")
            self.interest_in_property_selection.select_option("Owner")
            self.value_of_the_property_input.fill("1")
            self.content_limits_input.fill("2")
            self.business_interruption_limit_input.fill("3")
            self.construction_type_selection.select_option("Joisted Masonry")
            self.is_building_residential_selection.select_option("no")
            self.distance_to_the_coast_selection.select_option("1/2 mile or less")
            self.year_of_last_roof_update_input.fill("77")
            self.protection_class_selection.select_option("3")
            self.number_of_stories_input.fill("122")
            self.area_of_property_input.fill("33")
            self.year_built_input.fill("200")
            self.any_prior_losses_selection.select_option("yes")
 
        # self.page.fill('input[name="agency_zip"]', "12345")
  