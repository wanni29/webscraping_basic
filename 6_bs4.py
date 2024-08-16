'''
import requests
import time
from bs4 import BeautifulSoup
headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}
url = "https://comic.naver.com/webtoon"
res = requests.get(url, headers=headers)
res.raise_for_status()

time.sleep(5)  # 필요에 따라 대기 시간을 조절

soup = BeautifulSoup(res.text, "lxml")

print(res.text)

# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup  객체에서 처음 발견되는 a의 값을 프린트함
# print(soup.a.attrs) # a 태그 안에 있는 객체를 튜플형식으로 프린트함
# print(soup.div["id"]) # div 태그 안의 `id` 값을 가져옴


# print(soup.find(attrs={"class" : "Poster__image--d9XTI"}))
# print(soup.find("li", attrs={"class" : "rank01"}))
print(soup.find("div", attrs={"class" : "u_skip"}))
''' 
# -> 위의 코드로 진행하려고 했지만 requests 라이브러리는 html만 가져오기 때문에
# -> selenium 과 chromedriver를 사용하여 html 과 javascript의 로직을 
# -> 모두 함께 들고 오는 로직으로 기본적으로 갖추어야 할 코드를 수정해서 강의 진행

# -- 여기서 부터 시작입니다 : ) --
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
time.sleep(3) # 필요에 따라 대기 시간을 조절 하기 

# 페이지 소스 가져오기 
page_source = driver.page_source

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(page_source, "lxml")

# ============ 이 까지를 기본 소스코드로 가져가자 ! : ) ========