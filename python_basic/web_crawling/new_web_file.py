import time
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.by import By ## 클릭한 거 뭐로 조회할건지, By

browser = webdriver.Chrome()
browser.get("https://www.coupang.com/")
time.sleep(3) ## 사이트 오픈 기다리기_페이지 소스 받아올 때 까지 기다리는거_

## browser.implicitly_wait(time_to_wait=5) ## 사이트 오픈 기다리기(페이지 소스 받아올 때 까지 기다리는거_"로딩이 되면 바로 넘어감"!! time.sleep이랑 다름!)

browser.find_element(By.XPATH, "/html/body/div[3]/div/header/section/div[1]/div/form/fieldset/div/label/input").click() ## 브라우저에서 XPATH 가져오기
browser.find_element(By.XPATH, "/html/body/div[3]/div/header/section/div[1]/div/form/fieldset/div/label/input").send_keys("노트북")

browser.find_element(By.XPATH, "/html/body/div[3]/div/header/section/div[1]/div/form/fieldset/a").click()
time.sleep(3)


