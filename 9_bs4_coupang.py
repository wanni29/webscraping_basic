from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import re

# 웹 드라이버 설정
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=options)

# 쿠팡 페이지를 타겟팅 (노트북)
url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken=1=9&backgroundColor="
driver.get(url)

# 페이지가 완전히 로드 될 때까지 잠시 대기 
time.sleep(3)

# 페이지 소스 가져오기
page_source = driver.page_source

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(page_source, "lxml")

items = soup.find_all("li", class_=re.compile("^search-product"))
for item in items:

    # 광고 제품은 제외 
    ad_badge = item.find("span", class_="ad-badge-text")
    if ad_badge:
        # print(" <광고 상품 제외합니다>")
        continue

    name = item.find("div", class_="name").get_text() # 제품명
    # 삼성 제품 제외
    if "삼성" in name:
        # print(" <삼성 상품 제외합니다>")
        continue

    price = item. find("em", class_="sale").get_text() # 가격 

    # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
    rate = item.find("em", class_="rating") #  평점 
    if rate:
        rate = rate.get_text()
    else:
        # print(" <평점 없는 상품 제외합니다>")
        continue

    rate_count = item.find("span", class_="rating-total-count") # 평점수
    if rate_count:
        rate_count = rate_count.get_text()
        rate_count = rate_count[1:-1]
    else:
        # print(" <평점 수 없는 상품 제외합니다>")
        continue

    if float(rate) >= 4.5 and int(rate_count) > 100:
        print(name.strip(), price.strip(), rate.strip(), rate_count.strip())

