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
url = "https://comic.naver.com/index"
driver.get(url)

# 페이지가 완전히 로드 될 때까지 잠시 대기
time.sleep(0.01)

# 페이지 소스 가져오기
page_source = driver.page_source

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(page_source, "lxml")


# 기본기 
rank1 = soup.find("li", attrs={"class" : "AsideList__item--i30ly"})
rank1_text = rank1.find("span", class_="text").get_text()
print(rank1_text)

# next_sibling / previous_sibling 사용해보기
print("rank1.next_sibling : {}".format(rank1.next_sibling))

print("rank1.previous_sibling : {}".format(rank1.previous_sibling))


# 응용 - 클래스 이름은 같지만두번째 클래스부터 진행

# 모든 해당요소 들고오기
all_items = soup.find_all("ul", attrs={"class" : "AsideList__content_list--FXDvm"})

# 두 번째 요소를 선택 
second_item = all_items[1]

# ul 아래에 있는 li의 값을 추출 
target_rank1 = second_item.find("li", attrs={"class" : "AsideList__item--i30ly"})

# 텍스트 값 도출

# 랭킹 1위는 뽑아내고 이후는 포문 
target_rank1_text = target_rank1.find("span", class_="text").get_text()
print("랭킹 1위 : {0}".format(target_rank1_text))

target_rank_all = target_rank1.find_next_siblings("li")

rank_num = 2

for rank in target_rank_all:
    print("랭킹 {0}위 : {1}".format(rank_num, rank.find("span", class_="text").get_text()))
    rank_num += 1