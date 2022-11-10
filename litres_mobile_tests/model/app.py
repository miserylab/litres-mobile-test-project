from selene import be
from selene.support.shared import browser
from appium.webdriver.common.appiumby import AppiumBy
import allure


def skip_onboarding_adult_content_questions():
    with allure.step('Select a content language'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/choosebutton')).click()
    # with step('Skip blank page'):
    #     browser.element((AppiumBy.ID, 'android:id/content')).click()
    with allure.step('Skip onboarding page'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/btn_onboarding_litres_app_skip')).click()
    with allure.step('Disable adult content'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/btnDisableAdultContent')).click()
    with allure.step('Confirm disable adult content'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/btnConfirmDisableAdultContent')).click()


def delete_saved_book_from_account():
    if browser.element((AppiumBy.ID, 'ru.litres.android:id/horizontal_book_card')).matching(be.existing):
        browser.all(
            (AppiumBy.ID, 'ru.litres.android:id/horizontal_book_card')
        )[0].element((AppiumBy.ACCESSIBILITY_ID, 'More')).click()
        browser.all((AppiumBy.ID, 'android:id/title'))[1].click()

