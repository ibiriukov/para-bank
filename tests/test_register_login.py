import time


def test_register_login(page, account_overview_page):
    assert account_overview_page.get_text_of_h1() == "Accounts Overview"
    time.sleep(1)  # Used for demo purposes only

