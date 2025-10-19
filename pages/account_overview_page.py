import time

from playwright.sync_api import Page, expect

from pages.main_page import MainPage
from utils.common_methods import get_text_of_element, element_loaded


class AccountOverviewPage(MainPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.h1_element = page.locator("#showOverview h1, #openAccountForm h1, #showForm h1")
        self.rows_of_accounts  = page.locator("//tbody//tr")
        self.account_numbers = page.locator("#accountTable tbody a") # returns 1 elem initially
        self.table_data = page.locator("//table[@id='accountTable']//tbody//tr//td")
        self.total_amount = page.locator("//table[@id='accountTable']//tbody//tr[contains(.,'Total')]")

    def get_text_of_h1(self):
        element_loaded(self.h1_element)
        return get_text_of_element(self.h1_element)

    def get_number_of_accounts(self):
        time.sleep(1)
        return self.rows_of_accounts.count()-1

    def get_account_numbers(self):
        return self.account_numbers.inner_text()

    def get_balance(self, account_number):
        balance =""
        for n in range(self.table_data.count()):
            if account_number == self.table_data.nth(n).text_content().strip():
                balance = self.table_data.nth(n + 1).text_content().strip()
                break
        return balance

    def get_available_amount(self, account_number):
        avail_amount = ""
        for n in range(self.table_data.count()):
            if account_number == self.table_data.nth(n).text_content().strip():
                avail_amount = self.table_data.nth(n + 2).text_content().strip()
                break
        return avail_amount

    def get_total_amount(self):
        raw_text = self.total_amount.text_content()
        cleaned_text = raw_text.replace("\xa0", "").strip()
        return cleaned_text

    def verify_amount_value_based_col_name(self, account_number: str, expected_amount: str, column_name: str) -> bool:

        actual_amount= ""
        if column_name == "Balance":
            actual_amount = self.get_balance(account_number)
        elif column_name == "Available Amount":
            actual_amount = self.get_available_amount(account_number)
        else:
            print(f"\n❌ Unsupported column name: '{column_name}'")
            return False

        if actual_amount == "":
            print(f"\n❌ Account {account_number} not found in the table <- {account_number} :EXP")
            return False
        if actual_amount != expected_amount:
            print(f"\n❌ Account {account_number} has unexpected amount in {column_name}: {actual_amount} <- {expected_amount} :EXP")
            return False
        print(f"✅ Account {account_number} → {column_name}: {actual_amount}")
        return True

    def parse_money(self,raw: str) -> float:
        """
        Converts a currency string like "$1,000.00" into a float: 1000.00
        """
        cleaned = raw.replace("$", "").replace(",", "").strip()
        return float(cleaned)


