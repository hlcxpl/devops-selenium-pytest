import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def test_github_homepage_banner():
    browser = os.getenv("BROWSER", "chrome")

    if browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

    elif browser == "brave":
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)

    elif browser == "safari":
        driver = webdriver.Safari()  # Safari no tiene modo headless

    else:  # Chrome
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)

    element = driver.find_element(By.ID, 'hero-section-brand-heading')
    assert element.text == 'Build and ship software on a single, collaborative platform'

    driver.quit()
