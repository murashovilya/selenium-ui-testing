import allure
import pytest

from pages.droppable_page import DroppablePage


@allure.epic("UI")
@allure.feature("Drag and drop page")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
class TestDroppablePage:
    @allure.title("Drag and drop element")
    def test_drag_and_drop_element(self, droppable_page: DroppablePage):
        droppable_page.switch_to_frame()
        droppable_page.drag_and_drop_element()
        droppable_element_text = droppable_page.find_droppable_element().text
        assert droppable_element_text == "Dropped!", (
            f"Incorrect text in the droppable element: \
                {droppable_element_text}"
        )
