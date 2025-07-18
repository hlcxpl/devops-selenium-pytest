from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_example_domain():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Puedes usar directamente chromedriver si está en el PATH
    driver = webdriver.Chrome(options=options)
    
    driver.get('https://github.com')

    titleElement = driver.find_element(By.ID,'hero-section-brand-heading')

    assert titleElement.text == 'Build and ship software on a single, collaborative platform'

    driver.quit()