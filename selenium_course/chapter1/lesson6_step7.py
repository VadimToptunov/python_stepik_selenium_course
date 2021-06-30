import random
from selenium import webdriver
import string
import time


def find_elements(value):
    link = "http://suninjuly.github.io/huge_form.html"
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        elements = browser.find_elements_by_css_selector(value)
        for element in elements:
            answer = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(6))
            element.send_keys(answer)

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

    finally:
        time.sleep(30)
        browser.quit()
        

if __name__ == "__main__":
    value = "[type='text']"
    find_elements(value)