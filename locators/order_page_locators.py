

from selenium.webdriver.common.by import By


class OrderLocators:
    #Локаторы для формы "для кого самокат"

    LABEL_WHO_IS_THE_SCOOTER_FOR = [By.CLASS_NAME, "Order_Header__BZXOb"]
    ORDER_NAME = [By.XPATH, ".//input[@placeholder='* Имя']"]
    ORDER_SURNAME = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
    ORDER_ADDRESS = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]
    ORDER_METRO = [By.CLASS_NAME, "select-search__input"]
    ORDER_PHONE = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]
    BUTTON_FURTHER = [By.XPATH, "//*[@id='root']/div/div[2]/div[3]/button"]
    METRO_LIST = [By.XPATH, ".//li[@class='select-search__row']"]

    #Локаторы для формы "Про аренду"
    ORDER_WHEN_TO_BRING_SCOOTER = [By.CLASS_NAME, "react-datepicker__input-container"]
    ORDER_RENTAL_PERIOD = [By.CLASS_NAME, "Dropdown-control"]
    ORDER_RENTAL_PERIOD_MENU = [By.CLASS_NAME, "Dropdown-option"]
    ORDER_COLOUR_BLACK = [By.XPATH, ".//label[@for='black']"]
    ORDER_COLOUR_GREY = [By.XPATH, ".//label[@for='grey']"]
    POPUP_PLACE_AN_ORDER = [By.CLASS_NAME, "Order_ModalHeader__3FDaJ"]
    POPUP_SUCCESSFULLY_ISSUED = [By.XPATH, ".//div[text()='Заказ оформлен']"]
    BUTTON_CHECK_STATUS = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Посмотреть статус']"]
    BUTTON_ORDER_YES = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']"]
    ORDER_COMMENT = [By.XPATH, ".//input[@placeholder='Комментарий для курьера']"]
    BUTTON_ORDER = [By.XPATH, "//*[@id='root']/div/div[2]/div[3]/button[2]"]
    LABEL_ABOUT_RENT = [By.CLASS_NAME, "Order_Header__BZXOb"]


    @staticmethod
    def date_datapiker(number_date):
        return By.XPATH, f"//div[contains(@class, 'react-datepicker__day') and text() = '{number_date}']"

    @staticmethod
    def rental_period(period):
        list_period = ["сутки", "двое суток", "трое суток", "четверо суток", "пятеро суток", "шестеро суток","семеро суток"]
        return By.XPATH, f"//div[@class='Dropdown-option' and text()='{period}']"

    @staticmethod
    def colour_scooter(color):
        return By.XPATH, f".//label[@for='{color}']"


