from datetime import datetime
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class", autouse=True)
def driver_setup(request):
    print("\nSetting up browser")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    request.cls.driver = driver
    print("\nBrowser up and running")
    yield
    print("\nTesting finished \nClosing browser")
    driver.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    print(f"rep to {rep}")
    print(setattr(item, "rep_" + rep.when, rep))


@pytest.fixture(scope="function", autouse=True)
def attach_screenshot_on_fail(request):
    yield
    if request.node.rep_setup.failed:
        print("setting up env failed")
    elif request.node.rep_call.failed:
        print(f"Test execution for {request.node.name} failed, taking a screenshot")
        driver = request.cls.driver
        file_name = f'/screenshots/{request.node.name}_{datetime.today().strftime("%Y-%m-%d_%H-%M")}.png'
        print(f"file name to {file_name}")
        take_screenshot(driver, file_name)
        attach_screenshot_to_report(file_name)


def take_screenshot(driver, file_name):
    driver.save_screenshot(file_name)
    print("Screenshot saved")


def attach_screenshot_to_report(file_name):
    allure.attach.file(file_name, attachment_type=allure.attachment_type.PNG)
    print("Screenshot attached to the report")


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
