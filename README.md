# QA-Automations

This is my QA testing profile. I'm currently using selenium (python).

### Test.py
Test.py is my first introduction to Selenium where I import the selenium module, create a path for my Chrome browser & Chrome Driver, and open a browser for 3 seconds (using the time module).
If you want to use this file you'll need the following pre-requisites to run it.
1. Chrome browser
2. Chrome Driver

Your Chrome browser version and Chrome Driver version need to match (example: version 135.0.7049.115). You can visit [GoogleLabs](https://googlechromelabs.github.io/chrome-for-testing/) to get the specific Chrome Driver needed (it's a zip file).
Extract your Chrome Driver anywhere on your PC and enter your path as the chromedriver_path variable (line 10).

Example:
```
chromedriver_path = r"C:\Program Files (x86)\ChromeDriver\chromedriver.exe"
```

Do the same for the chrome_path variable as well (line 7).

Example: 
```
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
```

Lastly, you can edit the web page you'd like the program to open by replacing the URL in `driver.get("https://Some_website.com")`
