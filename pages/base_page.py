from typing import Callable, Literal, TypeVar

from selenium.common import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as wait

from config.settings import Settings as settings
from config.urls import URLs

D = TypeVar('D', bound=WebDriver | WebElement)
T = TypeVar('T')

ByType = Literal[
	'id',
	'xpath',
	'link text',
	'partial link text',
	'name',
	'tag name',
	'class name',
	'css selector',
]
LocatorType = tuple[ByType, str]


class BasePage:
	def __init__(self, driver: WebDriver) -> None:
		self.url = URLs.BASE_PAGE
		self.driver = driver

	def open(self) -> None:
		if self.url:
			self.driver.get(self.url)
		else:
			raise ValueError(f'Incorrect URL: {self.url}')

	def find(
		self, condition: Callable[[WebDriver], Literal[False] | T]
	) -> WebElement | T:
		return wait(self.driver, settings.TIMEOUT).until(condition)

	def find_visible_element(self, locator: LocatorType) -> WebElement:
		return self.find(EC.visibility_of_element_located(locator))

	def find_clickable_element(self, locator: LocatorType) -> WebElement:
		return self.find(EC.element_to_be_clickable(locator))

	def move_to_element(self, locator: LocatorType) -> None:
		(
			ActionChains(self.driver)
			.move_to_element(self.find_visible_element(locator))
			.perform()
		)

	def click(self, locator: LocatorType) -> None:
		button: WebElement = self.find_clickable_element(locator)
		try:
			button.click()
		except ElementClickInterceptedException:
			self.driver.execute_script('arguments[0].click()', button)

	def check_url(self, url: str) -> bool:
		try:
			return bool(self.find(EC.url_to_be(url)))
		except TimeoutException:
			return False
