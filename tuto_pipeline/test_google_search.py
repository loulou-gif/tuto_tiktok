import allure
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote_plus


QUERY = "Julius KONAN"


def attach_screenshot(driver, name="screenshot"):
    allure.attach(
        driver.get_screenshot_as_png(),
        name=name,
        attachment_type=allure.attachment_type.PNG,
    )


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
    d = webdriver.Chrome(options=options)
    yield d
    d.quit()


@allure.epic("Moteurs de recherche")
@allure.feature("DuckDuckGo Search")
@allure.story("Recherche par nom")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Recherche DuckDuckGo - Julius KONAN")
@allure.description("Vérifie que DuckDuckGo retourne des résultats pour Julius KONAN")
def test_search(driver):
    wait = WebDriverWait(driver, 15)

    with allure.step(f"Naviguer vers les résultats DuckDuckGo pour '{QUERY}'"):
        driver.get(f"https://duckduckgo.com/?q={quote_plus(QUERY)}&kl=fr-fr")
        attach_screenshot(driver, "page_chargee")

    with allure.step("Attendre les résultats de recherche"):
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='result']")))
        attach_screenshot(driver, "resultats")

    with allure.step("Vérifier que les résultats contiennent la requête"):
        allure.attach(
            f"Titre : {driver.title}\nURL : {driver.current_url}",
            name="page_info",
            attachment_type=allure.attachment_type.TEXT,
        )
        page_source = driver.page_source
        assert "Julius" in page_source or "KONAN" in page_source, (
            f"Aucun résultat trouvé. Titre={driver.title!r}"
        )