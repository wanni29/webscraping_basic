from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome options
options = webdriver.ChromeOptions()
# 이 옵션은 창이 닫히지 않도록 설정하는 옵션
options.add_experimental_option("detach", True)

# initialize the browser
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

# 창 최대화
browser.maximize_window()

# 네이버 항공권 이동
browser.get("https://flight.naver.com/")

# 가는 날 선택 클릭
browser.find_element(By.XPATH, "//button[contains(@class, 'tabContent_option___mYJO') and contains(@class, 'select_Date__Potbp')]").click()

# 이번달 27일, 28일 선택
# browser.find_elements(By.XPATH, "//b[text()='27']")[0].click() # [0] -> 이번달
# browser.find_elements(By.XPATH, "//b[text()='28']")[0].click() # [0] -> 이번달

# 다음달 27일, 28일 선택
# browser.find_elements(By.XPATH, "//b[text()='27']")[1].click() # [1] -> 다음달
# browser.find_elements(By.XPATH, "//b[text()='28']")[1].click() # [1] -> 다음달

# 이번달 27일, 다음달 28일 선택
browser.find_elements(By.XPATH, "//b[text()='27']")[0].click() # [0] -> 다음달
browser.find_elements(By.XPATH, "//b[text()='28']")[1].click() # [1] -> 이번달

# 제주도 선택하기
browser.find_element(By.CLASS_NAME, "end").click()
time.sleep(1.5)
browser.find_element(By.XPATH, "//button[text()='국내']").click()
time.sleep(1.5)
browser.find_element(By.XPATH, "//i[text()='제주']").click()

# 항공권 선택
browser.find_element(By.CLASS_NAME, "searchBox_search__dgK4Z").click()

# 어떠한 엘리먼트가 나올때까지 기달려줘 라는 의미 (최대 10초까지 기달림)
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[4]/div/div[2]/div[2]")))
    # 성공했을 때 이후 동작 수행
    print(elem.text)
finally:
    browser.quit()
