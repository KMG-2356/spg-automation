from dataclasses import dataclass

@dataclass
class HomeOwnersCoveragesParams:
    dwelling_value: str = ""
    cov_b: str = ""
    cov_c: str = ""
    cov_d: str = ""
    limit_of_liability: str = ""
    med_pay: str = ""
    home_systems_protection: str = ""
    service_line: str = ""
    identity_theft: str = ""
    water_backup: str = ""
    replacement_cost_pp: str = ""
    extended_repl_cost_dwell: str = ""
    special_comp_coverage: str = ""