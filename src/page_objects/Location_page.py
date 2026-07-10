import re
from playwright.sync_api import Page, expect

class LocationPage:
    def __init__(self, page: Page):
       
            self.page = page
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
            self.location_information_btn = self.page.get_by_role("button", name="Monoline Wind Location")
            self.add_location_button = self.page.get_by_role("button", name="Add Another Location")
        
            

    def fill_location_information_form(self,data):
        for i in range(len(data["02_WH_Locations"])):
            print("Location started")
            self.StreetAddress1_input.fill(data["02_WH_Locations"][i]["Street Address1"])
            self.StreetAddress2_input.fill(data["02_WH_Locations"][i]["Street Address 2"])
            self.city_input.fill(data["02_WH_Locations"][i]["City"])
            self.state_selection.select_option(data["02_WH_Locations"][i]["St"])
            self.zip_input.fill(str(data["02_WH_Locations"][i]["ZIP"]))
            self.interest_in_property_selection.select_option(data["02_WH_Locations"][i]["Interest in Property"])
            self.value_of_the_property_input.fill(str(data["02_WH_Locations"][i]["Building Value ($)"]))
            self.content_limits_input.fill(str(data["02_WH_Locations"][i]["Contents Limit ($)"]))
            self.business_interruption_limit_input.fill(str(data["02_WH_Locations"][i]["BI Limit ($) Max $100k"]))
            self.construction_type_selection.select_option(data["02_WH_Locations"][i]["Construction Type"])
            self.is_building_residential_selection.select_option(data["02_WH_Locations"][i]["Is Building Residential?"])
            self.distance_to_the_coast_selection.select_option(data["02_WH_Locations"][i]["Distance To Coast"])
            self.year_of_last_roof_update_input.fill(str(data["02_WH_Locations"][i]["Year of Last Roof Update"]))
            self.protection_class_selection.select_option(str(data["02_WH_Locations"][i]["Protection Class"]))
            self.number_of_stories_input.fill(str(data["02_WH_Locations"][i]["Number of Stories"]))
            self.area_of_property_input.fill(str(data["02_WH_Locations"][i]["Area(sq ft)"]))
            self.year_built_input.fill(str(data["02_WH_Locations"][i]["Year Built"]))
            self.any_prior_losses_selection.select_option(data["02_WH_Locations"][i]["Any PriorLosses?"])
            self.location_information_btn.click()

            if i < len(data["02_WH_Locations"]) - 1:
           
              self.add_location_button.click()
        # self.page.fill('input[name="agency_zip"]', "12345")
  