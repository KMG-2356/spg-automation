import os
import re
import sys
from utils.xlsx_loader import get_test_data
from pytest_bdd import given, parsers

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import pytest

pytest_plugins = ["pytest_playwright"]

import allure
import pathlib


@pytest.fixture(scope="session")
def base_url():
    return "https://rating.commund.com/"

@pytest.fixture(scope="function")
def test_data(request):
    test_case_id = None
    scenario_name = request.node.name
    match = re.search(r'TS[-_]?(\d{2})[-_]?(\d{2})', scenario_name, re.IGNORECASE)

    if not match:
        raise ValueError(
            f"Execution halted: The scenario '{scenario_name}' does not contain a valid 'TS-' ID in its name! "
            "Please name your scenario like: 'Scenario: TS-01-01 - My test description'"
        )
    
    test_case_id = f"TS-{match.group(1)}-{match.group(2)}"
            
    if not test_case_id:
        raise ValueError(
            f"Execution halted: The scenario '{request.node.name}' is missing a matching 'TS-' data tag! "
        )

    excel_file_path = "src/data/TestData.xlsx"

    try:
        data_payload = get_test_data(excel_file_path, test_case_id)
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
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        # try to attach a Playwright `page` screenshot if available
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
                # save screenshot to file
                page.screenshot(path=str(file_path))
                # attach to Allure report
                allure.attach.file(str(file_path), name="screenshot", attachment_type=allure.attachment_type.PNG)
            except Exception:
                # best-effort, do not fail the test hook if screenshot capture fails
                pass