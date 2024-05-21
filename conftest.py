from time import sleep

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from pages.autorization import AutorizationPage


@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    chrome_browser.maximize_window()
    return chrome_browser

@pytest.fixture()
def authorized_browser(browser):
    autorization_page = AutorizationPage(browser)
    autorization_page.open()
    sleep(1)
    autorization_page.sing_in()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    autorization_page.post
    autorization_page.pas()
    autorization_page.log()
    original_window = browser.window_handles[0]
    browser.switch_to.window(original_window)
    return browser