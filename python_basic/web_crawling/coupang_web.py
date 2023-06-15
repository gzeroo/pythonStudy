import time
import requests
import re
from bs4 import BeautifulSoup

## 유저가 직접 검색한 것으로 위장하기 위함 // 일부 웹사이트 크롤링 차단
headers = {"User-Agent":""}
## 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'  => 네이버 콘솔창(개발자도구 F12) 에서 navigator.userAgent 입력

for i in range(1,6):
    print("page", i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=9&backgroundColor=".format(i)
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")
    time.sleep(5)

    items = soup.find_all("li", attrs={"class": re.compile("^search-product")})

    for item in items:
        name = item.find("div", attrs={"class":"name"}).get_text()
        price = item.find("strong", attrs={"class":"price-value"}).get_text()
        rate = item.find("em", attrs={"class": "rating"})

        if rate:
            rate = rate.get_text()
        else: # 평점 없으면 계속
            continue
        rate_num = item.find("span", attrs={"class":"rating-total-count"})

        if rate_num:
            rate_num = rate_num.get_text()[1:-1]
        else: # 평점 없으면 계속
            continue

        link = item.find("a", attrs={"class":"search-product-link"})["href"]

        print(f"제품명: {name}")
        print(f"가격: {price}원")
        print(f"평점: {rate}점 ({rate_num}개)")
        print("바로가기: {}".format("http://www.coupang.com"+link))
        print(" ")
        print("-" * 100)