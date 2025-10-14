import allure
import pytest

from pages.frames_and_windows_page import FramesAndWindowsPage


@allure.epic("UI")
@allure.feature("Frames and windows page")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
class TestFramesAndWindowsPage:
    @allure.title("Open new browser tab")
    def test_open_new_browser_tab(self, frames_and_windows_page: FramesAndWindowsPage):
        frames_and_windows_page.switch_to_frame()
        for _ in range(2):
            windows = frames_and_windows_page.get_all_windows()
            frames_and_windows_page.click_new_browser_tab_link()
            windows_after_click = frames_and_windows_page.get_all_windows()
            assert len(windows_after_click) == len(windows) + 1, (
                "New browser tab is not opened"
            )
            frames_and_windows_page.switch_to_window(windows_after_click[-1])
            frames_and_windows_page.new_browser_tab_link_is_displayed()
