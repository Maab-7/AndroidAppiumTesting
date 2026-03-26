import allure
import pytest
from appium.webdriver.common.appiumby import AppiumBy

@allure.title("Verificar que la app abre correctamente")
@allure.description("Verifica que la app ApiDemos abre y tiene actividad")
def test_app_opens(driver):
    with allure.step("Verificar que la app está abierta"):
        assert driver.current_activity is not None
        print(f"Activity actual: {driver.current_activity}")

@allure.title("Navegar a Views")
@allure.description("Verifica que se puede navegar a la sección Views")
def test_navigate_to_views(driver):
    with allure.step("Click en Views"):
        views = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Views")
        views.click()

    with allure.step("Verificar que navegó a Views"):
        assert driver.current_activity is not None

@allure.title("Navegar a Animation")
@allure.description("Verifica que se puede navegar a la sección Animation")
def test_navigate_to_animation(driver):
    with allure.step("Click en Animation"):
        animation = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Animation")
        animation.click()

    with allure.step("Verificar navegación a Animation"):
        assert driver.current_activity is not None

@allure.title("Verificar elementos en pantalla principal")
@allure.description("Verifica que los elementos principales están presentes")
def test_main_elements_present(driver):
    with allure.step("Verificar que Views está presente"):
        views = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Views")
        assert views.is_displayed()

    with allure.step("Verificar que Animation está presente"):
        animation = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Animation")
        assert animation.is_displayed()

    with allure.step("Verificar que OS está presente"):
        os_element = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "OS")
        assert os_element.is_displayed()