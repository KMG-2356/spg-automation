import os
import re
import sys
from utils.xlsx_loader import get_test_data
from pytest_bdd import given, parsers
import pytest
import openpyxl
from config import EXCEL_FILE_PATH
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import allure
import pathlib

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    """Passes the start-maximized flag to the browser binary."""
    return {
        **browser_type_launch_args,
        "args": ["--start-maximized"],
    }

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Disables Playwright's default fixed viewport size."""
    return {
        **browser_context_args,
        "no_viewport": True
    }

def pytest_generate_tests(metafunc):
    """
    Dynamically maps Excel rows to pytest-bdd scenarios at test collection time.
    Surgically targets only files matching your step definition naming patterns.
    """
    # In Pytest 9+, metafunc.definition.path is a native pathlib.Path object
    file_name = metafunc.definition.path.name
    
    # Mirror the python_files matching rules from your pytest.ini
    if file_name.startswith("steps_") or "_steps" in file_name:
        try:
            wb = openpyxl.load_workbook(EXCEL_FILE_PATH, read_only=True)
            sheet_names = [s.title for s in wb.worksheets if s.sheet_state == "visible"]
            if not sheet_names:
                return
            
            master_sheet_name = sheet_names[0]
            df_master = pd.read_excel(EXCEL_FILE_PATH, sheet_name=master_sheet_name)
            id_column_name = df_master.columns[0]
            
            all_ids = df_master[id_column_name].dropna().unique().tolist()
            
            cli_ids = metafunc.config.getoption("--ids")
            if cli_ids:
                target_ids = [i.strip() for i in cli_ids.split(",")]
                all_ids = [x for x in all_ids if x in target_ids]
            
            cli_limit = metafunc.config.getoption("--limit")
            if cli_limit is not None:
                all_ids = all_ids[:cli_limit]
            
            if all_ids:
                metafunc.parametrize("test_data", all_ids, indirect=True, ids=lambda x: f"ID={x}")
                
        except Exception as e:
            print(f"\nWarning: Failed to dynamically generate tests from Excel: {e}")

@pytest.fixture(scope="session")
def base_url():
    return "https://rating.commund.com/"

@pytest.fixture(scope="function")
def test_data(request):
    test_case_id = request.param
    print(f"Test case ID printed from conftest{test_case_id}")
    # scenario_name = request.node.name
    # match = re.search(r'TS[-_]?(\d{3})', scenario_name, re.IGNORECASE)


    # if not match:
    #     raise ValueError(
    #         f"Execution halted: The scenario '{scenario_name}' does not contain a valid 'TS-' ID in its name! "
    #         "Please name your scenario like: 'Scenario: TS-001 - My test description'"
    #     )
    
    # test_case_id = f"TS-{match.group(1)}"

    # if not test_case_id:
    #     raise ValueError(
    #         f"Execution halted: The scenario '{request.node.name}' is missing a matching 'TS-' data tag! "
    #     )

    # excel_file_path = "src/data/TestData.xlsx"

    try:
        data_payload = get_test_data(EXCEL_FILE_PATH, test_case_id)
        return data_payload
    except Exception as e:
        pytest.fail(f"Fixture Setup Error: Failed to fetch test data for tag '{test_case_id}'. Reason: {str(e)}")


@given(parsers.parse('the login page is open for ID "{test_case_id}"'), target_fixture="test_data")
def load_dynamic_test_data(test_case_id):
    excel_file_path = "src/data/TestData.xlsx"
    
    try:
        data_payload = get_test_data(excel_file_path, test_case_id)
        return data_payload
    except Exception as e:
        import pytest
        pytest.fail(f"Step Setup Error: Failed to parse row data for '{test_case_id}'. Reason: {str(e)}")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        try:
            page = item.funcargs.get("page")
        except Exception:
            page = None

        if page:
            try:
                results_dir = pathlib.Path("allure-results")
                results_dir.mkdir(parents=True, exist_ok=True)
                file_name = f"{item.name}.png"
                file_path = results_dir / file_name
                page.screenshot(path=str(file_path))
                allure.attach.file(str(file_path), name="screenshot", attachment_type=allure.attachment_type.PNG)
            except Exception:
                pass