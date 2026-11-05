from config.urls import URLs
from pages.main_page import MainPage
from utils.assertion import Assert


def test_running_shoes(main_page: MainPage) -> None:
	main_page.open()
	main_page.click_running_shoes()

	Assert.check_url(main_page, URLs.RUNNING_SHOES_PAGE)


def test_boots(main_page: MainPage) -> None:
	main_page.open()
	main_page.click_boots()

	Assert.check_url(main_page, URLs.BOOTS_PAGE)


def test_shoes(main_page: MainPage) -> None:
	main_page.open()
	main_page.click_shoes()

	Assert.check_url(main_page, URLs.SHOES_PAGE)


def test_sneakers(main_page: MainPage) -> None:
	main_page.open()
	main_page.click_sneakers()

	Assert.check_url(main_page, URLs.SNEAKERS_PAGE)


def test_wintry(main_page: MainPage) -> None:
	main_page.open()
	main_page.click_wintry()

	Assert.check_url(main_page, URLs.WINTRY_PAGE)
