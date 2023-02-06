import time
from selenium.webdriver.common.by import By



link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"



def test_find_button_buy(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    time.sleep(10)
    button_buy = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")

    assert None != button_buy, \
        f"Button buy not found"  

    time.sleep(10)
