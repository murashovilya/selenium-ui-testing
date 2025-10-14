import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class DroppablePage(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.URL = "https://way2automation.com/way2auto_jquery/droppable.php"
        self.IFRAME = (By.XPATH, "//iframe[@class='demo-frame']")
        self.DRAGGABLE_ELEMENT = (By.ID, "draggable")
        self.DROPPABLE_ELEMENT = (By.ID, "droppable")

    def switch_to_frame(self) -> None:
        self.driver.switch_to.frame(self.find_element(self.IFRAME))

    def find_draggable_element(self) -> WebElement:
        return self.find_element(self.DRAGGABLE_ELEMENT)

    def find_droppable_element(self) -> WebElement:
        return self.find_element(self.DROPPABLE_ELEMENT)

    @allure.step("Drag and drop element")
    def drag_and_drop_element(self) -> None:
        self.action.drag_and_drop(
            self.find_draggable_element(), self.find_droppable_element()
        ).perform()
