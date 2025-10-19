import time

import pytest

from playwright.sync_api import sync_playwright

import os, sys

from config import CONFIG
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.register_page import RegisterPage
from utils.common_methods import element_loaded, log_location
from utils.data_generaters import generate_user_name

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context(
        locale="en-US" )
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture()
def account_overview_page(page, admin_page_ready):
    user_name = generate_user_name()
    print(f"Printing from {log_location()} :\n{user_name}")

    main_page=admin_page_ready

    register_page = RegisterPage(page)
    assert register_page.register(user_name) == "Welcome "+user_name
    account_overview_page=main_page.select_tab_in_side_panel("Accounts Overview")
    return account_overview_page


@pytest.fixture()
def admin_page_ready(page):
    page.goto(CONFIG["base_url"])
    main_page = MainPage(page)
    admin_page = main_page.select_tab_in_side_header_panel("Admin Page")
    assert admin_page.get_text_of_h1() == "Administration"
    admin_page.set_initial_balance("1000")
    admin_page.set_min_balance("0")
   # admin_page.submit_btn()
    assert admin_page.submit_button() == "Settings saved successfully."
    return main_page
