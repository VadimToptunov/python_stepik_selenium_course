from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


def new_robot_test(link):
	try:
		browser = webdriver.Chrome()
		browser.get(link)

		num1 = int(browser.find_element_by_id("num1").text)
		num2 = int(browser.find_element_by_id("num2").text)
		sum_value = num1 + num2

		dropdown = browser.find_element_by_id("dropdown")
		select = Select(dropdown)
		select.select_by_visible_text(str(sum_value))

		button = browser.find_element_by_css_selector(".btn.btn-default")
		button.click()

		time.sleep(30)
	finally:
		browser.quit()


if __name__ == "__main__":
	link = "http://suninjuly.github.io/selects1.html"
	new_robot_test(link)
	link2 = "http://suninjuly.github.io/selects2.html"
	new_robot_test(link2)




# select = Select(browser.find_element_by_tag_name("select"))