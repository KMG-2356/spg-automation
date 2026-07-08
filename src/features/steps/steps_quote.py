import os

import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from config import *
from page_objects.quote_page import QuotePage

FEATURE_PATH = os.path.join(os.path.dirname(__file__), "..", "login.feature")

scenarios(FEATURE_PATH)

@pytest.fixture
def login_page(page):
    return LoginPage(page)


@given('the login page is open')
def given_login_page_open(login_page, base_url):
    login_page.navigate(base_url)
    return login_page


@when('the user logs in with valid user')
def when_user_logs_in(login_page):
    login_page.login(USERNAME, PASSWORD)


@then('the login should be successfull')
def then_login_should_be(login_page):
    login_page.is_logged_in()
