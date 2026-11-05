from typing import Iterator

from pytest import Item, fixture
from selenium.webdriver.remote.webdriver import WebDriver

from config.logger_config import get_logger
from pages.main_page import MainPage

log = get_logger(__name__)


def pytest_runtest_setup(item: Item) -> None:
	log.info('START TEST: %s', item.name)


def pytest_runtest_teardown(item: Item) -> None:
	log.info('END TEST: %s', item.name)


@fixture(scope='class')
def main_page(driver: WebDriver) -> Iterator[MainPage]:
	yield MainPage(driver)
