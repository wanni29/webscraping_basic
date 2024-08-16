from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

# 웹드라이버 설정
options = webdriver.ChromeOptions()
options.headless = True  # 브라우저를 숨김 모드로 실행 (실제 브라우저 창이 나타나지 않음)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 네이버 웹툰 페이지로 이동
url = "https://comic.naver.com/webtoon"
driver.get(url)

# 페이지가 완전히 로드될 때까지 잠시 대기
time.sleep(5)  # 필요에 따라 대기 시간을 조절

# 페이지 소스 가져오기
page_source = driver.page_source

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(page_source, "lxml")

# 원하는 요소 찾기
u_skip_div = soup.find("div", attrs={"class": "u_skip"})
print(u_skip_div)

# 드라이버 종료
driver.quit()