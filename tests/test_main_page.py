

import allure
import pytest

import data
from curl import dzen, main_site
from pages.main_page import MainPageScooter


class TestClickLogoYandexGoingToDzen:
    @allure.title("Тест перехода на дзен при клике на логотип яндекса")
    def test_going_to_dzen_when_click_logo(self, driver):
        # Arrange
        main_page = MainPageScooter(driver)
        # Act
        main_page.click_logo_yandex()
        #Assert
        assert driver.current_url == dzen

class TestClickLogoScooterGoingMainPage:
    @allure.title("Тест перехода на главную страницу при клике на логотип самоката")
    def test_going_to_main_page_when_click_logo_scooter(self, driver):
        #Arrange
        main_page = MainPageScooter(driver)
        #Act
        main_page.click_down_button_order()
        main_page.click_logo_scooter()
        #Assert
        assert driver.current_url == main_site

class TestQuestionAnswer:
    @allure.title("Тест ответов важных вопросов")
    @pytest.mark.parametrize('question_number, expected_text', data.Data.question_answer)
    def test_answer_question(self, driver, question_number, expected_text):
        # Arrange
        main_page = MainPageScooter(driver)
        # Act
        main_page.click_accept_cookie()
        main_page.click_on_question(question_number)
        #Assert
        assert main_page.check_question_answer(expected_text)


