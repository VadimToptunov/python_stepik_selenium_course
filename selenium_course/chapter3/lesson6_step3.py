import math
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(20)
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def get_answer():
	answer = math.log(int(time.time()))
	print(str(answer))
	return str(answer)


@pytest.mark.parametrize('lesson_id', 
	["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_user_should_get_correct_optional_feedback(browser, get_answer, lesson_id):
	link = f"https://stepik.org/lesson/{lesson_id}/step/1"
	browser.get(link)

	WebDriverWait(browser, 20).until(EC.visibility_of_element_located(
		(By.CSS_SELECTOR, ".ember-text-area.ember-view.textarea.string-quiz__textarea"))).send_keys(get_answer)

	WebDriverWait(browser, 20).until(EC.element_to_be_clickable(
		(By.CSS_SELECTOR, ".submit-submission"))).click()

	optional_feedback = WebDriverWait(browser, 20).until(EC.visibility_of_element_located(
		(By.CSS_SELECTOR, ".smart-hints__hint"))).text

	assert optional_feedback == "Correct!", f"Otional feedback is incorrect on page {link}"
