import os
import re
import sys
from utils.xlsx_loader import get_test_data
from pytest_bdd import given, parsers
import pytest
import openpyxl
from config import EXCEL_FILE_PATH
import pandas as pd
from playwright.sync_api import expect

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import allure
import pathlib

expect.set_options(timeout=30000)

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    """Passes the start-maximized flag to the browser binary."""
    return {
        **browser_type_launch_args,
        "args": ["--start-maximized"],
        "timeout": 60000
    }

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Disables Playwright's default fixed viewport size."""
    return {
        **browser_context_args,
        "no_viewport": True,
    }

def _resolve_excel_path(scenario_title: str) -> str:
    if not scenario_title:
        return ""

    data_dir = os.path.join("src", "data")
    
    clean_title = re.sub(r'[^a-zA-Z0-9]', '', scenario_title).lower()

    if os.path.exists(data_dir):
        for file in os.listdir(data_dir):
            if file.endswith(".xlsx"):
                stem = file.replace(".xlsx", "")
                clean_stem = re.sub(r'[^a-zA-Z0-9]', '', stem).lower()
                
                if clean_stem in clean_title:
                    return os.path.join(data_dir, file)
                    
    return ""

def _normalize_feature_token(value: str) -> str:
    return re.sub(r'[^a-z0-9]+', '', (value or '').lower())


def _matches_feature_filter(item, feature_filters):
    if not feature_filters:
        return True

    haystack_parts = [
        getattr(item, "nodeid", ""),
        getattr(item, "path", ""),
        getattr(item, "fspath", ""),
    ]
    haystack = " ".join(str(part) for part in haystack_parts if str(part))
    normalized_haystack = _normalize_feature_token(haystack)

    for feature_filter in feature_filters:
        normalized_filter = _normalize_feature_token(feature_filter)
        if normalized_filter and normalized_filter in normalized_haystack:
            return True

    return False


def pytest_collection_modifyitems(config, items):
    feature_filters = []
    for option_name in ("--feature-file",):
        feature_filters.extend(config.getoption(option_name) or [])

    if not feature_filters:
        return

    parsed_filters = []
    for raw_filter in feature_filters:
        parsed_filters.extend([value.strip() for value in raw_filter.split(",") if value.strip()])

    if not parsed_filters:
        return

    items[:] = [item for item in items if _matches_feature_filter(item, parsed_filters)]


def pytest_generate_tests(metafunc):
    if "test_data" not in metafunc.fixturenames:
        metafunc.fixturenames.append("test_data")

    scenario_obj = getattr(metafunc.function, "__scenario__", None)
    scenario_title = scenario_obj.name if scenario_obj else ""
    
    resolved_excel_path = _resolve_excel_path(scenario_title)

    if not resolved_excel_path:
        return

    try:
        wb = openpyxl.load_workbook(resolved_excel_path, read_only=True)
        sheet_names = [s.title for s in wb.worksheets if s.sheet_state == "visible"]
        if not sheet_names:
            return
        
        master_sheet_name = sheet_names[0]
        df_master = pd.read_excel(resolved_excel_path, sheet_name=master_sheet_name)
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
    return "https://internal.commund.com/"

@pytest.fixture(scope="function")
def test_data(request):
    """Retrieves specific data row payloads utilizing the running scenario's context."""
    if not hasattr(request, "param"):
        scenario_obj = getattr(request.node.obj, "__scenario__", None)
        title = scenario_obj.name if scenario_obj else request.node.name
        pytest.fail(
            f"\n[Data Router Error] Scenario '{title}' requested data, "
            f"but no excel filename matched this text inside 'src/data/' during collection."
        )

    test_case_id = request.param
    
    scenario_obj = getattr(request.node.obj, "__scenario__", None)
    scenario_title = scenario_obj.name if scenario_obj else ""
    
    resolved_excel_path = _resolve_excel_path(scenario_title)
    try:
        data_payload = get_test_data(resolved_excel_path, test_case_id)
        return data_payload
    except Exception as e:
        pytest.fail(f"Fixture Setup Error: Failed to fetch row '{test_case_id}' from '{resolved_excel_path}'. Reason: {str(e)}")

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