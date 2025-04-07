import allure
from locators.main_page_locators import MainLocators
from locators.order_page_locators import OrderLocators
from pages.base_page import BasePage



class OrderPage(BasePage):
    @allure.step("Кликнуть на кнопку заказа")
    def click_header_button(self):
        self.click_on_element(MainLocators.HEADER_BUTTON_ORDER)

    @allure.step("Кликнуть на кнопку принятия куки")
    def click_accept_cookie(self):
        self.click_on_element(MainLocators.COOKIE_ACCEPT)

    @allure.step("Клик на кнопку заказа")
    def click_button_order_middle(self):
        self.click_accept_cookie()
        self.scroll_to_element(MainLocators.BOTTOM_BUTTON_ORDER)
        self.click_on_element(MainLocators.BOTTOM_BUTTON_ORDER)

    @allure.step("Заполнить форму 'для кого самокат'")
    def fill_form_who_is_the_scooter_for(self, name, surname, address, metro, phone):
        self.send_keys_to_input(OrderLocators.ORDER_NAME, name)
        self.send_keys_to_input(OrderLocators.ORDER_SURNAME, surname)
        self.send_keys_to_input(OrderLocators.ORDER_ADDRESS, address)
        self.click_on_element(OrderLocators.ORDER_METRO)
        self.send_keys_to_input(OrderLocators.ORDER_METRO, metro)
        self.click_on_element(OrderLocators.METRO_LIST)
        self.send_keys_to_input(OrderLocators.ORDER_PHONE, phone)

    @allure.step("Клик на кнопку 'далее'")
    def click_button_further(self):
        self.click_on_element(OrderLocators.BUTTON_FURTHER)

    @allure.step("Заполнить поле 'дата'")
    def input_when_to_bring(self, date):
        self.click_on_element(OrderLocators.ORDER_WHEN_TO_BRING_SCOOTER)
        self.click_on_element(OrderLocators.date_datapiker(date))



    @allure.step("Выбор срока аренды")
    def choosing_the_rental_period(self, period):
        self.click_on_element(OrderLocators.ORDER_RENTAL_PERIOD)
        self.wait_for_element(OrderLocators.ORDER_RENTAL_PERIOD_MENU)
        self.click_on_element(OrderLocators.rental_period(period))

    @allure.step("Выбор цвета")
    def color_selection(self, color):
        self.click_on_element(OrderLocators.colour_scooter(color))

    @allure.step("Заполнить поле комментарий")
    def input_to_comment(self, text):
        self.send_keys_to_input(OrderLocators.ORDER_COMMENT, text)

    @allure.step("Кликнуть на кнопку 'Заказать'")
    def click_button_order(self):
        self.click_on_element(OrderLocators.BUTTON_ORDER)

    @allure.step("Ожидание попапа 'Оформить заказ?'")
    def wait_popup_place(self):
        self.wait_for_element(OrderLocators.POPUP_PLACE_AN_ORDER)

    @allure.step("Клик на кнопку соглашения")
    def click_yes_in_popup(self):
        self.click_on_element(OrderLocators.BUTTON_ORDER_YES)


    @allure.step("Ожидание попапа 'Заказ успешно оформлен'")
    def wait_popup_successfully_order(self):
        return self.wait_for_element(OrderLocators.POPUP_SUCCESSFULLY_ISSUED)

    @allure.step("Ожидание прогрузки 'про аренду'")
    def wait_label_about_rent(self):
        self.wait_for_element(OrderLocators.LABEL_ABOUT_RENT)

    @allure.step("Заполнить форму 'про аренду'")
    def fill_about_rent(self, date, period, color, text):
        self.input_when_to_bring(date)
        self.choosing_the_rental_period(period)
        self.color_selection(color)
        self.input_to_comment(text)






