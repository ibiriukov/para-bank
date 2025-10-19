from pages.main_page import MainPage
from utils.common_methods import element_loaded, get_text_of_element


class AdministrationPage(MainPage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.h1_element = page.locator("#rightPanel h1")
        self.ini_balance = page.locator("#initialBalance")
        self.min_balance = page.locator("#minimumBalance")
        self.submit_btn = page.locator("//input[@value='Submit']")
        self.success_mes = page.locator("#rightPanel p b")

    def get_text_of_h1(self):
        element_loaded(self.h1_element)
        return get_text_of_element(self.h1_element)

    def set_initial_balance(self, in_balance):
        self.ini_balance.fill(in_balance)

    def set_min_balance(self, min_balance):
        self.min_balance.fill(min_balance)

    def submit_button(self):
        self.submit_btn.click()
        element_loaded(self.success_mes)
        return self.success_mes.inner_text()

