from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://openweathermap.org/'
load_div = (By.CSS_SELECTOR, 'div.owm-loader-container > div')
marketplace_link = (By.CSS_SELECTOR, '#desktop-menu ul li:nth-child(4) a')
marketplace = 'https://home.openweathermap.org/marketplace'


@pytest.fixture()
def wait(driver):
    wait = WebDriverWait(driver, 25)
    yield wait


@pytest.fixture()
def open_and_load_page(driver, wait):
    driver.get(URL)
    wait.until_not(EC.presence_of_element_located(load_div))


def test_TC_002_03_07_verify_marketplace_link_redirects_to_valid_page(driver, open_and_load_main_page, wait):
    driver.set_window_size(1200, 800)
    driver.find_element(*marketplace_link).click()
    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    assert driver.current_url == marketplace