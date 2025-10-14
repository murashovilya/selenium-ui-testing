import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class AuthenticationPage(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.URL = "https://www.httpwatch.com/httpgallery/authentication/#showExample10"
        self.USERNAME = "httpwatch"
        self.PASSWORD = "httpwatch"
        self.CREDENTIALS = f"{self.USERNAME}:{self.PASSWORD}"
        self.DISPLAY_IMAGE_BUTTON = (By.ID, "displayImage")
        self.IMAGE_URL = f"https://{self.CREDENTIALS}@www.httpwatch.com/httpgallery/authentication/authenticatedimage/default.aspx"  # noqa
        self.AUTHENTICATED_IMAGE = (By.TAG_NAME, "img")

    @allure.step("Click Display Image Button")
    def click_display_image_button(self) -> None:
        self.click(self.DISPLAY_IMAGE_BUTTON)

    @allure.step("Open Image Page")
    def open_image_page(self) -> None:
        self.driver.get(self.IMAGE_URL)

    def find_authenticated_image(self) -> WebElement:
        return self.find_element(self.AUTHENTICATED_IMAGE)

    def authenticated_image_is_displayed(self) -> None:
        self.element_is_displayed(self.AUTHENTICATED_IMAGE)
