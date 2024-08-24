from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) # 이 옵션은 창이 닫히지 않도록 설정함

# Initialize the browser
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 1. 네이버 이동
browser.get("http://naver.com")

# 2. 네이버 로그인 버튼
elem = browser.find_element(By.CLASS_NAME, "MyView-module__link_login___HpHMW")
elem.click()

# 3. id, pw 입력
browser.find_element(By.ID, "id").send_keys("naver_id")
browser.find_element(By.ID, "pw").send_keys("naver_pwd")

# 4. login 버튼 클릭
browser.find_element(By.ID, "log.login").click()

time.sleep(3)

# 5. id를 새로 입력
browser.find_element(By.ID, "id").clear()
browser.find_element(By.ID, "id").send_keys("my_id")

# 6. HTML 정보 출력
print(browser.page_source) 

# 7. 브라우저 종료
# browser.close() # 현재 탭만 종료
browser.quit() # 브라우저 종료
