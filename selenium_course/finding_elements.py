from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

URL = "http://suninjuly.github.io/simple_form_find_task.html"
BUTTON_ID = "submit_button"

def failed_test(browser):
	browser.get(URL)
	button = browser.find_element_by_id("submit")
	button.click()


def find_by_id_first(browser):
	browser.get(URL)
	button = browser.find_element_by_id(BUTTON_ID)
	button.click()


def find_by_id_second(browser):
	browser.get(URL)
	button = browser.find_element(By.ID, BUTTON_ID)
	button.click()


if __name__ == "__main__":
	browser = webdriver.Chrome()
	try:
		find_by_id_first(browser)
		find_by_id_second(browser)
		failed_test(browser)
	except NoSuchElementException:
		print("Element is not found.")
	finally:
		browser.quit()