from time import sleep
from pages.filter_2 import FiltersPage2
import allure


def test_filter_2(authorized_browser):
    with allure.step('Test filter_2'):
        filters_page_2 = FiltersPage2(authorized_browser)

    with allure.step("open_filters_2"):
        filters_page_2.open()

    with allure.step("pluss"):
        filters_page_2.pluss()

    with allure.step("unpluss"):
        filters_page_2.unpluss()
