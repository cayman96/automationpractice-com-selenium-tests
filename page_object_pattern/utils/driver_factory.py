from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chService
from selenium.webdriver.firefox.service import Service as ffService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from page_object_pattern.utils.gh_token import GeckoToken
import os
# ta klasa będzie nam służyć do wyboru drivera, jeśli chcemy przetestować naszą apkę na innych przeglądarkach.
class DriverFactory:
    # oznaczymy sobie ta metodę jako statyczną - nie będzie wymagać od nas tworzenia obiektu klasy DriverFactory.
    @staticmethod
    # self nam tu nie jest potrzebny
    def get_driver(browser):
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_experimental_option("detach", True)
            return webdriver.Chrome(service=chService(ChromeDriverManager().install()), options=options)
        elif browser == "firefox":
            # jebać firefoxa jak ja cie kurwo nienawidze aaaaaaaaaaaaaaaaaa
            # kurwa token w kodzie - zły pomysł!
            os.environ['GH_TOKEN'] = GeckoToken.get_token()
            return webdriver.Firefox(service=ffService(GeckoDriverManager().install()))
        else:
            raise Exception("Please provide valid driver name")