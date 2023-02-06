import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def math_data():
    return math.log(int(time.time()))
    

link = "https://stepik.org/lesson/236895/step/1"
links_task = ['https://stepik.org/lesson/236895/step/1',
              'https://stepik.org/lesson/236896/step/1', 
              'https://stepik.org/lesson/236897/step/1',
              'https://stepik.org/lesson/236898/step/1',
              'https://stepik.org/lesson/236899/step/1',
              'https://stepik.org/lesson/236903/step/1',
              'https://stepik.org/lesson/236904/step/1',
              'https://stepik.org/lesson/236905/step/1',
              ]




@pytest.mark.parametrize('step_links', links_task)
def test_login_stepik(browser, step_links):
    browser.implicitly_wait(5)
    browser.get(link)
    button_navbar_login = browser.find_element(By.CSS_SELECTOR, ".navbar__auth_login")
    button_navbar_login.click()
    email = browser.find_element(By.ID, "id_login_email")
    email.send_keys("ewokoman@yandex.ru")
    password = browser.find_element(By.ID, "id_login_password")
    password.send_keys("Vkontakte12")
    
    button_login = browser.find_element(By.CSS_SELECTOR, ".sign-form__btn.button_with-loader")
    button_login.click()
    time.sleep(3)
    browser.get(step_links)
    time.sleep(3)
    reply = browser.find_element(By.CSS_SELECTOR, ".string-quiz__textarea")
    reply.send_keys(str(math_data()))
    time.sleep(3)
    send_reply_btn = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
    )
    send_reply_btn.click()
    time.sleep(3)
    correct_text = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
    correct_text_text = correct_text.text
    time.sleep(3)


    print('\n'+'-'*10)
    print('\n'+ correct_text_text)
    print('\n'+'-'*10)

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Correct!" == correct_text_text, \
        f"expected Correct!, got {correct_text_text}"  

    # 'smart-hints__hint'
    # 'Correct!'
    
    time.sleep(10)