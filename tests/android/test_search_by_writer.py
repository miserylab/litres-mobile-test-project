__author__ = 'miserylab'

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser

from litres_mobile_tests.model import app


@allure.tag('mobile')
@allure.title('Test search by writer')
def test_search_by_writer():
    app.skip_onboarding_adult_content_questions()

    with allure.step('Click on seach field'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/search')).click()
    with allure.step('Search "Philip Dick"'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/et_search_query')).send_keys('Philip Dick')
    with allure.step('Check "All results" is selected'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'All results')).should(have.attribute('selected').value('true'))

    with allure.step('Check results preview'):
        browser.element(
            (AppiumBy.ID, 'ru.litres.android:id/tv_book_count_search_item'))\
            .should(have.attribute('text').value('Author - 168 books'))
        browser.element(
            (AppiumBy.ID, 'ru.litres.android:id/tv_name_search_item')).should(have.attribute('text').value('Philip Dick'))
        browser.element(
            (AppiumBy.ID, 'ru.litres.android:id/tv_additional_info_search_item'))\
            .should(have.attribute('text')
                    .value('Genres: Science fiction, Graphic arts, Literary criticism'))

    with allure.step('Click on results preview'):
        browser.all((AppiumBy.ID, 'ru.litres.android:id/searchList')).all(
            (AppiumBy.CLASS_NAME, 'android.widget.FrameLayout'))[0].click()

    with allure.step('Check opened page'):
        browser.element(
            (AppiumBy.ID, 'ru.litres.android:id/name_view')).should(have.attribute('text').value('Philip Dick'))