import os
from selenium import webdriver
import time

def file_upload_test(link):
	try:
		browser = webdriver.Chrome()
		browser.get(link)

		find_by_name(browser, "firstname", "Ivan")
		find_by_name(browser, "lastname", "Ivanov")
		find_by_name(browser, "email", "my.mail@post.ru")

		upload_dutton = browser.find_element_by_id("file")
		upload_dutton.send_keys(get_file_path())

		submit_button = browser.find_element_by_css_selector(".btn.btn-primary")
		submit_button.click()

		time.sleep(30)
	finally:
		browser.quit()



def find_by_name(browser, name, input_data):
	element = browser.find_element_by_name(name)
	element.send_keys(input_data)


def get_file_path():
	current_dir = os.path.abspath(os.path.dirname(__file__))
	return os.path.join(current_dir, 'file.txt')


if __name__ == "__main__":
	link = "http://suninjuly.github.io/file_input.html"
	file_upload_test(link)