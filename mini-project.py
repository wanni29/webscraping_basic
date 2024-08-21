# 10_bs4_coupang_pages.py를 이용하여 
# 앞으로 필요한 물건 웹 스크랩핑 해보기
# 웹 스크랩핑 대상 : 모니터 암

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import re 

# 웹 드라이버 설정
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.headless = True
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=options)

for i in range(1, 10):
    print("페이지 정보 : ", i)
    # 쿠팡 모니터 암 타겟팅
    url = f"https://www.coupang.com/np/search?q=%EB%AA%A8%EB%8B%88%ED%84%B0+%EC%95%94&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={i}&rocketAll=false&searchIndexingToken=1=9&backgroundColor="
    driver.get(url)

    # 페이지가 완전히 로드 될 때까지 잠시 대기
    time.sleep(2)

    # 페이지 소스 가져오기
    page_source = driver.page_source

    # BeautifulSoup을 사용하여 HTML 파싱 
    soup = BeautifulSoup(page_source, "lxml")

    items = soup.find_all("li", class_=re.compile("^search-product"))
    for item in items:

        # 광고 제품은 제외시키기
        ad_badge = item.find("span", class_="ad-badge-text")
        if ad_badge:
            continue

        # 제품명
        name = item.find("div", class_="name").get_text()

        # 가격
        price = item.find("em", class_="sale")
        if price:
            price = price.get_text()
        else:
            continue

        # 평점
        rate = item.find("em", class_="rating")
        if rate:
            rate = rate.get_text()
        else:
            continue

        # 리뷰수
        rate_count = item.find("span", class_="rating-total-count")
        if rate_count:
            rate_count = rate_count.get_text()[1:-1]
        else:
            continue

        link = item.find("a", class_="search-product-link")["href"]


        if float(rate) >= 5.0 and int(rate_count) > 2000:
            print(f"제품명 : {name}".strip())
            print(f"가격 : {price}".strip())
            print(f"평점 : {rate}점 / ({rate_count}개)".strip())
            print("바로가기 : {}".format("https://www.coupang.com" + link).strip())
            print("=" * 100)
