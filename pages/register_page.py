import os
import time

from playwright.sync_api import Page, Locator

from config import CONFIG
from pages.account_overview_page import AccountOverviewPage
from utils.common_methods import element_loaded


class RegisterPage:
    def __init__(self, page: Page):
        self.page = page
        self.customer_fName: Locator = self.page.locator("//input[@id='customer.firstName']")
        self.customer_lName = "//input[@id='customer.lastName']"
        self.customer_street = "//input[@id='customer.address.street']"
        self.customer_city = "//input[@id='customer.address.city']"
        self.customer_state = "//input[@id='customer.address.state']"
        self.customer_zip = "//input[@id='customer.address.zipCode']"
        self.customer_phone = "//input[@id='customer.phoneNumber']"
        self.customer_ssn = "//input[@id='customer.ssn']"
        self.customer_uName = "//input[@id='customer.username']"
        self.customer_psw = "//input[@id='customer.password']"
        self.customer_repeatedPsw = "//input[@id='repeatedPassword']"
        self.registerBtn = "//input[@value='Register']"

        self.welcome_message= page.locator("#rightPanel h1")


    def register(self, user_name):
        self.page.goto(CONFIG["base_url"])
        assert element_loaded(self.customer_fName)
        self.customer_fName.fill("fName")
        self.page.fill(self.customer_lName, "lName")
        self.page.fill(self.customer_street, "Address")
        self.page.fill(self.customer_city, "City")
        self.page.fill(self.customer_state, "State")
        self.page.fill(self.customer_zip, "12345")
        self.page.fill(self.customer_phone, "11133344455")
        self.page.fill(self.customer_ssn, CONFIG["ssi"])
        self.page.fill(self.customer_uName, user_name)
        self.page.fill(self.customer_psw, CONFIG["password"])

        self.page.fill(self.customer_repeatedPsw, CONFIG["password"])
        self.page.click(self.registerBtn)
        assert element_loaded(self.welcome_message)

        return self.welcome_message.text_content()