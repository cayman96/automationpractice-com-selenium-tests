from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from page_object_pattern.locators.locators import *
from selenium.webdriver.support.wait import WebDriverWait
import logging
import allure

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.wait = WebDriverWait(self.driver, 10, 0.5)

    @allure.step("Klikam w główny banner i ląduję z powrotem na głównej")
    def click_on_header_banner(self):
        self.logger.info("Klikam na banner na górze")
        self.driver.find_element(By.XPATH, HeaderLocators.upperBanner).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="click on header banner",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Klikam w przycisk \"Contact us\"")
    def click_on_contact_us(self, wait):
        self.logger.info("Klikam w przycisl \'Contact us\'")
        self.driver.find_element(By.XPATH, HeaderLocators.contactUsBtn).click()
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, ContactUsLocators.sendMsgForm)))
        allure.attach(self.driver.get_screenshot_as_png(), name="click on contact us button",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Klikam w przycisk 'Women'")
    def click_on_women(self, wait):
        self.logger.info("Klikam w przycisk 'Women'")
        self.driver.find_element(By.XPATH, HeaderLocators.womenBtn).click()
        allure.attack(self.driver.get_screenshot_as_png(), name="click on women button",
                      attachment_type=AttachmentType.PNG)