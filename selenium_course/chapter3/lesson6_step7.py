link = "http://selenium1py.pythonanywhere.com/"
"""
Test should be run with the following command (plugin pytest-rerunfailures is used):
pytest -v --tb=line --reruns 1 --browser_name=chrome lesson6_step7.py
"""

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#magic_link")