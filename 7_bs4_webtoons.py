from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

# 웹 드라이버 설정
options = webdriver.ChromeOptions()
options.headless = True # 브라우저를 숨김 모드로 실행
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 네이버 웹툰 페이지로 이동
url = "https://comic.naver.com/webtoon"
driver.get(url)

# 페이지가 완전히 로드 될 때까지 잠시 대기
time.sleep(3)

# 페이지 소스 가져오기
page_source = driver.page_source

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(page_source, "lxml")

# 네이버 웹툰 전체 목록 가져오기
cartoons = soup.find_all("span", class_="text")
for cartoon in cartoons:
    print(cartoon.get_text())


