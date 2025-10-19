from playwright.sync_api import Page

from pages.main_page import MainPage
from utils.common_methods import element_loaded, get_text_of_element


class TransferFundsPage(MainPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.h1_element = page.locator("#showOverview h1, #openAccountForm h1, #showForm h1")
        self.amount_input_field = page.locator("#transferForm #amount")
        self.account_select_from = page.locator("#transferForm #fromAccountId")
        self.account_select_to = page.locator("#transferForm #toAccountId")
        self.submit_btn = page.locator("//input[@type='submit']")
        self.open_new_account_result_mes = page.locator("#showResult h1")


    def get_text_of_h1(self):
        element_loaded(self.h1_element)
        return get_text_of_element(self.h1_element)

    def add_value_to_amount_field(self, amount):

        self.amount_input_field.fill(amount)

    def transfer_from_to(self, acc_from, acc_to):
        self.account_select_from.select_option(acc_from)
        self.account_select_to.select_option(acc_to)
        self.submit_btn.click()
        element_loaded(self.open_new_account_result_mes)
        return self.open_new_account_result_mes.text_content()


