from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # 헤드리스 모드로 실행
options.add_argument("--window-size=1920x1080")  # 브라우저 크기 설정 (헤드리스 모드에서 유용)


# intialize the browser
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)

# 옵션 추가 - 웹 페이지 최대화
# browser.maximize_window()

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
browser.get_screenshot_as_file("google_movie.png")

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("ytd-grid-movie-renderer", class_="style-scope ytd-grid-renderer")

print(f"total_movie_count : {len(movies)}")

for movie in movies:
    # 영화 제목
    title = movie.find("span", class_="style-scope ytd-grid-movie-renderer")
    if title:
        title = title.get_text().strip()
    else:
        continue

    # 징르
    category = movie.find("span", class_="grid-movie-renderer-metadata style-scope ytd-grid-movie-renderer")
    if category:
        category = category.get_text().split(" • ")[0].strip()
    else:
        continue

    # 저장 방식
    buy_or_rental = movie.find("p", class_="style-scope ytd-badge-supported-renderer")
    if buy_or_rental:
        buy_or_rental = buy_or_rental.get_text().strip()
    else:
        continue

    # 링크 정보
    link = movie.find("a", class_="yt-simple-endpoint inline-block style-scope ytd-thumbnail")["href"]
    if link:
        link = "https://www.youtube.com" + link 
    else:
        continue
    
    print("-" * 100)
    print(f"영화 제목 : {title}")
    print(f"저장 방식 : {buy_or_rental}")
    print(f"장르 :  {category}")
    print(f"링크 : {link}")
    print("-" * 100)

browser.quit()

