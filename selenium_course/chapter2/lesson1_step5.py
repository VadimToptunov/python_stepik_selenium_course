import math
from selenium import webdriver
import time


def robot_test(link):
	try:
		browser = webdriver.Chrome()
		browser.get(link)

		x_value = browser.find_element_by_id("input_value").text

		answer = calc(x_value)

		answer_field = browser.find_element_by_id("answer")
		answer_field.send_keys(str(answer))

		checkbox = browser.find_element_by_id("robotCheckbox")
		checkbox.click()

		robots_rule_radio = browser.find_element_by_id("robotsRule")
		robots_rule_radio.click()

		submit_button = browser.find_element_by_css_selector(".btn.btn-default")
		submit_button.click()
		time.sleep(30)
	finally:
		browser.quit()


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


if __name__ == "__main__":
	link = "http://suninjuly.github.io/math.html"
	robot_test(link)
