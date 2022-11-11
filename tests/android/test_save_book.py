__author__ = 'miserylab'
import os
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser
from litres_mobile_tests.model import app

from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv('email')
PASSWORD = os.getenv('password')


@allure.tag('mobile')
@allure.title('Test save a book')
def test_save_a_book():
    app.skip_onboarding_adult_content_questions()

    with allure.step('Click on seach field'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/search')).click()
    with allure.step('Search "Ubik"'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/et_search_query')).send_keys('Ubik')

    with allure.step('Content should be found'):
        browser.all(
            (AppiumBy.ID, 'ru.litres.android:id/horizontal_book_card')
        ).should(have.size(1))

    with allure.step('Save a book'):
        browser.all(
            (AppiumBy.ID, 'ru.litres.android:id/horizontal_book_card'))[0].element(
            (AppiumBy.ACCESSIBILITY_ID, 'Add to shelved')).click()
        browser.driver.hide_keyboard()

    with allure.step('Click on Profile Menu button'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/ll_profile_menu_item')).click()
    with allure.step('Click on Profile Menu button'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/login_button')).click()

    with allure.step('Enter login'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/login')).send_keys(EMAIL)
    with allure.step('Enter password'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/password')).send_keys(PASSWORD)
    with allure.step('Click "Log in" button'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/sign_in_btn')).click()


    with allure.step('Check saved book in "My books" menu "Saved"'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'My books')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'SAVED')).click()

    with allure.step('Content should be found'):
        browser.all(
            (AppiumBy.ID, 'ru.litres.android:id/cardView')
        ).should(have.size(1))
        browser.all(
            (AppiumBy.ID, 'ru.litres.android:id/horizontal_book_card')
        )[0].element((AppiumBy.ID, 'ru.litres.android:id/bookName')).should(have.text('Ubik'))


    #post-condition
    app.delete_saved_book_from_account()
