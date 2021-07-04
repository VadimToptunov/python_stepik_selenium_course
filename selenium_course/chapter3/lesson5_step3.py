import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


"""
@pytest.mark.<any_word_you need>

The <any_word_you_need> should be registered in file pytest.ini like this:
[pytest]
markers =
    smoke: marker for smoke tests
    regression: marker for regression tests

And it should be ran like this (to run only( tests with the mark "smoke"):

pytest -s -v -m smoke lesson5_step2.py

or like this (to run all tests but the ones marked "smoke"):
pytest -s -v -m "not smoke" lesson5_step2.py

or like this (to run smoke AND regresson tests):
pytest -s -v -m "smoke or regression" lesson5_step2.py

or like this (to run ONLY smoke tests for win10):
pytest -s -v -m "smoke and win10" lesson5_step3.py

"""

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
