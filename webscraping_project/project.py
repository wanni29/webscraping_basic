import requests
from bs4 import BeautifulSoup

# create_soup 
def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

# scrape_weather
def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8"
    soup = create_soup(url)

    cast = soup.find("p", class_="summary").get_text()

    curr_temp = soup.find("div", class_="temperature_text").get_text().replace("현재 온도", "") # 현재온도
    targets = soup.find_all("li", class_="week_item today")

    min_temp = targets[0].find("span", class_="lowest").get_text() # 최저 온도
    max_temp = targets[0].find("span", class_="highest").get_text() # 최고 온도

    morning_and_afternoon = targets[0].find_all("span", class_="weather_left")

    morning_rain_rate = morning_and_afternoon[0].get_text() #  오전 강수확률
    afternoon_rain_rate = morning_and_afternoon[1].get_text() # 오후 강수확률

    dust_list = soup.find_all("li", class_="item_today")

    pm10 = dust_list[0].get_text() # 미세먼지
    pm25 = dust_list[1].get_text() # 초미세먼지


    # 출력
    print(cast)
    print(f"현재 {curr_temp} ({min_temp} / {max_temp})")
    print(f"강수확률 {morning_rain_rate.strip()} / {afternoon_rain_rate.strip()}")
    print()
    print(f"{pm10.strip()}")
    print(f"{pm25.strip()}")
    print()

# scrape_headline_news
def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com"
    soup = create_soup(url)
    news_list = soup.find_all("div", class_="cjs_journal_wrap _item_contents", limit=3)
    for index, news in enumerate(news_list):
        # title
        title = news.find("div", class_="cjs_t")
        if title:
            title = title.get_text().strip()
        else:
            continue

        # link
        link = news.find("a", class_="cjs_news_a _cds_link _editn_link")["href"]
        if link:
            link = link
        else:
            continue

        # 출력
        print(f"{index+1}. {title}")
        print(f"(링크 : {link})")
        print()

# Setup Logic
if __name__ == "__main__":
    # scrape_weather() # 오늘의 날씨 정보 가져오기
    scrape_headline_news()