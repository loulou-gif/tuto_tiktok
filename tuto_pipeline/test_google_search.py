import allure
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
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
@allure.feature("Google Search")
@allure.story("Recherche par nom")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Recherche Google - Julius KONAN")
@allure.description("Vérifie que la recherche Google retourne des résultats pour Julius KONAN")
def test_google_search(driver):
    with allure.step(f"Naviguer directement vers les résultats pour '{QUERY}'"):
        url = f"https://www.google.com/search?q={quote_plus(QUERY)}&hl=fr"
        driver.get(url)
        attach_screenshot(driver, "page_chargee")

    with allure.step("Accepter les cookies si la bannière est présente"):
        try:
            accept_btn = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,
                    "//button[.//span[contains(text(),'Tout accepter')"
                    " or contains(text(),'Accept all')"
                    " or contains(text(),'Accepter tout')]]"
                ))
            )
            accept_btn.click()
            attach_screenshot(driver, "apres_cookies")
        except TimeoutException:
            pass

    with allure.step("Vérifier que la page contient des résultats"):
        attach_screenshot(driver, "resultats_recherche")
        page_source = driver.page_source
        allure.attach(
            f"Titre: {driver.title}\nURL: {driver.current_url}",
            name="page_info",
            attachment_type=allure.attachment_type.TEXT,
        )
        assert "Julius" in page_source or "KONAN" in page_source, (
            f"Aucun résultat trouvé. Titre={driver.title!r}  URL={driver.current_url!r}"
        )