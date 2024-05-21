from time import sleep

from pages.base import BasePage
from selenium.webdriver.common.by import By


pluss_ing = (By.XPATH, "//input[@placeholder='+ Ингредиент']")
unpluss_ing = (By.XPATH, "//input[@placeholder='- Ингредиент']")


class FiltersPage2(BasePage, ):
    def __init__(self, browser):
        super().__init__(browser)



    def open(self):
        return self.browser.get('http://eda.ru')


    def pluss(self):
        self.find(pluss_ing).click()
        return self.find(pluss_ing).send_keys('куринное филе, помидоры, сыр')
        sleep(5)

    def unpluss(self):
        self.find(unpluss_ing).click()
        return self.find(unpluss_ing).send_keys('огурцы, лимон')
        sleep(5)

    def open_filter_2(self):
        return self.browser.get('http://eda.ru')
        implicitly_wait(20)

    def open_filters_2(self):
        self.find((By.XPATH, "//button[@class='emotion-13uukrm']")).click()

    def pluss(self):
        self.find(pluss_ing).click()
        return self.find(pluss_ing).send_keys('куринное филе, помидоры, сыр')
        sleep(5)

    def unpluss(self):
        self.find(unpluss_ing).click()
        return self.find(unpluss_ing).send_keys('огурцы, лимон')
        sleep(5)
