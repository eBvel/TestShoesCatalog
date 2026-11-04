from config.settings import Settings as settings
from config.urls import URLs
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait as wait


class BasePage:

    def __init__(self, driver: WebDriver):
        self.url = URLs.BASE_PAGE
        self.driver = driver

    def open(self):
        if self.url:
            self.driver.get(self.url)
        else:
            raise ValueError(f'Incorrect URL: {self.url}')

    def find(self, condition):
        return wait(self.driver, settings.TIMEOUT).until(condition)

    def find_visible_element(self, locator):
        return self.find(EC.visibility_of_element_located(locator))

    def find_clickable_element(self, locator):
        return self.find(EC.element_to_be_clickable(locator))

    def move_to_element(self, locator) -> None:
        (
            ActionChains(self.driver)
            .move_to_element(self.find_visible_element(locator))
            .perform()
        )

    def click(self, locator):
        button = self.find_clickable_element(locator)
        try:
            button.click()
        except ElementClickInterceptedException:
            self.driver.execute_script('arguments[0].click()', button)

    def check_url(self, url: str):
        try:
            return self.find(EC.url_to_be(url))
        except TimeoutException:
            return False
