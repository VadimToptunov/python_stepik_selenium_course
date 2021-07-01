import math
from selenium import webdriver
import time

def alert_handling_test(link):
	try:
		browser = webdriver.Chrome()
		browser.get(link)

		click_submit_button(browser)

		time.sleep(5)

		alert = browser.switch_to.alert
		alert.accept()

		# time.sleep(5)

		x_value = browser.find_element_by_id("input_value").text

		answer = calc(x_value)

		input_field = browser.find_element_by_id("answer")
		input_field.send_keys(answer)

		click_submit_button(browser)

		time.sleep(30)
	finally:
		browser.quit()


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


def click_submit_button(browser):
	button = browser.find_element_by_css_selector(".btn.btn-primary")
	button.click()


if __name__ == "__main__":
	link = "http://suninjuly.github.io/alert_accept.html"
	alert_handling_test(link)
