import math
import time
from selenium import webdriver

def math_link_text_test(css1, css2, css3, css4):
	link = "http://suninjuly.github.io/find_link_text"
	link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
	try:
		browser = webdriver.Chrome()
		browser.get(link)
		new_link = browser.find_element_by_link_text(link_text)
		new_link.click()
		input1 = browser.find_element_by_tag_name(css1)
		input1.send_keys("Ivan")
		input2 = browser.find_element_by_name(css2)
		input2.send_keys("Petrov")
		input3 = browser.find_element_by_class_name(css3)
		input3.send_keys("Smolensk")
		input4 = browser.find_element_by_id(css4)
		input4.send_keys("Russia")
		button = browser.find_element_by_css_selector("button.btn")
		button.click()
		time.sleep(30)

	finally:
		browser.quit()


if __name__ == "__main__":
	css1 = "input"
	css2 = "last_name"
	css3 = "city"
	css4 = "country"
	math_link_text_test(css1, css2, css3, css4)
