from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# User-agent
# headers = {
#     "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
#     "Accept-Language" : "ko-KR,ko" # 한글로 된 데이터를 요청
#     }

# Setup Chrome options
options = webdriver.ChromeOptions()

# 옵션 추가 - 웹페이지가 자동으로 꺼지지 않도록
options.add_experimental_option("detach", True)

# intialize the browser
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)

# 옵션 추가 - 웹 페이지 최대화
browser.maximize_window()

# 원하는 웹사이트로 이동 
url = "https://www.youtube.com/feed/storefront?bp=EgCSAQMI4gKiBQIoBQ%3D%3D"
browser.get(url)

# 지정한 위치로 스크롤 내리기
# 모니터(해상도) 높이인 1080 위치로 스크롤 내리기 
# browser.execute_script("window.scrollTo(0, 1080)")

# 화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

#  뷰포트 높이 가져오기
# viewport_height = browser.execute_script("return window.innerHeight")

interval = 2 # 2초에 한번씩 스크롤 내림
#  현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.documentElement.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 한번에 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")

    # 스크롤을 화면 크기만큼만 내림
    # browser.execute_script(f"window.scrollBy(0, {viewport_height});")

    # 페이지 로딩 대기
    time.sleep(interval)

    curr_height = browser.execute_script("return document.documentElement.scrollHeight")
    if  curr_height == prev_height:
        break
    
    prev_height = curr_height

print("스크롤 완료")