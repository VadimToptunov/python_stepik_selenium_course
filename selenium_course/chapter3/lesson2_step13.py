from selenium import webdriver
import time
import unittest

class TestRegistration(unittest.TestCase):


	def setUp(self):
		"""
		Sets up environment before test. In this case it creates a instance of a browser.
		"""
		self.browser = webdriver.Chrome()

	def test_registration(self):
		"""
		Successful test on registration.
		
		Steps:
		1. Open a browser on link http://suninjuly.github.io/registration1.html;
		2. Fill all registration fields: name, last name, email, phone, address;
		3. Click "Submit" button;
		4. Wait till a new page is opened;
		5. Check the welcome text is equal to: "Congratulations! You have successfully registered!"
		"""
		link = "http://suninjuly.github.io/registration1.html"
		browser = self.browser
		browser.get(link)

		self.fill_registration_info(browser)
		self.click_submit(browser)
		welcome_text = self.get_welcome_text(browser)
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

	def test_registration_failed(self):
		"""
		Failed test on registration.
		
		Steps automated:
		1. Open a browser on link http://suninjuly.github.io/registration2.html;
		2. Fill all registration fields: name, last name, email, phone, address;
		3. Click "Submit" button;
		4. Wait till a new page is opened;
		5. Check the welcome text is equal to: "Congratulations! You have successfully registered!"

		The test fails on step 2. It cannot find field for last name.
		"""
		link = "http://suninjuly.github.io/registration2.html"
		browser = self.browser
		browser.get(link)

		self.fill_registration_info(browser)
		self.click_submit(browser)
		welcome_text = self.get_welcome_text(browser)
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


	def fill_registration_info(self, browser):
		self.fill_form(browser, "first", "first", "Ivan")
		self.fill_form(browser, "first", "second", "Ivanov")
		self.fill_form(browser, "first", "third", "my.mail@yandex.ru")
		self.fill_form(browser, "second", "first", "+79601123456")
		self.fill_form(browser, "second", "second", "Lenin avenue, 10")

	def click_submit(self, browser):
		button = browser.find_element_by_css_selector("button.btn")
		button.click()


	def get_welcome_text(self, browser):
		time.sleep(1)
		welcome_text_elt = browser.find_element_by_tag_name("h1")
		return welcome_text_elt.text


	def tearDown(self):
		"""
		Closes browser after each test
		"""
		time.sleep(10)
		self.browser.quit()


	def fill_form(self, browser, class_part1, class_part2, input):
		xpath = f"//*[@class='{class_part1}_block']//*[@class='form-control {class_part2}']"
		elem = browser.find_element_by_xpath(xpath)
		elem.send_keys(input)


if __name__ == "__main__":
	unittest.main()

	# unittest.main(link1, link2)
    # link = "http://suninjuly.github.io/registration2.html"
    # registration_test(link)
