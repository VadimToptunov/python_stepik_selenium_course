import time
from selenium import webdriver


def first_test(link, css1, css2, css3, css4, xpath):
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_tag_name(css1)
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_name(css2)
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_class_name(css3)
        input3.send_keys("Smolensk")
        input4 = browser.find_element_by_id(css4)
        input4.send_keys("Russia")
        button = browser.find_element_by_xpath(xpath)
        button.click()

    finally:
        time.sleep(30)
        browser.quit()


if __name__ == "__main__":
    link = "http://suninjuly.github.io/find_xpath_form"
    css1 = "input"
    css2 = "last_name"
    css3 = "city"
    css4 = "country"
    xpath = "//*[text() = 'Submit']"
    first_test(link, css1, css2, css3, css4, xpath)
