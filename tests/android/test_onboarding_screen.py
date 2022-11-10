__author__ = 'miserylab'

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser
from allure import step
from selene import be




@allure.tag('mobile')
@allure.title('Check onboarding screens')
def test_onboarding_screen():

    with allure.step('Select a content language'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/choosebutton')).click()

    with allure.step('Check onboarding screen 1'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/btn_onboarding_litres_app_books')).should(be.visible)
        browser.element((AppiumBy.ID, 'ru.litres.android:id/iv_onboarding_litres_app_arrow')).should(be.visible)
        browser.element(
            (AppiumBy.ID, 'ru.litres.android:id/tv_onboarding_litres_app_title')).should(have.text('Listen to audio books'))
        browser.element(
            (AppiumBy.ID, 'ru.litres.android:id/tv_onboarding_litres_description')).should(have.attribute('text').value('Listen to audiobooks AUDIO when walking, jogging or in public transport'))
        browser.element((AppiumBy.ID, 'ru.litres.android:id/btn_onboarding_litres_app_skip')).should(be.visible)
        browser.element((AppiumBy.ID, 'ru.litres.android:id/btn_onboarding_litres_app_next')).should(be.visible)

    with allure.step('Click "More" on onboarding screen 1'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/btn_onboarding_litres_app_next')).click()

    with allure.step('Check onboarding screen 2'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/btn_onboarding_litres_app_books')).should(be.visible)
        browser.element((AppiumBy.ID, 'ru.litres.android:id/iv_onboarding_litres_app_arrow')).should(be.visible)
        browser.element(
            (AppiumBy.ID, 'ru.litres.android:id/tv_onboarding_litres_app_title'))\
            .should(have.text('There is always an option'))
        browser.element(
            (AppiumBy.ID, 'ru.litres.android:id/tv_onboarding_litres_description'))\
            .should(have.text('Choose e-books TEXT'))
        browser.element((AppiumBy.ID, 'ru.litres.android:id/btn_onboarding_litres_app_next')).should(be.visible)

    with allure.step('Click "Clear" on onboarding screen 2'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/btn_onboarding_litres_app_next')).click()

    with allure.step('Check Adult Books menu is visible'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/btnDisableAdultContent')).should(be.visible)
