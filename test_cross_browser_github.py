import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_github_homepage_banner():
    browser = os.getenv("BROWSER", "chrome")

    if browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

    elif browser == "brave":
        options = ChromeOptions()
        options.binary_location = "/usr/bin/brave-browser" 
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)

    elif browser == "safari":
        driver = webdriver.Safari() 

    else: 
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)

    driver.get('https://github.com')

    try:
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.presence_of_element_located((By.ID, 'hero-section-brand-heading')))
        assert element.text == 'Build and ship software on a single, collaborative platform'
    finally:
        driver.quit()
