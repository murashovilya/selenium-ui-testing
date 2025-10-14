import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class BankManagerLoginPage(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.URL = (
            "https://www.way2automation.com/angularjs-protractor/banking/#/manager"
        )
        self.ADD_CUSTOMER_BUTTON = (By.XPATH, "//button[@ng-click='addCust()']")
        self.OPEN_ACCOUNT_BUTTON = (By.XPATH, "//button[@ng-click='openAccount()']")
        self.CUSTOMERS_BUTTON = (By.XPATH, "//button[@ng-click='showCust()']")

    @allure.step("Click Add Customer button")
    def click_add_customer_button(self) -> None:
        self.click(self.ADD_CUSTOMER_BUTTON)

    @allure.step("Click Open Account button")
    def click_open_account_button(self) -> None:
        self.click(self.OPEN_ACCOUNT_BUTTON)

    @allure.step("Click Customers button")
    def click_customers_button(self) -> None:
        self.click(self.CUSTOMERS_BUTTON)
