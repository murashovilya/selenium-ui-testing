import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10, poll_frequency=1)
        self.action = ActionChains(driver)
        self.URL = ""

    def open_page(self) -> None:
        with allure.step(f"Open page {self.URL}"):
            self.driver.get(self.URL)

    def page_is_opened(self) -> None:
        self.wait.until(EC.url_to_be(self.URL))

    def refresh_page(self) -> None:
        self.driver.refresh()

    def get_page_title(self) -> str:
        return self.driver.title

    def get_page_url(self) -> str:
        return self.driver.current_url

    def get_all_windows(self) -> list:
        return self.driver.window_handles

    def switch_to_window(self, window: str) -> None:
        self.driver.switch_to.window(window)

    def get_cookie(self, name: str) -> dict | None:
        return self.driver.get_cookie(name)

    def add_cookie(self, cookie: dict) -> None:
        self.driver.add_cookie(cookie)

    def delete_cookie(self, name: str) -> None:
        self.driver.delete_cookie(name)

    def scroll_to_bottom(self) -> None:
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def page_is_scrollable(self) -> bool:
        return self.driver.execute_script(
            "return document.body.scrollHeight > window.innerHeight;"
        )

    def remove_focus(self) -> None:
        self.driver.execute_script("document.activeElement.blur();")

    def element_is_focused(self, locator: tuple) -> bool:
        return self.driver.execute_script(
            "return document.activeElement === arguments[0];",
            self.find_element(locator),
        )

    def find_element(self, locator: tuple) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator: tuple) -> list[WebElement]:
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def element_is_displayed(self, locator: tuple) -> None:
        assert self.find_element(locator).is_displayed(), (
            f"Element {locator} is not displayed",
        )

    def fill_field(self, locator: tuple, data: str) -> None:
        self.wait.until(EC.element_to_be_clickable(locator)).send_keys(data)

    def clear_field(self, locator: tuple) -> None:
        self.wait.until(EC.element_to_be_clickable(locator)).clear()

    def click(self, locator: tuple) -> None:
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def get_alert(self) -> Alert:
        return self.wait.until(EC.alert_is_present())

    @allure.step("Enter text {text} in alert")
    def enter_text_in_alert(self, text: str) -> None:
        alert = self.get_alert()
        alert.send_keys(text)
        alert.accept()

    def select(self, locator: tuple) -> Select:
        return Select(self.wait.until(EC.element_to_be_clickable(locator)))
