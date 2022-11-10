__author__ = 'miserylab'
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser
from allure import step


from litres_mobile_tests.model import app


@allure.tag('mobile')
@allure.title('Check main page after onboarding skip')
def test_main_page_after_onboarding_skip():
    app.skip_onboarding_adult_content_questions()

    with allure.step('Check "Catalog" is selected'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Catalog')).should(have.attribute('selected').value('true'))
    with allure.step('Check "Books to read" is selected'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Books to read')).should(have.attribute('selected').value('true'))