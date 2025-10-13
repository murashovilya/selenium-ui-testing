import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.bank_manager_login_page import BankManagerLoginPage


class AddCustomerPage(BankManagerLoginPage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.URL = "https://www.way2automation.com/angularjs-protractor/banking/#/manager/addCust"
        self.FIRST_NAME_FIELD = (By.XPATH, "//input[@ng-model='fName']")
        self.LAST_NAME_FIELD = (By.XPATH, "//input[@ng-model='lName']")
        self.POST_CODE_FIELD = (By.XPATH, "//input[@ng-model='postCd']")
        self.ADD_CUSTOMER_BUTTON_2 = (By.XPATH, "//button[@type='submit']")

    @allure.step("Enter {first_name} in First Name field")
    def enter_first_name(self, first_name: str) -> None:
        self.fill_field(self.FIRST_NAME_FIELD, first_name)

    @allure.step("Enter {last_name} in Last Name field")
    def enter_last_name(self, last_name: str) -> None:
        self.fill_field(self.LAST_NAME_FIELD, last_name)

    @allure.step("Enter {post_code} in Post Code field")
    def enter_post_code(self, post_code: str) -> None:
        self.fill_field(self.POST_CODE_FIELD, post_code)

    @allure.step("Click Add Customer button under Post Code field")
    def click_add_customer_button_2(self) -> None:
        self.click(self.ADD_CUSTOMER_BUTTON_2)
