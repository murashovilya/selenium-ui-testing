import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.URL = "https://www.way2automation.com/"
        self.HEADER = (By.XPATH, "//div[@class='ast-above-header-wrap  ']")
        self.HEADER_CONTACTS = [
            "+919711-111-558",
            "+919711-191-558",
            "+1 646-480-0603",
            "seleniumcoaching",
            "trainer@way2automation.com",
        ]
        self.MENU = (By.XPATH, "//ul[@id='ast-hf-menu-1']")
        self.ALL_COURSES_BUTTON = (By.XPATH, "(//ul[@id='ast-hf-menu-1']/li)[2]")
        self.LIFETIME_MEMBERSHIP_BUTTON = (
            By.XPATH,
            "(//span[text()='Lifetime Membership'])[1]",
        )
        self.LIFETIME_MEMBERSHIP_BLOCK = (
            By.XPATH,
            "(//div[@class='elementor-slide-description'])[1]",
        )
        self.LIFETIME_MEMBERSHIP_BLOCK_DESCRIPTION = """
        LIFETIME MEMBERSHIP FOR LIVE TRAININGS IN JUST 7000 RS / 99 USD
        1. Selenium with Core Java - starts 03rd May 2025 (Duration 3.5 Months)
        2. API Automation Rest Assured - starts 10th May 2025 \
            (Duration 2 Months)
        """
        self.REG_BUTTON = (By.XPATH, "//div[@class='swiper-slide-contents']/a")
        self.SELENIUM_COURSE_BLOCK = (By.XPATH, "//div[@data-id='259f3103']/div")
        self.MOST_POPULAR_COURSES_BLOCK = (By.XPATH, "//div[@data-id='50827c4']")
        self.ACTIVE_COURSE_IN_MOST_POPULAR_COURSES_BLOCK = (
            By.XPATH,
            "//div[@class='swiper-slide swiper-slide-active']",
        )
        self.PREVIOUS_COURSE_IN_MOST_POPULAR_COURSES_BLOCK = (
            By.XPATH,
            "//div[@class='swiper-slide swiper-slide-prev']",
        )
        self.NEXT_COURSE_IN_MOST_POPULAR_COURSES_BLOCK = (
            By.XPATH,
            "//div[@class='swiper-slide swiper-slide-next']",
        )
        self.PREVIOUS_MOST_POPULAR_COURSE_BUTTON = (
            By.XPATH,
            "(//div[@aria-label='Previous slide'])[2]",
        )
        self.NEXT_MOST_POPULAR_COURSE_BUTTON = (
            By.XPATH,
            "(//div[@aria-label='Next slide'])[2]",
        )
        self.FOOTER = (By.XPATH, "//div[@data-elementor-type='footer']")
        self.FOOTER_CONTACTS = [
            "CDR Complex, 3rd Floor, Naya Bans Market, Sector 15, Noida, Near sec-16 Metro Station",  # noqa
            "+91 97111-11-558",
            "+91 97111-91-558",
            "trainer@way2automation.com",
            "seleniumcoaching@gmail.com",
        ]

    def find_header(self) -> WebElement:
        return self.find_element(self.HEADER)

    def header_is_displayed(self) -> None:
        self.element_is_displayed(self.HEADER)

    def find_menu(self) -> WebElement:
        return self.find_element(self.MENU)

    def menu_is_displayed(self) -> None:
        self.element_is_displayed(self.MENU)

    def find_lifetime_membership_block(self) -> WebElement:
        return self.find_element(self.LIFETIME_MEMBERSHIP_BLOCK)

    def reg_button_is_displayed(self) -> None:
        self.element_is_displayed(self.REG_BUTTON)

    def selenium_course_block_is_displayed(self) -> None:
        self.element_is_displayed(self.SELENIUM_COURSE_BLOCK)

    def find_most_popular_courses_block(self) -> list[WebElement]:
        return self.find_elements(self.MOST_POPULAR_COURSES_BLOCK)

    def find_active_course_in_most_popular_courses_block(self) -> WebElement:
        return self.find_element(self.ACTIVE_COURSE_IN_MOST_POPULAR_COURSES_BLOCK)

    def find_previous_course_in_most_popular_courses_block(self) -> WebElement:
        return self.find_element(self.PREVIOUS_COURSE_IN_MOST_POPULAR_COURSES_BLOCK)

    def find_next_course_in_most_popular_courses_block(self) -> WebElement:
        return self.find_element(self.NEXT_COURSE_IN_MOST_POPULAR_COURSES_BLOCK)

    def move_to_most_popular_courses_block(self) -> None:
        self.action.move_to_element(
            self.find_element(self.MOST_POPULAR_COURSES_BLOCK)
        ).perform()

    @allure.step("Нажать на кнопку Назад в блоке Most Popular Courses")
    def click_previous_most_popular_course_button(self) -> None:
        self.click(self.PREVIOUS_MOST_POPULAR_COURSE_BUTTON)

    @allure.step("Нажать на кнопку Вперед в блоке Most Popular Courses")
    def click_next_most_popular_course_button(self) -> None:
        self.click(self.NEXT_MOST_POPULAR_COURSE_BUTTON)

    @allure.step("Нажать на кнопку Lifetime Membership в меню All Courses")
    def click_lifetime_membership_button(self) -> None:
        self.action.move_to_element(self.find_element(self.ALL_COURSES_BUTTON)).pause(
            1
        ).move_to_element(self.find_element(self.LIFETIME_MEMBERSHIP_BUTTON)).pause(
            1
        ).click().perform()

    def find_footer(self) -> WebElement:
        return self.find_element(self.FOOTER)

    def footer_is_displayed(self) -> None:
        self.element_is_displayed(self.FOOTER)
