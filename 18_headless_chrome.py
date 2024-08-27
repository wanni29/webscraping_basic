from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome options - headless version
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=1920x1080")
options.add_argument("--user-agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'")

# intialize the browser
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 원하는 웹사이트로 이동
url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
browser.get(url)

detected_value = browser.find_element(By.ID, "detected_value")
print(detected_value.text)

browser.quit()