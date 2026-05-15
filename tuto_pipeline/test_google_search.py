import allure
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    d = webdriver.Chrome(options=options)
    d.maximize_window()
    yield d
    d.quit()
    
                                        


@allure.epic("Moteurs de recherche")
@allure.feature("Google Search")
@allure.story("Recherche par nom")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Recherche Google - Julius KONAN")
@allure.description("Vérifie que la recherche Google retourne des résultats pour Julius KONAN")
def test_google_search(driver):
    with allure.step("Ouvrir Google"):
        driver.get("https://www.google.com")

    wait = WebDriverWait(driver, 10)

    with allure.step("Localiser la barre de recherche"):
        search_box = wait.until(
            EC.presence_of_element_located((By.NAME, "q"))
        )

    time.sleep(2)

    with allure.step("Saisir 'Julius KONAN' et valider"):
        search_box.send_keys("Julius KONAN")
        time.sleep(1)
        search_box.send_keys(Keys.RETURN)

    time.sleep(5)

    with allure.step("Vérifier le titre de la page"):
        assert "Julius KONAN" in driver.title
