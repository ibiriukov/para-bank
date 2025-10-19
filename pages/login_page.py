import time

from config import CONFIG
from pages.account_overview_page import AccountOverviewPage


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = 'input[name="username"]'
        self.password_input = 'input[name="password"]'
        self.login_button = 'input[type="submit"]'


    def login(self, username, password):
        self.page.goto(CONFIG["base_url"])
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)
        return AccountOverviewPage(self.page)

