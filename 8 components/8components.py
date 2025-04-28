from selenium import webdriver
from selenium.webdriver.common.by import By

# Start the session
driver = webdriver.Chrome()

# Navigates to the web page
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# Requests the web page's title
title = driver.title

# Implicit wait to make sure the site is loaded before requesting info
driver.implicitly_wait(0.5)

# Find the text input and the submit button
search_form = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

# Enters "Selenium" into the text box. Clicks the search button.
search_form.send_keys("Selenium")
submit_button.click()

# Request 
message = driver.find_element(by=By.ID, value="message")
text = message.text

# Quits the session
driver.quit()