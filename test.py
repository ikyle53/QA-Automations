from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Path to Chrome Browser
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Path to ChromeDriver
chromedriver_path = r"C:\Users\KyleH\ChromeDriver\chromedriver-win64\chromedriver.exe"

# Set up options for Brave
options = Options()
options.binary_location = chrome_path

# Create WebDriver with Brave
driver = webdriver.Chrome(service=Service(chromedriver_path), options=options)

# Test run: visit a website
driver.get("https://www.reddit.com/r/dadjokes/?rdt=59351")
print(driver.title)

time.sleep(3)
driver.quit()