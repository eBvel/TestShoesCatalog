from typing import Union

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.options import ArgOptions
from selenium.webdriver.common.webdriver import LocalWebDriver, RemoteWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pytest import fixture, FixtureRequest


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        default='chrome',
        help='The type of browser to run tests. '
             'Possible values: "chrome", "firefox", "remote".'
    )
    parser.addoption(
        '--remote',
        action='store',
        default=None,
        help='Selenium Grid URL, e.g. http://localhost:4444/wd/hub'
    )
    parser.addoption(
        '--view-mode',
        action='store_true',
        default=False,
        help='The mode, that can run browser without UI.'
    )


@fixture(scope="session")
def browser_type(request: FixtureRequest) -> str:
    return request.config.getoption('--browser').lower()


@fixture(scope="session")
def view_mode(request: FixtureRequest) -> bool:
    return request.config.getoption('--view-mode')


@fixture(scope="session")
def remote_url(request: FixtureRequest) -> str:
    return request.config.getoption('--remote')


@fixture(scope='session')
def driver(
        browser_type: str,
        view_mode: bool,
        remote_url: str
):

    if browser_type == 'chrome':
        options = ChromeOptions()
    elif browser_type == 'firefox':
        options = FirefoxOptions()
    else:
        raise ValueError(f'Incorrect value of browser type {browser_type}')


    if not view_mode:
        options.add_argument('--headless')

    if remote_url:
        driver = webdriver.Remote(
            command_executor=remote_url,
            options=options
        )
    else:
        if browser_type == 'chrome':
            driver = webdriver.Chrome(
                options=options,
                service=ChromeService(ChromeDriverManager().install())
            )
        else:
            driver = webdriver.Firefox(
                options=options,
                service=FirefoxService(GeckoDriverManager().install())
            )

    yield driver

    driver.close()