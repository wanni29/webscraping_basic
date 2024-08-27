# Quiz) 부동산 매물(송파 헬리오시티) 정보를 스크래핑 하는 프로그램을 만드시오

# [조회 조건]
# 1.  http://daum.net 접속
# 2. ` 송파 헬리오시티 ` 검색
# 3.  다음 부동산 부분에 나오는 결과 정보

# [출력 결과]
# ===========  매물 1 ==========
# 거래 : 매매
# 면적 : 84 / 59 (공급 / 전용)
# 가격 : 165,000 (만원)
# 동 : 214동
# 층 : 고 / 23
# ===========  매물 1 ==========
# ...

# [주의 사항]
# - 실습하는 시점에 위 매물이 없다면 다른 곳으로 대체 가능

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

# Setup Chrome options
options = webdriver.ChromeOptions()

# 옵션 추가 - 웹페이지가 자동으로 꺼지지 않도록
options.add_experimental_option("detach", True)
options.add_argument("--user-agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'")

# initialize the browser
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 옵션 추가 - 웹페이지 최대화
browser.maximize_window()

# 원하는 웹사이트로 이동 
url = "https://realty.daum.net/home/apt/danjis/38487"
browser.get(url)

# 데이터 뽑기 시작
soup = BeautifulSoup(browser.page_source, "lxml")

time.sleep(5)
targets = soup.find_all("div", class_="css-1dbjc4n r-1awozwy r-s4x47v r-18u37iz r-17s6mgv r-1m04atk")
print(f"targets_count : {len(targets)}")

for idx, target in enumerate(targets) :

    # 가격과 거래방법
    price = target.find("div", class_="css-1563yu1 r-aw03qq r-1wbh5a2 r-1w6e6rj r-159m18f r-1b43r93 r-b88u0q r-rjixqe r-13hce6t r-1ff274t r-13wfysu r-q42fyq r-1ad0z5i")
    if price:
        plate = price.get_text().split(" ")
        use = plate[0]

        final_price = ''
        for index in range(1, len(plate)):
            final_price += plate[index]
    else: 
        continue
    
    # # 면적
    # area = target.find("div", class_="css-1563yu1 r-1dnsj32 r-1wbh5a2 r-1w6e6rj r-159m18f r-n6v787 r-majxgm r-14yzgew r-fdjqy7 r-13wfysu r-q42fyq r-1ad0z5i")
    # if area:
    #     area = area.get_text().strip()
    # else:
    #     continue

    # # 층수 
    # floor = target.find("div", class_="css-1563yu1 r-1dnsj32 r-1wbh5a2 r-1w6e6rj r-159m18f r-n6v787 r-majxgm r-14yzgew r-fdjqy7 r-13wfysu r-q42fyq r-1ad0z5i")
    # if floor:
    #     floor = floor.get_text().split(" ")[-1].strip()
    # else:
    #     continue

    area_and_floors = target.find_all("div", class_="css-1563yu1 r-1dnsj32 r-1wbh5a2 r-1w6e6rj r-159m18f r-n6v787 r-majxgm r-14yzgew r-fdjqy7 r-13wfysu r-q42fyq r-1ad0z5i")
    area = area_and_floors[0].get_text()
    floor = area_and_floors[1].get_text()[-3:]

    print("=" * 10 + " 매물{0} ".format(idx) + "=" * 10)
    print(f"거래 : {use}")
    print(f"가격 : {final_price}".strip())
    print(f"면적 : {area}".strip())
    print(f"층 : {floor}".strip())
    print()

browser.quit()