from typing import TypeVar

from config.logger_config import get_logger
from pages.base_page import BasePage

log = get_logger(__name__)
T = TypeVar('T')


class Assert:
    @staticmethod
    def compare_values(current_value: T, expected_value: T) -> None:
        log.info('assert %s == %s', current_value, expected_value)
        assert current_value == expected_value, (
            f"The values: {current_value} and {expected_value} don't match"
        )

    @staticmethod
    def check_url(page: BasePage, expected_url: str) -> None:
        log.info('assert %s == %s', page.driver.current_url, expected_url)
        assert page.check_url(expected_url), f'Incorrect URL: {expected_url}'
