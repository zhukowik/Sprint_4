import pytest
from selenium import webdriver
import sys

sys.path.append('C:/Users/zewer/PycharmProjects/Sprint_4')
from curl import *


@pytest.fixture(scope='function')
def driver():
    browser = webdriver.Firefox()
    browser.get(main_site)
    yield browser
    browser.quit()