import time

import pytest

from utils.common_methods import assert_is_true

@pytest.mark.register_new_user
def test_register_login(page, account_overview_page):
    print("\ntest_register_login::")
    assert assert_is_true(account_overview_page.get_text_of_h1(), "Accounts Overview")

def test_account_count(page, account_overview_page):
    print("\ntest_account_count::")
    assert assert_is_true(account_overview_page.get_text_of_h1(), "Accounts Overview")
    assert assert_is_true(account_overview_page.get_number_of_accounts(), 1)

def test_balances_for_initial_account(page, account_overview_page):
    print("\ntest_balances_for_initial_account::")

    assert assert_is_true(account_overview_page.get_text_of_h1(), "Accounts Overview")
    assert assert_is_true(account_overview_page.get_number_of_accounts(), 1)
    account_number_checking = account_overview_page.get_account_numbers()
    assert account_overview_page.verify_amount_value_based_col_name(account_number_checking, "$1000.00", "Balance")
    assert account_overview_page.verify_amount_value_based_col_name(account_number_checking, "$1000.00",
                                                                    "Available Amount")
    assert assert_is_true(account_overview_page.get_total_amount(), "Total$1000.00")

@pytest.mark.open_new_account
def test_open_new_account(page, account_overview_page):
    print("\ntest_open_new_account::")

    assert assert_is_true(account_overview_page.get_text_of_h1(), "Accounts Overview" )
    assert assert_is_true(account_overview_page.get_number_of_accounts(), 1)
    account_number_checking=account_overview_page.get_account_numbers()
    assert account_overview_page.verify_amount_value_based_col_name(account_number_checking, "$1000.00", "Balance")
    assert account_overview_page.verify_amount_value_based_col_name(account_number_checking,  "$1000.00", "Available Amount" )
    assert assert_is_true(account_overview_page.get_total_amount(), "Total$1000.00")

    open_new_account_page = account_overview_page.select_tab_in_side_panel("Open New Account")
    assert assert_is_true(open_new_account_page.get_text_of_h1(), "Open New Account" )
    open_new_account_page.select_account_type("SAVINGS")
    assert assert_is_true(open_new_account_page.get_selected_option(),"SAVINGS")
    assert assert_is_true(open_new_account_page.click_open_new_acc_btn(), "Account Opened!")
    account_number_savings= open_new_account_page.get_new_account_number_from_result()
    account_overview_page=open_new_account_page.select_tab_in_side_panel("Accounts Overview")
    assert assert_is_true(account_overview_page.get_text_of_h1(), "Accounts Overview")
    assert assert_is_true(account_overview_page.get_number_of_accounts(), 2)
    time.sleep(1)  # Used for demo purposes only
    assert account_overview_page.verify_amount_value_based_col_name(account_number_checking, "$1000.00", "Balance")
    assert account_overview_page.verify_amount_value_based_col_name(account_number_checking, "$1000.00", "Available Amount")

    assert account_overview_page.verify_amount_value_based_col_name(account_number_savings, "$0.00", "Balance")
    assert account_overview_page.verify_amount_value_based_col_name(account_number_savings, "$0.00","Available Amount")
    assert assert_is_true(account_overview_page.get_total_amount(), "Total$1000.00")

@pytest.mark.transfer_funds
def test_transfer_funds(page, account_overview_page):
    print("\ntest_transfer_funds::")

    assert assert_is_true(account_overview_page.get_text_of_h1(), "Accounts Overview")
    assert assert_is_true(account_overview_page.get_number_of_accounts(), 1)
    account_number_checking = account_overview_page.get_account_numbers()
    assert account_overview_page.verify_amount_value_based_col_name(account_number_checking, "$1000.00", "Balance")
    assert account_overview_page.verify_amount_value_based_col_name(account_number_checking, "$1000.00",
                                                                    "Available Amount")
    assert assert_is_true(account_overview_page.get_total_amount(), "Total$1000.00")

    open_new_account_page = account_overview_page.select_tab_in_side_panel("Open New Account")
    assert assert_is_true(open_new_account_page.get_text_of_h1(), "Open New Account")
    open_new_account_page.select_account_type("SAVINGS")
    assert assert_is_true(open_new_account_page.get_selected_option(), "SAVINGS")
    assert assert_is_true(open_new_account_page.click_open_new_acc_btn(), "Account Opened!")
    account_number_savings = open_new_account_page.get_new_account_number_from_result()
    account_overview_page = open_new_account_page.select_tab_in_side_panel("Accounts Overview")
    assert assert_is_true(account_overview_page.get_text_of_h1(), "Accounts Overview")
    assert assert_is_true(account_overview_page.get_number_of_accounts(), 2)
    time.sleep(1) # Used for demo purposes only
    assert account_overview_page.verify_amount_value_based_col_name(account_number_checking, "$1000.00", "Balance")
    assert account_overview_page.verify_amount_value_based_col_name(account_number_checking, "$1000.00",
                                                                    "Available Amount")

    assert account_overview_page.verify_amount_value_based_col_name(account_number_savings, "$0.00", "Balance")
    assert account_overview_page.verify_amount_value_based_col_name(account_number_savings, "$0.00", "Available Amount")
    assert assert_is_true(account_overview_page.get_total_amount(), "Total$1000.00")

    transfer_funds_page=account_overview_page.select_tab_in_side_panel("Transfer Funds")
    assert assert_is_true(transfer_funds_page.get_text_of_h1(), "Transfer Funds")
    transfer_funds_page.add_value_to_amount_field("300")
    assert assert_is_true(transfer_funds_page.transfer_from_to(account_number_checking, account_number_savings), "Transfer Complete!")
    account_overview_page=transfer_funds_page.select_tab_in_side_panel("Accounts Overview")
    assert assert_is_true(account_overview_page.get_text_of_h1(), "Accounts Overview")
    time.sleep(1) # Used for demo purposes only
    assert account_overview_page.verify_amount_value_based_col_name(account_number_checking, "$700.00", "Balance")
    assert account_overview_page.verify_amount_value_based_col_name(account_number_checking, "$700.00",
                                                                    "Available Amount")

    assert account_overview_page.verify_amount_value_based_col_name(account_number_savings, "$300.00", "Balance")
    assert account_overview_page.verify_amount_value_based_col_name(account_number_savings, "$300.00", "Available Amount")
    assert assert_is_true(account_overview_page.get_total_amount(), "Total$1000.00")

    time.sleep(2) # Used for demo purposes only
