import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

def explicit_wait_test(link):
	try:
		browser = webdriver.Chrome()
		browser.get(link)

		book_button = browser.find_element_by_css_selector("#book.btn.btn-primary")


		WebDriverWait(browser, 12).until(
			EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

		book_button.click()

		x_value = browser.find_element_by_id("input_value").text

		answer = calc(x_value)

		input_field = browser.find_element_by_id("answer")
		input_field.send_keys(answer)

		submit_button = browser.find_element_by_css_selector("#solve.btn.btn-primary")
		submit_button.click()

		time.sleep(30)

	finally:
		browser.quit()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


if __name__ == '__main__':
	link = "http://suninjuly.github.io/explicit_wait2.html"
	explicit_wait_test(link)