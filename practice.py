from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--user-agent=''")

# Initialize the browser
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 옵션 추가 - 웹페이지 최대화
browser.maximize_window()

# 원하는 웹사이트로 이동 
url = "https://realty.daum.net/home/apt/danjis/38487"
browser.get(url)

# 모든 요소가 로드될 때까지 대기 (최대 10초)
WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "css-1dbjc4n")))

# 데이터 뽑기 시작
soup = BeautifulSoup(browser.page_source, "lxml")

# 매물 정보 가져오기
targets = soup.find_all("div", class_="css-1dbjc4n r-1awozwy r-s4x47v r-18u37iz r-17s6mgv r-1m04atk")

for idx, target in enumerate(targets):
    # 가격과 거래 방법 추출
    price = target.find("div", class_="css-1563yu1 r-aw03qq r-1wbh5a2 r-1w6e6rj r-159m18f r-1b43r93 r-b88u0q r-rjixqe r-13hce6t r-1ff274t r-13wfysu r-q42fyq r-1ad0z5i")
    if price:
        plate = price.get_text().split(" ")
        use = plate[0]

        final_price = ''
        for index in range(1, len(plate)):
            final_price += plate[index]
    else: 
        continue
    
    # 면적과 층수 정보 추출
    area_and_floors = target.find_all("div", class_="css-1563yu1 r-1dnsj32 r-1wbh5a2 r-1w6e6rj r-159m18f r-n6v787 r-majxgm r-14yzgew r-fdjqy7 r-13wfysu r-q42fyq r-1ad0z5i")
    if len(area_and_floors) >= 2:
        area = area_and_floors[0].get_text()
        floor = area_and_floors[1].get_text()[-3:]
    else:
        area = "N/A"
        floor = "N/A"

    print("=" * 10 + " 매물 {0} ".format(idx) + "=" * 10)
    print(f"거래 : {use}")
    print(f"가격 : {final_price}".strip())
    print(f"면적 : {area}".strip())
    print(f"층 : {floor}".strip())
    print()

browser.quit()