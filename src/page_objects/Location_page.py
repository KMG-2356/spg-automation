import re
from playwright.sync_api import Page, expect, TimeoutError

class LocationPage:
    def __init__(self, page: Page):
       
            self.page = page
            self.street_address1_input = self.page.get_by_role("textbox").first
            self.street_address2_input = self.page.get_by_role("textbox").nth(1)
            self.city_input = self.page.get_by_role("textbox").nth(2)
            self.state_selection = self.page.get_by_role("combobox").first
            self.zip_input = self.page.get_by_role("textbox").nth(3)
            self.business_interruption_limit_input = self.page.get_by_role("textbox", description="Business Interruption Limit?", exact=True)
            self.distance_to_the_coast_selection1 = self.page.get_by_role("combobox").nth(4)
            self.distance_to_the_coast_selection2 = self.page.get_by_role("combobox").nth(5)
            self.number_of_stories_input = self.page.get_by_role("spinbutton", description="Number of Stories?", exact=True)
            self.area_of_property_input = self.page.get_by_role("spinbutton", description="Area of Property?", exact=True)
            self.year_built_input = self.page.get_by_role("spinbutton", description="Year Built?", exact=True)
            self.location_information_btn = self.page.get_by_role("button",name=re.compile(r"Monoline Wind Location \d+$")).first
            self.location_management_btn = self.page.get_by_role("button",name="Monoline Wind Location Management")
            self.add_location_button = self.page.get_by_role("button", name="Add Another Location")
            self.monoline_wind_location_heading = self.page.get_by_role("heading", name="    Monoline Wind")
            self.loading_screen = self.page.locator(".jss53")


    def interest_in_property_selection(self, i):
        return self.page.locator(f'[id="wd.locations.{i}.interest"]')
    def value_of_the_property_input(self, i):
        return self.page.locator(f'[id="wd.locations.{i}.dwelling_value"]')
    def content_limits_input(self, i):
        return self.page.locator(f'[id="wd.locations.{i}.contents_limit"]')
    def construction_type_selection(self, i):
        return self.page.locator(f'[id="wd.locations.{i}.construction"]')
    def year_of_last_roof_update_input(self, i):
        return self.page.locator(f'[id="wd.locations.{i}.roof_update"]')
    def protection_class_selection(self, i):
        return self.page.locator(f'[id="wd.locations.{i}.protection_class"]')
    def any_prior_losses_selection(self, i):
        return self.page.locator(f'[id="wd.locations.{i}.losses"]')  
    def type_of_occupancy_selection(self, i):
        return self.page.locator(f'[id=\"wd.locations.{i}.residential\"]')
    def is_building_residential_selection(self, i):
        return self.page.locator(f'[id="wd.locations.{i}.occupancy"]')          
    

    def fill_location_information_form(self,data):
        expect(self.monoline_wind_location_heading).to_be_visible()
        for i in range(len(data["02_WH_Locations"])):
            self.zip_input.fill(str(data["02_WH_Locations"][i]["ZIP"]))
            self.check_loading()
            self.street_address1_input.fill(data["02_WH_Locations"][i]["Street Address1"])
            self.street_address2_input.fill(data["02_WH_Locations"][i]["Street Address 2"])
            self.city_input.fill(data["02_WH_Locations"][i]["City"])
            self.state_selection.select_option(data["02_WH_Locations"][i]["St"])
            self.check_loading()
            self.interest_in_property_selection(i).select_option(data["02_WH_Locations"][i]["Interest in Property"])
            self.check_loading()
            self.value_of_the_property_input(i).fill(str(data["02_WH_Locations"][i]["Building Value ($)"]))
            self.content_limits_input(i).fill(str(data["02_WH_Locations"][i]["Contents Limit ($)"]))
            self.business_interruption_limit_input.fill(str(data["02_WH_Locations"][i]["BI Limit ($) Max $100k"]))
            self.construction_type_selection(i).select_option(data["02_WH_Locations"][i]["Construction Type"])
            self.check_loading()
            self.is_building_residential_selection(i).select_option(data["02_WH_Locations"][i]["Is Building Residential?"])
            self.check_loading()
            if data["02_WH_Locations"][i]["Is Building Residential?"]=="Yes":
               self.distance_to_the_coast_selection2.select_option(data["02_WH_Locations"][i]["Distance To Coast"])
               self.check_loading()
            if data["02_WH_Locations"][i]["Is Building Residential?"]=="No":
               self.distance_to_the_coast_selection1.select_option(data["02_WH_Locations"][i]["Distance To Coast"].strip())
               self.check_loading()
            if self.type_of_occupancy_selection(i).is_visible():
               self.type_of_occupancy_selection(i).select_option(data["02_WH_Locations"][i]["Type of Occupancy"])
               self.check_loading()

            self.year_of_last_roof_update_input(i).fill(str(data["02_WH_Locations"][i]["Year of Last Roof Update"]))
            self.protection_class_selection(i).select_option(str(data["02_WH_Locations"][i]["Protection Class"]))
            self.check_loading()
            self.number_of_stories_input.fill(str(data["02_WH_Locations"][i]["Number of Stories"]))
            self.area_of_property_input.fill(str(data["02_WH_Locations"][i]["Area(sq ft)"]))
            self.year_built_input.fill(str(data["02_WH_Locations"][i]["Year Built"]))
            self.any_prior_losses_selection(i).select_option(data["02_WH_Locations"][i]["Any PriorLosses?"])
            expect(self.location_management_btn).to_be_visible()
            expect(self.location_management_btn).to_be_enabled()
            self.location_management_btn.click()
            self.check_loading()

            if i < len(data["02_WH_Locations"]) - 1:
              expect(self.add_location_button).to_be_visible()
              expect(self.add_location_button).to_be_enabled()
              self.add_location_button.click()

    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")
  