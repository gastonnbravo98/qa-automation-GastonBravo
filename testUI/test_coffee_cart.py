import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://coffee-cart.app/"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)  
    driver.get(URL)
    yield driver
    driver.quit()

def agregar_cafe(driver, nombre):
    driver.find_element(By.XPATH, f"//div[@data-test='{nombre}']").click()


def texto_carrito(driver):
    return driver.find_element(By.XPATH, "//a[@aria-label='Cart page']").text.lower()


def ir_al_carrito(driver):
    driver.find_element(By.XPATH, "//a[@aria-label='Cart page']").click()


def test_agregar_cafe_al_carrito(driver):
    assert texto_carrito(driver) == "cart (0)"

    agregar_cafe(driver, "Cappuccino")

    assert texto_carrito(driver) == "cart (1)"

    ir_al_carrito(driver)
    total = driver.find_element(By.XPATH, "//button[@data-test='checkout']")
    assert "Total: $19.00" in total.text


def test_eliminar_cafe_del_carrito(driver):
    agregar_cafe(driver, "Espresso")
    ir_al_carrito(driver)

    driver.find_element(By.XPATH, "//button[contains(@class, 'delete')]").click()

    assert "No coffee, go add some." in driver.find_element(By.ID, "app").text
    assert texto_carrito(driver) == "cart (0)"


def test_compra_completa(driver):
    agregar_cafe(driver, "Cappuccino")
    ir_al_carrito(driver)
    driver.find_element(By.XPATH, "//button[@data-test='checkout']").click()

    driver.find_element(By.ID, "name").send_keys("Gaston Test")
    driver.find_element(By.ID, "email").send_keys("gaston@test.com")
    driver.find_element(By.ID, "submit-payment").click()

    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.XPATH, "//div[contains(@class, 'success')]"), "Thanks for your purchase."
        )
    )

    mensaje = driver.find_element(By.XPATH, "//div[contains(@class, 'success')]")
    assert "Thanks for your purchase." in mensaje.text
    assert texto_carrito(driver) == "cart (0)"