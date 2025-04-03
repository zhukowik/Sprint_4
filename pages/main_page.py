import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainLocators

class MainPageScooter(BasePage):
    @allure.step("Кликнуть на вопрос")
    def click_on_question(self, number_question):
        question_locator = MainLocators.number_question(number_question)
        self.scroll_to_element(question_locator)
        self.click_on_element(question_locator)

    @allure.step("Сравни ответ на вопрос")
    def check_question_answer(self, expected_text):
        actual_text = self.get_text_on_element(MainLocators.QUESTION_ANSWER)
        return actual_text == expected_text

    @allure.step("Кликнуть на логотип яндекса")
    def click_logo_yandex(self):
        self.click_on_element(MainLocators.HEADER_LOGO_YANDEX)

    @allure.step("Кликнуть на логотип самоката")
    def click_logo_scooter(self):
        self.click_on_element(MainLocators.HEADER_LOGO_SCOOTER)

    @allure.step("Кликнуть на кнопку принятия куки")
    def click_accept_cookie(self):
        self.click_on_element(MainLocators.COOKIE_ACCEPT)

    @allure.step("Клик по нижней кнопки заказать")
    def click_down_button_order(self):
        self.click_accept_cookie()
        self.scroll_to_element(MainLocators.BOTTOM_BUTTON_ORDER)
        self.click_on_element(MainLocators.BOTTOM_BUTTON_ORDER)
