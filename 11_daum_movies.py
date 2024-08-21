from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import requests
import re 

# 웹 드라이버 설정
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.headless = True
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=options)

for year in range(2015, 2020):
    url = f"https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q={year}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84"
    driver.get(url)

    time.sleep(2)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "lxml")

    standard = re.compile("https://search1.kakaocdn.net/thumb/R232x328")
    images = soup.find_all("a", class_="thumb_bf")

    for idx, image in enumerate(images):
        target = image.find("img")["src"]

        if standard.match(target):
            print(target)
            # 이미지를 다운로드하려면 requests를 하여야 한다.
            # driver 같은경우는 웹페이지가  자바스크립트로 동적으로 열리는 페이지에서
            # 코드를 가져오지 못하기 때문에 셀러니움과 크롬드라이버를 사용한거구
            # 이미지 다운로드는 처음 말했듯이 requests 라이브러리를 사용하여야한다.
            image_res = requests.get(target)

            with open("movie_{}_{}.jpg".format(year, idx + 1), "wb" ) as f:
                f.write(image_res.content)

            # 상위 5개 이미지까지만 다운로드
            if idx >= 4:
                break