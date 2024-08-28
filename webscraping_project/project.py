import requests
from bs4 import BeautifulSoup

'''
[오늘의 날씨]
흐림, 어제보다 00도 높아요
현재 00도 (최저 00도 / 최고 00도)
오전 강수확률 00% / 오후 강수확률 00%

미세먼지 좋음
초미세먼지 좋음
'''

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

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

if __name__ == "__main__":
    scrape_weather() # 오늘의 날씨 정보 가져오기