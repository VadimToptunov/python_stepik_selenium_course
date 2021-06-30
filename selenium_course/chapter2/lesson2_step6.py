import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


def execute_script_test(link):
	try:
		browser = webdriver.Chrome()
		browser.get(link)

		x_value = browser.find_element_by_id("input_value").text

		answer = calc(x_value)

		input_field = browser.find_element_by_id("answer")
		input_field.send_keys(answer)

		submit_button = browser.find_element_by_css_selector(".btn.btn-primary")
		scroll_to(browser, "button", submit_button)

		checkbox = browser.find_element_by_id("robotCheckbox")
		checkbox.click()

		robots_rule_radio = browser.find_element_by_id("robotsRule")
		robots_rule_radio.click()


		submit_button.click()

		time.sleep(30)
	finally:
		browser.quit()


def scroll_to(browser, tagname, element):
	script = f"document.getElementsByTagName('{tagname}')[0].scrollIntoView(true);"
	browser.execute_script(script, element)
	

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


if __name__ == "__main__":
	link = "http://suninjuly.github.io/execute_script.html"
	execute_script_test(link)




# select = Select(browser.find_element_by_tag_name("select"))