import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        """
        The whole run will be considered successful, but the test will be marked as XFAIL
        XFAIL = Expected fail on test.

        reason - the mark to show in console

        If there's a reason, then the run should be run like this:
        pytest -rx -v lesson5_step5.py

        When the bug is fixed, it is displayed as XPASS ("unexpectedly pass") in console and 
        then the annotation @pytest.mark.xfail can be removed
        """
        browser.get(link)
        browser.find_element_by_css_selector("button.favorite")