import time

import allure
import pytest

import data
from pages.base_page import BasePage
from pages.order_page import OrderPage


class TestOrderScooterThroughHeaderButton:
    @allure.title("Тест появления всплывающего окна с сообщением об успешном создании заказа. Через верхнею кнопку входа в сценарий")
    @pytest.mark.parametrize('name, surname, address, metro, phone, date, period, color, text', data.Data.data_who_is_scooter_for)
    def test_order_scooter_through_header_button(self, driver, name, surname, address, metro, phone, date, period, color, text):
        # Arrange
        order_page = OrderPage(driver)
        # Act
        order_page.click_header_button()
        order_page.fill_form_who_is_the_scooter_for(name, surname, address, metro, phone)
        order_page.click_button_further()
        order_page.wait_label_about_rent()
        order_page.fill_about_rent(date, period, color, text)
        order_page.click_button_order()
        order_page.wait_popup_place()
        order_page.click_yes_in_popup()
        # Assert
        assert OrderPage.wait_popup_successfully_order

class TestOrderScooterThroughMiddleButton:
    @allure.title("Тест появления всплывающего окна с сообщением об успешном создании заказа. Через нижнею кнопку входа в сценарий")
    @pytest.mark.parametrize('name, surname, address, metro, phone, date, period, color, text',
                             data.Data.data_who_is_scooter_for)
    def test_order_scooter_through_middle_button(self, driver, name, surname, address, metro, phone, date, period, color, text):
        # Arrange
        order_page = OrderPage(driver)
        # Act
        order_page.click_button_order_middle()
        order_page.fill_form_who_is_the_scooter_for(name, surname, address, metro, phone)
        order_page.click_button_further()
        order_page.wait_label_about_rent()
        order_page.fill_about_rent(date, period, color, text)
        order_page.click_button_order()
        order_page.wait_popup_place()
        order_page.click_yes_in_popup()
        # Assert
        assert OrderPage.wait_popup_successfully_order