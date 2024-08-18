from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

# 웹 드라이버 설정
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 네이버 웹툰 페이지로 이동
url = "https://comic.naver.com/webtoon/list?titleId=777767"
driver.get(url)

# 페이지가 완전히 로드 될 때까지 잠시 대기 
time.sleep(3)

# 페이지 소스 가져오기
page_source = driver.page_source

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(page_source, "lxml")

# 모든 a태그를 가져오기(링크와 타이틀을 함께 포함)
cartoons = soup.find_all("a", class_="EpisodeListList__link--DdClU")

# 각 a태그에서 제목과 링크를 추출
# strip() : 문자열 접두 / 접미 쪽 공백을 제거
for cartoon in cartoons:
    title = cartoon.find("span", class_="EpisodeListList__title--lfIzU").get_text()
    link = "https://comic.naver.com" + cartoon["href"]
    print("내가 제일 좋아하는 웹툰 : {0}, 보러가기(클릭): {1}".format(title, link))