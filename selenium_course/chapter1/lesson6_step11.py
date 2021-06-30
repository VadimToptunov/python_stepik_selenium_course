from selenium import webdriver
import time


def registration_test(link):
    try: 
        browser = webdriver.Chrome()
        browser.get(link)

        # Заполняем формы:
        # Имя
        fill_forms(browser, "first", "first", "Ivan")
        # Фамилия
        fill_forms(browser, "first", "second", "Ivanov")
        # E-mail
        fill_forms(browser, "first", "third", "my.mail@yandex.ru")
        # Номер телефона
        fill_forms(browser, "second", "first", "+79601123456")
        # Адрес
        fill_forms(browser, "second", "second", "Lenin avenue, 10")

        # Находим кнопку регистрации
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

def fill_forms(browser, class_part1, class_part2, input):
    # Формируем строку xpath'а
    xpath = f"//*[@class='{class_part1}_block']//*[@class='form-control {class_part2}']"
    # Находим элемент
    elem = browser.find_element_by_xpath(xpath)
    # Пишем данные
    elem.send_keys(input)


if __name__ == "__main__":
    link = "http://suninjuly.github.io/registration2.html"
    registration_test(link)
