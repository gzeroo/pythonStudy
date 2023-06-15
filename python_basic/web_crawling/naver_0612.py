## 웹 크롤리 ## 네이버 쇼핑에서 "빵"을 검색해서 빵 이름만 가져오기

from bs4 import BeautifulSoup
from selenium import webdriver

# selenium 동적 페이지
# BeautifulSoup 정적 페이지

import time

query = input("입력해주세요: ")
url = "https://search.shopping.naver.com/search/all?query={}".format(query)

browser = webdriver.Chrome()
browser.get(url)

# browser.get("https://www.naver.com") ## 링크 사이트 열기

time.sleep(3) ## 창 3초 띄우기

# print(browser.page_source) ## 네이버 웹 소스 오픈(변수.page_source)

soup = BeautifulSoup(browser.page_source, "html.parser") ## BeautifulSoup(지금 접속해 있는 웹사이트의 html 형식, "찾을 텍스트" / html.parser - html에서 특정 찾는 값을 쓸거다)

items = soup.find_all("a", attrs={"adProduct_link__NYTV9 linkAnchor"}) # html 에서 "a" 로 시작하는 태그 찾기 / attrs = 빵의 제목 클래스명을 가져왔음

for item in items:
    print(item.text)



