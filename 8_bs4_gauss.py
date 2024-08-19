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
url = "https://comic.naver.com/webtoon/list?titleId=799793"
driver.get(url)

# 페이지가 완전히 로드 될 때까지 잠시 대기
time.sleep(3)

# 페이지 소스 가져오기
page_source = driver.page_source

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(page_source, "lxml")

# 모든 a 태그를 가져오기 (링크와 타이틀을 함께 포함)
episode_links = soup.find_all("a", class_="EpisodeListList__link--DdClU")

# 각 a태그 에서 제목과 링크를 추출
# strip() : 문자열 접두 / 접미 쪽 공백 제거 

# 만화 제목 + 링크 가져오기
# for episode in episode_links:
#     title = episode.find("span", attrs={"class" : "EpisodeListList__title--lfIzU"}).get_text()
#     link = "https://comic.naver.com" +  episode["href"]
#     print("제목 : {0}, 링크 {1}".format(title, link))

# 평점 정보
total_rates = 0

cartoons = soup.find_all("div", class_="EpisodeListList__meta_info--Cgquz")
for cartoon in cartoons:
    rate = cartoon.find("span", class_="text").get_text()
    print(rate)
    total_rates += float(rate)
print("전체 점수 : ", total_rates)
print("평균 점수 : ", total_rates / len(cartoons))    

# 브라우저 닫기
driver.quit()

# 뷰티풀 수프 한글 문서 제공함 꼭  읽어보고 공부해보기