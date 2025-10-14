import allure
import pytest

from pages.authentication_page import AuthenticationPage


@allure.epic("UI")
@allure.feature("Authentication page")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
class TestAuthenticationPage:
    @allure.title("Authentication")
    def test_authentication(self, authentication_page: AuthenticationPage):
        authentication_page.click_display_image_button()
        authentication_page.open_image_page()
        authentication_page.authenticated_image_is_displayed()
        image_attribute = str(
            authentication_page.find_authenticated_image().get_attribute("src")
        )
        assert authentication_page.CREDENTIALS in image_attribute, (
            f"Incorrect image: {image_attribute}"
        )
