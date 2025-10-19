import time

from playwright.sync_api import Page

from pages.main_page import MainPage
from utils.common_methods import element_loaded, get_text_of_element, select_dropdown_option


class OpenNewAccountPage(MainPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.h1_element = page.locator("#showOverview h1, #openAccountForm h1, #showForm h1")
        self.account_type_select = page.locator("//p//b[text()='What type of Account would you like to open?']//../following-sibling::select[@id='type']")
        self.open_new_acc_btn = page.locator("//div//input[@type='button']")
        self.open_new_account_result_mes = page.locator("#openAccountResult h1")
        self.account_num_open_new_acc_result = page.locator("#openAccountResult a")

    def get_text_of_h1(self):
        element_loaded(self.h1_element)
        return get_text_of_element(self.h1_element)

    def select_account_type(self, typeName):
        select_dropdown_option(self.account_type_select, typeName, "text")

    def get_selected_option(self):
        return self.account_type_select.locator("option:checked").text_content()

    def click_open_new_acc_btn(self):
        time.sleep(2)
        self.open_new_acc_btn.click()
        element_loaded(self.open_new_account_result_mes)
        return self.open_new_account_result_mes.text_content()

    def get_new_account_number_from_result(self):
        element_loaded(self.account_num_open_new_acc_result)
        return self.account_num_open_new_acc_result.text_content()









