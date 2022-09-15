import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.support.wait import WebDriverWait
from page_object_pattern.utils.driver_factory import DriverFactory

wait = None

@pytest.fixture
def setup(request):
    # na razie tylko chrome, potem zmodyfikuję aby też na firefoxie się uruchamiał
    browser = "chrome"
    driver = DriverFactory.get_driver(browser)
    if browser == "firefox":
        driver.maximize_window()
    driver.implicitly_wait(4)
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    global wait
    wait = WebDriverWait(driver, 10.0, 0.5)
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name="test failed", attachment_type=AttachmentType.PNG)
    driver.quit()

def return_wait():
    return wait
