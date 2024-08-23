from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) # 이 옵션은 창이 닫히지 않도록 설정함

# Initialize the browser
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
browser.get("http://naver.com")