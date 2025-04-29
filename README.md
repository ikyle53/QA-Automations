# QA-Automations

## Setup for Selenium (python)

### Install Selenium

Use pip to install Selenium:
`pip install selenium`

You'll need 2 main components to be able to do anything in Selenium

1. Compatible Browser
2. Compatible WebDriver

The popular choice online is Chrome so I'll go over setting up the WebDriver for Chrome. Your Chrome browser version and Chrome Driver version need to match (example: version 135.0.7049.115). You can visit [GoogleLabs](https://googlechromelabs.github.io/chrome-for-testing/) to get the specific Chrome Driver needed (it's a zip file). **Make sure the Chrome Driver version matches your Chrome Browser's version** Extract your Chrome Driver anywhere on your PC and enter the path to the .exe as the a variable in your program.

Example:
```
chromedriver_path = r"C:\Program Files (x86)\ChromeDriver\chromedriver.exe"
```

Do the same for the Chrome Browser so Selenium can utilize it.

Example: 
```
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
```

Optional: Use WebDriver Manager (no manual download):

`pip install webdriver-manager`

Example code:
```
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManage().install()))
```

`ChromeDriver().install` is going to automatically download the correct ChromeDriver version that matches your installed version of Chrome. It then returns the path to that ChromeDriver executable.

`Service()` creates a Service object using the path to the downloaded ChromeDriver. Selenium then uses it to launch and control the browser process.

`webdriver.Chrome(service=...)` initializes a new Chrome browser instance controlled by Selenium. It passes the Service object into the constructor so it knows which ChromeDriver to use.

Lastly, `driver`- the variable- is going to let us open URL's, interact with elements, run automation tasks, scrape content, etc.

## Selenium Basics

Selenium is made up of 8 main components:
1. Starting the session
2. Taking action on the browser
3. Requesting browser information
4. Establishing a waiting strategy
5. Finding an element
6. Taking an action on the element
7. Requesting element information
8. Ending the session

The common uses cases for Selenium:
- Repetitive tasks
- Web scraping
- Testing

The cool thing is that all the endpoints listed in [W3C](https://w3c.github.io/webdriver/) are supported by Selenium. It also adds a lot of extra capabilities that aren't listed in W3C.