from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    time.sleep(30)
    message1 = browser.find_element(By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")

    assert message1.text != ""
    print("Нашли кнопку: " + message1.text)