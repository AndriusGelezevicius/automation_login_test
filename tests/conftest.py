import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    # driver = webdriver.Chrome(...) Paleidžia Chrome naršyklę per Selenium WebDriver.
    # ChromeDriverManager().install() automatiškai pasirūpina, kad būtų naudojama tinkama chromedriver versija.
    # Service(...) naudojama naujoje Selenium API kaip paleidimo mechanizmas.
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    yield driver

    driver.quit()