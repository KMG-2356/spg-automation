from playwright.sync_api import Page, expect, TimeoutError
from models.apd_risk_info_params import RiskInfoParams

class APDRiskInformationPage:
    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.hiring_process_input = self.page.locator('[id="cargo.risk_info.hiring_process"]')
        self.firing_process_input = self.page.locator('[id="cargo.risk_info.firing_process"]')
        self.add_another_driver_btn = self.page.get_by_role("button", name="Add Another Driver")
        self.add_another_power_unit_btn = self.page.get_by_role("button", name="Add Another Power Unit")
        self.has_trailers_select = self.page.locator('[id="cargo.risk_info.has_trailers"]')
        self.add_another_trailer_btn = self.page.get_by_role("button", name="Add Another Trailer")
        self.extra_equipment_select = self.page.locator('[id="cargo.risk_info.extra_equipment"]')
        self.extra_equipment_input = self.page.locator('[id="cargo.risk_info.extra_equipment"]')
        self.exemption_reasons_input = self.page.locator('[id="cargo.risk_info.exemption_reasons"]')
        self.rented_each_job_select = self.page.locator('[id="cargo.risk_info.rented_each_job"]')
        self.rented_equipment_select = self.page.locator('[id="cargo.risk_info.rented_equipment"]')
        self.titled_vehicles_select = self.page.locator('[id="cargo.risk_info.titled_vehicles"]')
        self.owner_driven_select = self.page.locator('[id="cargo.risk_info.owner_driven"]')
        self.inspected_vehicles_select = self.page.locator('[id="cargo.risk_info.inspected_vehicles"]')
        self.inspection_interval_select = self.page.locator('[id="cargo.risk_info.inspection_interval"]')
        self.gvw_select = self.page.locator('[id="cargo.risk_info.gvw"]')
        self.driver_experience_select = self.page.locator('[id="cargo.risk_info.driver_experience"]')
        self.secure_vehicles_input = self.page.locator('[id="cargo.risk_info.secure_vehicles"]')
        self.loss_payee_info_btn = self.page.get_by_role("button", name="Loss Payee Information")
        self.add_owner_btn = self.page.get_by_role("button", name="Add Another Owner")
        self.loading_screen = self.page.locator(".jss53")

    def owners_name_input(self,i):
        return self.page.locator(f"[id=\"cargo.risk_info.owners.{i}.owner_name\"]")

    def driver_name_input(self, i):
        return self.page.locator(f"[id=\"cargo.risk_info.drivers.{i}.driver_name\"]")

    def driver_dob_input(self, i):
        return self.page.locator(f"[id=\"cargo.risk_info.drivers.{i}.driver_dob\"]")

    def driver_license__number_input(self, i):
        return self.page.locator(f"[id=\"cargo.risk_info.drivers.{i}.driver_license\"]")

    def driver_license_state_select(self, i):
        return self.page.locator(f"[id=\"cargo.risk_info.drivers.{i}.driver_state\"]")

    def driver_yoe_input(self, i):
        return self.page.locator(f"[id=\"cargo.risk_info.drivers.{i}.driver_years_experience\"]")

    def driver_date_of_hire_input(self, i):
        return self.page.locator(f"[id=\"cargo.risk_info.drivers.{i}.driver_hire_date\"]")

    def driver_relationship_select(self, i):
        return self.page.locator(f"[id=\"cargo.risk_info.drivers.{i}.driver_relationship\"]")

    def driver_violation_history_select(self, i):
        return self.page.locator(f"[id=\"cargo.risk_info.drivers.{i}.is_violation_known\"]")

    def driver_minor_violations_input(self, i):
        '''condtional'''
        return self.page.locator(f"[id=\"cargo.risk_info.drivers.{i}.minor_violations\"]")

    def driver_major_viloation_input(self, i):
        '''condtional'''
        return self.page.locator(f"[id=\"cargo.risk_info.drivers.{i}.major_violations\"]")

    def driver_accidents_input(self, i):
        '''condtional'''
        return self.page.locator(f"[id=\"cargo.risk_info.drivers.{i}.accidents\"]")

    def power_unit_vehicle_year_input(self, i: int):
        return self.page.locator(f'[id="cargo.risk_info.power_units.{i}.vehicle_year"]')

    def power_unit_vehicle_make_input(self, i: int):
        return self.page.locator(f'[id="cargo.risk_info.power_units.{i}.vehicle_make"]')

    def power_unit_vehicle_type_select(self, i: int):
        return self.page.locator(f'[id="cargo.risk_info.power_units.{i}.vehicle_type"]')

    def power_unit_vehicle_cost_input(self, i: int):
        return self.page.locator(f'[id="cargo.risk_info.power_units.{i}.vehicle_cost"]')

    def power_unit_vin_known_select(self, i: int):
        return self.page.locator(f'[id="cargo.risk_info.power_units.{i}.vin_known"]')

    def power_unit_vehicle_vin_input(self, i: int):
        '''conditional'''
        return self.page.locator(f'[id="cargo.risk_info.power_units.{i}.vehicle_vin"]')

    def trailer_owned_select(self, i: int):
        return self.page.locator(f'[id="cargo.risk_info.trailers.{i}.trailer_owned"]')

    def trailer_type_select(self, i: int):
        return self.page.locator(f'[id="cargo.risk_info.trailers.{i}.trailer_type"]')

    def trailer_year_input(self, i: int):
        return self.page.locator(f'[id="cargo.risk_info.trailers.{i}.trailer_year"]')

    def trailer_make_input(self, i: int):
        return self.page.locator(f'[id="cargo.risk_info.trailers.{i}.trailer_make"]')

    def trailer_cost_input(self, i: int):
        return self.page.locator(f'[id="cargo.risk_info.trailers.{i}.trailer_cost"]')

    def trailer_vin_known_select(self, i: int):
        return self.page.locator(f'[id="cargo.risk_info.trailers.{i}.trailer_vin_known"]')

    def trailer_vin_input(self, i: int):
        '''conditional'''
        return self.page.locator(f'[id="cargo.risk_info.trailers.{i}.trailer_vin"]')


    def fill_risk_information(self, params: RiskInfoParams) -> None:
        self.hiring_process_input.fill(params.hiring_process)
        self.firing_process_input.fill(params.firing_process)

        seen_owners = set()
        owner_index = 0
        for owner in params.owners:
            owner_name = owner["Owner Name (Cargo Only)"].strip()
            if owner_name in seen_owners:
                continue
            seen_owners.add(owner_name)
            if owner_index > 0:
                self.add_owner_btn.click()
                self.check_loading()
            self.owners_name_input(owner_index).fill(owner_name)
            owner_index += 1

        for i, driver in enumerate(params.drivers):
            if i > 0:
                self.add_another_driver_btn.click()
                self.check_loading()
            self.driver_name_input(i).fill(driver["Driver Name"])
            self.driver_dob_input(i).fill(driver["Date of Birth"])
            self.driver_license__number_input(i).fill(driver["License Number"])
            self.driver_license_state_select(i).select_option(driver["License State"])
            self.check_loading()
            self.driver_yoe_input(i).fill(driver["Years of Experience"])
            self.driver_date_of_hire_input(i).fill(driver["Date of Hire"])
            self.driver_relationship_select(i).select_option(driver["Relationship"])
            self.check_loading()
            self.driver_violation_history_select(i).select_option(driver["Violation History Known?"])
            self.check_loading()
            if self.driver_minor_violations_input(i).is_visible():
                self.driver_minor_violations_input(i).fill(driver["Minor Violations Count"])
                self.driver_major_viloation_input(i).fill(driver["Major Violations Count"])
                self.driver_accidents_input(i).fill(driver["At-Fault Accidents Count"])

        for i, vehicle in enumerate(params.vehicles):
            if i > 0:
                self.add_another_power_unit_btn.click()
                self.check_loading()

            self.power_unit_vehicle_year_input(i).fill(vehicle["Vehicle Year"])
            self.power_unit_vehicle_make_input(i).fill(vehicle["Vehicle Make"])
            self.power_unit_vehicle_type_select(i).select_option(vehicle["Vehicle Type"])
            self.check_loading()
            self.power_unit_vehicle_cost_input(i).fill(vehicle["Vehicle Cost ($)"])
            self.power_unit_vin_known_select(i).select_option(vehicle["VIN Known?"])
            self.check_loading()
            
            if self.power_unit_vehicle_vin_input(i).is_visible():
                self.power_unit_vehicle_vin_input(i).fill(vehicle["VIN Number"])

        if len(params.trailers) > 0:
            self.has_trailers_select.select_option("Yes")
            self.check_loading()
            for i, trailer in enumerate(params.trailers):
                if i > 0:
                    self.add_another_trailer_btn.click()
                    self.check_loading()

                self.trailer_owned_select(i).select_option(trailer["Owned by Insured?"])
                self.check_loading()
                self.trailer_type_select(i).select_option(trailer["Trailer Type"])
                self.check_loading()
                if self.trailer_year_input(i).is_visible(): 
                    self.trailer_year_input(i).fill(trailer["Year"])
                if self.trailer_make_input(i).is_visible():
                    self.trailer_make_input(i).fill(trailer["Trailer Make"])
                self.trailer_cost_input(i).fill(trailer["Trailer Cost ($)"])

                if self.trailer_vin_known_select(i).is_visible():
                    self.trailer_vin_known_select(i).select_option(trailer["VIN Known?"])
                    self.check_loading()
                
                if self.trailer_vin_input(i).is_visible():
                    self.trailer_vin_input(i).fill(trailer["VIN Number"])
        else:
            self.has_trailers_select.select_option("No")

        self.extra_equipment_select.select_option(params.has_extra_equipment)
        self.check_loading()
        if self.exemption_reasons_input.is_visible():
            self.exemption_reasons_input.fill(params.exemption_reason)
        self.rented_each_job_select.select_option(params.rented_each_job)
        self.check_loading()
        self.rented_equipment_select.select_option(params.rented_equipment)
        self.check_loading()
        self.titled_vehicles_select.select_option(params.titled_vehicles)
        self.check_loading()
        self.owner_driven_select.select_option(params.owner_driven)
        self.check_loading()
        self.inspected_vehicles_select.select_option(params.inspected_vehicles)
        self.check_loading()
        if self.inspection_interval_select.is_visible():
            self.inspection_interval_select.select_option(params.inspection_interval)
            self.check_loading()
        self.gvw_select.select_option(params.gvw)
        self.check_loading()
        if self.driver_experience_select.is_visible():
            self.driver_experience_select.select_option(params.driver_experience)
            self.check_loading()
        self.secure_vehicles_input.fill(params.secure_vehicle)

        expect(self.loss_payee_info_btn).to_be_visible()
        expect(self.loss_payee_info_btn).to_be_enabled()
        self.loss_payee_info_btn.click()

    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")