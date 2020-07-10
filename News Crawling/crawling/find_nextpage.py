import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import find_tag
import inputfile
import requests
import time
import random
from urllib.request import FancyURLopener

def collecting_nextpage(reuse_url_naver,reuse_url_daum,reuse_url_google):
    page = 2
    while True:
        #각각의 url 생성
        rand_value = random.randint(1, 3)
        time.sleep(rand_value)
        url_naver = reuse_url_naver+str(page*10-9)+"&refresh_start=0"
        url_daum = reuse_url_daum+str(page)+""
        url_google = reuse_url_google+str(page*10-10)+"&sa=X&ved=2ahUKEwifheD8k4vpAhVbL6YKHTg-B4gQ_AUoAnoECA0QBA&biw=1366&bih=635"
        #naver html 파일 저장
        rand_value = random.randint(1, 3)
        time.sleep(rand_value)
        html_naver = urllib.request.urlopen(url_naver).read()
        soup_naver = BeautifulSoup(html_naver,"html.parser")
        #daum html 파일 저장
        rand_value = random.randint(1, 3)
        time.sleep(rand_value)
        html_daum = requests.get(url_daum).text
        soup_daum = BeautifulSoup(html_daum,'html.parser')
        #google html 파일 저장
        rand_value = random.randint(1, 5)
        time.sleep(rand_value)
        session = requests.Session()
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
        }
        html = session.get(url_google, headers=headers).content

        # class AppURLopener(FancyURLopener):     			 
        #     version = "Mozilla/5.0"

        # FancyURLopener().version
        # AppURLopener().version

        # html = AppURLopener().open(url_google)
        soup_google = BeautifulSoup(html, "html.parser")
        # html_google = requests.get(url_google).text
        # soup_google = BeautifulSoup(html_google,"html.parser")

        #가져온 html에서 필요한 부분 파싱
        text_value_naver , link_value_naver , posting_time_value_naver = find_tag.find_naver_class_(soup_naver)
        text_value_daum , link_value_daum, posting_time_value_daum = find_tag.find_daum_class_(soup_daum)
        text_value_google , link_value_google , posting_time_value_google = find_tag.find_google_class_(soup_google)

        #반복문을 탈출할 조건을 마련하고, 계속입력을 진행한다.
        if page==400:
            break
        else:
            inputfile.input_file_value(text_value_naver,link_value_naver,posting_time_value_naver)
            inputfile.input_file_value(text_value_daum, link_value_daum ,posting_time_value_daum)
            inputfile.input_file_value_google(text_value_google,link_value_google,posting_time_value_google)
            
        page = page + 1


#다음페이지로 넘어가는 함수.
# url에 &start=?? 를 추가해서 페이지를 넘어가면서 하면된다.