import pytest
from page_object_pattern.tests.conftest import return_wait
from page_object_pattern.pages.main_page import MainPage

@pytest.mark.usefixtures("setup")
class TestMainPage:
    def test_main_page_click_banner(self, setup):
        self.driver.get("http://automationpractice.com/index.php")
        main = MainPage(self.driver)
        main.click_on_header_banner()
        assert self.driver.title == "My Store"
        main.click_on_contact_us(return_wait())
        assert self.driver.title == "Contact us - My Store"

    def test_main_page_click_contact_us(self, setup):
        pass
