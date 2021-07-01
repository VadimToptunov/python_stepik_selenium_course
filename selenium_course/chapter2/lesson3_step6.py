import math
from selenium import webdriver
import time


def handling_different_windows_test(link):
	try:
		browser = webdriver.Chrome()
		browser.get(link)
		
		time.sleep(5)
		click_submit_button(browser, ".trollface.btn.btn-primary")

		new_window = browser.window_handles[1]
		browser.switch_to.window(new_window)

		x_value = browser.find_element_by_id("input_value").text

		answer = calc(x_value)

		input_field = browser.find_element_by_id("answer")
		input_field.send_keys(answer)

		click_submit_button(browser, ".btn.btn-primary")

		time.sleep(30)
	finally:
		browser.quit()

	
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


def click_submit_button(browser, selector):
	button = browser.find_element_by_css_selector(selector)
	button.click()	

if __name__ == '__main__':
	link = "http://suninjuly.github.io/redirect_accept.html"
	handling_different_windows_test(link)