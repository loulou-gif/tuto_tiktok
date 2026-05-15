from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()

options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)

driver.maximize_window()

driver.get("https://www.google.com")

wait = WebDriverWait(driver, 10)

search_box = wait.until(
    EC.presence_of_element_located((By.NAME, "q"))
)

time.sleep(2)

search_box.send_keys("Julius KONAN")

time.sleep(1)

search_box.send_keys(Keys.RETURN)

time.sleep(5)

assert "Julius KONAN" in driver.title

driver.quit()