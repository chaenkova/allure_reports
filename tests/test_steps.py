import allure
from selene import browser, by, be


def test_search_issue():
    with allure.step('Открыть \'github.com\''):
        browser.open('https://github.com')

    with allure.step(
            'Выполнить поиск \'eroshenkoam/allure-example\''
    ):
        browser.element('.search-input').click()
        browser.element('#query-builder-test').type(
            'eroshenkoam/allure-example'
        ).submit()

    with allure.step('Выбрать \'eroshenkoam/allure-example\''):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Перейти в issues'):
        browser.element('#issues-tab').click()

    with allure.step('Находим Issue с номером #89'):
        browser.element(by.partial_text("#89")).should(be.visible)
