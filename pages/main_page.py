from config.locators import MainPageLocators as locators
from pages.base_page import BasePage


class MainPage(BasePage):
	def move_to_catalog(self) -> None:
		self.move_to_element(locators.CATALOG)

	def click_running_shoes(self) -> None:
		self.move_to_catalog()
		self.click(locators.RUNNING_SHOES)

	def click_boots(self) -> None:
		self.move_to_catalog()
		self.click(locators.BOOTS)

	def click_shoes(self) -> None:
		self.move_to_catalog()
		self.click(locators.SHOES)

	def click_sneakers(self) -> None:
		self.move_to_catalog()
		self.click(locators.SNEAKERS)

	def click_wintry(self) -> None:
		self.move_to_catalog()
		self.click(locators.WINTRY)
