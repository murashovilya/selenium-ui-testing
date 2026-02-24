import allure
import pytest

from pages.sql_page import SQLPage
from utils.cookies_manager import Cookies


@allure.epic("UI")
@allure.feature("Страница SQL")
@pytest.mark.smoke
class TestSQLPage:
    @allure.title("Авторизация")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("run", range(2))
    def test_login(self, run: int, sql_page: SQLPage):
        try:
            cookie = Cookies.get_cookie_from_file()
            sql_page.delete_cookie("PHPSESSID")
            sql_page.add_cookie(cookie)
            sql_page.refresh_page()
            Cookies.delete_cookie_file()
        except FileNotFoundError:
            sql_page.enter_login(sql_page.LOGIN)
            sql_page.enter_password(sql_page.PASSWORD)
            sql_page.click_enter_button()
            Cookies.save_cookie(sql_page.get_cookie("PHPSESSID"))  # type: ignore
        right_header_text = sql_page.find_right_header().text
        nickname_length = len(sql_page.NICKNAME)
        nickname = right_header_text[-nickname_length:]
        assert nickname == sql_page.NICKNAME, f"Некорректный никнейм: {nickname}"

    @allure.title("Удаление фокуса из поля Login и проверка наличия скролла")
    def test_remove_focus_from_login_field_and_check_scroll(self, sql_page: SQLPage):
        assert sql_page.element_is_focused(sql_page.LOGIN_FIELD), (
            "В поле Login отсутствует фокус"
        )
        sql_page.remove_focus()
        assert not sql_page.element_is_focused(sql_page.LOGIN_FIELD), (
            "В поле Login присутствует фокус"
        )
        assert sql_page.page_is_scrollable(), "На странице отсутствует скролл"
