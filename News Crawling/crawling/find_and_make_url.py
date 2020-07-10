import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import requests
from urllib.request import FancyURLopener

def making_url_naver(search):
    base_url_naver ="https://search.naver.com/search.naver?&where=news&query="
    plus_url_naver = search
    middle_url_naver = "&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=37&start="
    indexing_naver = "1"
    end_url_naver = "&refresh_start=0"
    url = base_url_naver+urllib.parse.quote_plus(plus_url_naver)+middle_url_naver+indexing_naver+end_url_naver
    html = urllib.request.urlopen(url).read()
    soup_naver = BeautifulSoup(html,"html.parser")
    return soup_naver , base_url_naver+urllib.parse.quote_plus(plus_url_naver)+middle_url_naver

def making_url_daum(search):
    base_url_daum = "https://search.daum.net/search?w=news&DA=PGD&enc=utf8&cluster=y&cluster_page=1&q="
    plus_url_daum = search
    middle_url_daum = "&p="
    indexing_daum = "1"
    end_url_daum = ""
    url = base_url_daum+urllib.parse.quote_plus(plus_url_daum)+middle_url_daum+indexing_daum+end_url_daum
    html = requests.get(url).text
    soup_daum = BeautifulSoup(html,'html.parser')
    return soup_daum, base_url_daum+urllib.parse.quote_plus(plus_url_daum)+middle_url_daum
    
def making_url_google(search):
    base_url_google = "https://www.google.co.kr/search?q="
    plus_url_google = search
    middle_url_google = "&source=lnms&tbm=nws&start="
    indexing_google = "0"
    end_url_google = "&sa=X&ved=2ahUKEwifheD8k4vpAhVbL6YKHTg-B4gQ_AUoAnoECA0QBA&biw=1366&bih=635"
    url = base_url_google+urllib.parse.quote_plus(plus_url_google)+middle_url_google+indexing_google+end_url_google
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    }
    html = session.get(url, headers=headers).content

    # class AppURLopener(FancyURLopener):     			 
    #     version = "Mozilla/5.0"

    # a = FancyURLopener().version
    # a = AppURLopener().version

    # html = AppURLopener().open(url)
    # soup_google = BeautifulSoup(html, "html.parser")
    # print(soup_google)

    # html = requests.get(url).text
    soup_google = BeautifulSoup(html,"html.parser")
    return soup_google , base_url_google+urllib.parse.quote_plus(plus_url_google)+middle_url_google

#url을 사용자가 입력한 검색어와 결합해 검색하고, 원하는 사이트에 있는 html정보를 분석하고 이를 url과 함께 반환하는 함수
#page 값도 받아서 필요한 정보의 페이지 값을 받아 url이 이동할수 있도록 조정

# &숫자 가들어가야 페이지가 넘어간다. 네이버의 경우에는 10단위.

