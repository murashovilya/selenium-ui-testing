import allure
import pytest
from faker import Faker

from pages.alert_page import AlertPage


@allure.epic("UI")
@allure.feature("Alert page")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
class TestAlertPage:
    @allure.title("Enter text in alert")
    def test_enter_text_in_alert(self, alert_page: AlertPage):
        alert_page.click_input_alert_button()
        alert_page.switch_to_input_alert_iframe()
        alert_page.click_display_alert_button()
        alert_page.enter_text_in_alert(text := Faker().name())
        alert_text = alert_page.find_alert_text().text
        assert alert_text == f"Hello {text}! How are you today?", (
            f"Incorrect alert text: {alert_text}"
        )
