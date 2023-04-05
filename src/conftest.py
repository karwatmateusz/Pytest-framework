from datetime import datetime
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from utilities.Logger import Logger
import logging


log = Logger(logging.DEBUG)


@pytest.fixture(scope="class", autouse=True)
def driver_setup(request):
    print("\nSetting up browser")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    request.cls.driver = driver
    print("Browser up and running")
    yield
    print("\nTesting finished, closing browser")
    driver.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="function", autouse=True)
def check_test_result(request):
    yield
    if request.node.rep_setup.failed:
        print("setting up env failed")
        log.error("Setting up env failed")
    else:
        log.info(
            f"Test execution for something like {request.node.name} {request.node.rep_call.outcome}, taking a screenshot"
        )
        driver = request.cls.driver
        file_name = f'screenshots/{request.node.name}_{datetime.today().strftime("%Y-%m-%d_%H-%M")}.png'
        take_screenshot(driver, file_name)
        attach_screenshot_to_report(file_name)


def take_screenshot(driver, file_name):
    driver.save_screenshot(file_name)
    log.info(f"Screenshot {file_name} taken")


def attach_screenshot_to_report(file_name):
    allure.attach.file(file_name, attachment_type=allure.attachment_type.PNG)
    log.info(f"Screenshot {file_name} attached to the report")


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Currently available option: chrome",
    )


@pytest.fixture(scope="class")
def browser_selected(request):
    return request.config.getoption("--browser")


# TO DO: add fixture to run headlessly or not
