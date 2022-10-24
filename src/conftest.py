from datetime import datetime
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

"""Fixture to install webdriver"""
@pytest.fixture(scope="class", autouse=True)
def driver_setup(request, browser_selected):
    print("\nSetting up browser")
    if browser_selected=='chrome':
        print(f"Installing {browser_selected} browser")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    else:
        print("Please select chrome as a browser")
    driver.maximize_window()
    request.cls.driver = driver
    print("\nBrowser up and running")
    yield
    print("\nTesting finished \nClosing browser")
    driver.quit()

"""Hook implementation to store result of the test"""
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    print(f'rep to {rep}')
    print(setattr(item, "rep_" + rep.when, rep))

"""Fixture to take screenshot after test fail
Save screenshot and attach it to allure test report"""
@pytest.fixture(scope="function", autouse=True)
def attach_screenshot_on_fail(request):
    yield
    if request.node.rep_setup.failed:
        print("setting up env failed")
    elif request.node.rep_call.failed:
        print(f"Test execution for {request.node.name} failed, taking a screenshot")
        driver = request.cls.driver
        file_name = f'{request.node.name}_{datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'.replace(
            "/", "_"
        ).replace(
            "::", "__"
        )
        take_screenshot(driver, file_name)
        print("Screenshot saved")   
        attach_screenshot_to_report(file_name)
        print("Screenshot attached to the report")
    elif request.node.rep_teardown.failed:
        print("teardown failed")

def take_screenshot(driver, file_name):
    driver.save_screenshot(file_name)
    return file_name

def attach_screenshot_to_report(file_name):
    allure.attach.file(file_name, attachment_type=allure.attachment_type.PNG)

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Currently available option: chrome"
    )

@pytest.fixture(scope='class')
def browser_selected(request):
    return request.config.getoption("--browser")

#TO DO: add fixture to run headlessly or not