from playwright.sync_api import Page


class MainPage:
    def __init__(self, page: Page):
        self.page = page
        self.accounts_overview_tab = page.locator("//li//a[text()='Accounts Overview']")
        self.side_panel_tabs = page.locator("#leftPanel li")
        self.side_header_panel_tabs = page.locator("#headerPanel .leftmenu li")

    def select_tab_in_side_panel(self, tabName):
        for i in range(self.side_panel_tabs.count()):
            tab = self.side_panel_tabs.nth(i)
            if tab.text_content().strip() == tabName:
                tab.click()
                if tabName == "Accounts Overview":
                    from pages.account_overview_page import AccountOverviewPage
                    return AccountOverviewPage(self.page)
                if tabName == "Open New Account":
                    from pages.open_new_account_page import OpenNewAccountPage
                    return OpenNewAccountPage(self.page)
                if tabName == "Transfer Funds":
                    from pages.transfer_funds_page import TransferFundsPage
                    return TransferFundsPage(self.page)

                # Add more tabs as needed
                return None
        raise ValueError(f"Tab {tabName} not found in side panel")

    def select_tab_in_side_header_panel(self, tabName):
        for i in range(self.side_header_panel_tabs.count()):
            tab = self.side_header_panel_tabs.nth(i)
            if tab.text_content().strip() == tabName:
                tab.click()
                if tabName == "Admin Page":
                    from pages.administration_page import AdministrationPage
                    return AdministrationPage(self.page)

                # Add more tabs as needed
                return None
        raise ValueError(f"Tab {tabName} not found in side panel")
