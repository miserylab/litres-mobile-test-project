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
@allure.title('Test login')
def test_login():
    app.skip_onboarding_adult_content_questions()

    with allure.step('Click on Profile Menu button'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/ll_profile_menu_item')).click()
    with allure.step('Check "Profile" is selected'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Profile')).should(have.attribute('selected').value('true'))
    with allure.step('Click on Profile Menu button'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/login_button')).click()

    with allure.step('Enter login'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/login')).type(EMAIL)
    with allure.step('Enter password'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/password')).type(PASSWORD)
    with allure.step('Click "Log in" button'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/sign_in_btn')).click()

    with allure.step('Check user is logged'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/user_name')).should(have.text('Registered reader'))
        browser.element((AppiumBy.ID, 'ru.litres.android:id/user_login')).should(have.text(EMAIL))






