import allure
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():

    options = Options()

    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")

    d = webdriver.Chrome(options=options)

    yield d

    d.quit()


@allure.epic("Moteurs de recherche")
@allure.feature("Google Search")
@allure.story("Recherche par nom")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Recherche Google - Julius KONAN")
@allure.description("Vérifie que la recherche Google retourne des résultats pour Julius KONAN")

def test_google_search(driver):

    wait = WebDriverWait(driver, 10)

    with allure.step("Ouvrir Google"):
        driver.get("https://www.google.com")

    with allure.step("Localiser la barre de recherche"):
        search_box = wait.until(
            EC.presence_of_element_located((By.NAME, "q"))
        )

    with allure.step("Saisir Julius KONAN et valider"):
        search_box.send_keys("Julius KONAN")
        search_box.send_keys(Keys.RETURN)

    with allure.step("Vérifier le titre"):
        wait.until(
            EC.title_contains("Julius KONAN")
        )

        assert "Julius KONAN" in driver.title