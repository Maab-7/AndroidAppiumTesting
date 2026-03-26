import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.app = "/Users/marco/Downloads/ApiDemos-debug.apk"
    options.automation_name = "UiAutomator2"
    options.no_reset = False

    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4723",
        options=options
    )

    yield driver
    driver.quit()