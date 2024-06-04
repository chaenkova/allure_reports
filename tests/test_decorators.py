import allure
from selene import browser, by, be


def test_search_issue():
    open_site('https://github.com')

    search_repository('eroshenkoam/allure-example')
    open_repository('eroshenkoam/allure-example')
    click_issues_tab()

    issue_should_be_visible('#89')


@allure.step('Открыть {link}')
def open_site(link):
    browser.open(link)


@allure.step('Выполнить поиск {value}')
def search_repository(value):
    browser.element('.search-input').click()
    browser.element('#query-builder-test').type(value).press_enter()


@allure.step('Выбрать {link}')
def open_repository(link):
    browser.element(by.link_text(link)).click()


@allure.step('Перейти в "Issues"')
def click_issues_tab():
    browser.element('#issues-tab').click()


@allure.step('Находим Issue с номером {number}')
def issue_should_be_visible(number):
    browser.element(by.partial_text(number)).should(be.visible)
