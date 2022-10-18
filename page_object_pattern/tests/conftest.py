import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.support.wait import WebDriverWait
from page_object_pattern.utils.driver_factory import DriverFactory

# deklaruję waita po to, aby go potem przekazać do funkcji wywoływanych podczas testu z klas stron
wait = None

@pytest.fixture
def setup(request):
    # na razie tylko chrome, potem zmodyfikuję aby też na firefoxie się uruchamiał
    browser = "chrome"
    # tworzenie webdrivera
    driver = DriverFactory.get_driver(browser)
    """webdriver do firefoxa jest zjebany i sam jakby nie ogarnia że ma odpalić się w zmaksymalizowanym oknie.
    chrome nie ma tego problemu, dlatego ten warunek, gdy jako driver użyty zostanie firefox"""
    if browser == "firefox":
        driver.maximize_window()
    # implicit wait aby test się wywalił po 4-sekundach jak się nie driver nie odpali
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
