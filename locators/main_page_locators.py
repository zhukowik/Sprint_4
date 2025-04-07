from selenium.webdriver.common.by import By



class MainLocators:

    @staticmethod
    def number_question(number):
        return By.XPATH, f'.//*[@id="accordion__heading-{number}"]'


    HEADER_BUTTON_ORDER = [By.CLASS_NAME, "Button_Button__ra12g"]
    BOTTOM_BUTTON_ORDER = [By.XPATH, "//*[@id='root']/div/div/div[4]/div[2]/div[5]/button"]

    HEADER_LOGO_SCOOTER = [By.CLASS_NAME, "Header_LogoScooter__3lsAR"]
    HEADER_LOGO_YANDEX = [By.CLASS_NAME, "Header_LogoYandex__3TSOI"]
    QUESTION_ANSWER = [By.XPATH, "//div[@data-accordion-component='AccordionItemPanel' and not(@hidden)]"]
    COOKIE_ACCEPT = [By.ID, "rcc-confirm-button"]
