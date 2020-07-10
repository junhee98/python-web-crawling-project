import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import find_and_make_url
import find_tag
import finding_total
import inputfile
import find_nextpage
import time
import random





search = input("please input your search word: ") #사용자로부터 검색어를 입력받는다.

soups_naver , reuse_url_naver = find_and_make_url.making_url_naver(search) #  search 값을 받아 원하는 url을 생성하고 원하는 url에 있는 html 정보를 soups에 반환, 다음페이지로 넘어가는데 활용할 url정보를 reuse_url에 반환
rand_value = random.randint(1, 3)
time.sleep(rand_value)
soups_daum , reuse_url_daum = find_and_make_url.making_url_daum(search)  
rand_value = random.randint(1, 3)
time.sleep(rand_value)
soups_google , reuse_url_google = find_and_make_url.making_url_google(search)


# max_index_naver = finding_total.find_total_page_naver(soups_naver) # url정보는 soups에서 받아 페이지에서 총 게시물수를 가져와서 max_index로 반환하는 함수. 

# max_index_daum = finding_total.find_total_page_daum(soups_daum)

# max_index_google = finding_total.find_total_page_google(soups_google)


text_value_naver , link_value_naver , posting_time_value_naver = find_tag.find_naver_class_(soups_naver) # url에서 가져온 html 정보중 원하는 텍스트 정보와 그에 걸려있는 링크정보를 각각 text_value 와 link_value에 리스트형태로 반환하는 함수.

text_value_daum , link_value_daum, posting_time_value_daum = find_tag.find_daum_class_(soups_daum)

text_value_google , link_value_google , posting_time_value_google = find_tag.find_google_class_(soups_google)



inputfile.input_file_head() #페이지 만드는데 필요한 헤더파일작성



inputfile.input_file_value(text_value_naver,link_value_naver,posting_time_value_naver) # 가져온 텍스트 값과 링크 값들을 파일에 저장시키는 함수.

inputfile.input_file_value(text_value_daum, link_value_daum ,posting_time_value_daum)

inputfile.input_file_value_google(text_value_google,link_value_google,posting_time_value_google)


find_nextpage.collecting_nextpage(reuse_url_naver,reuse_url_daum,reuse_url_google)

inputfile.input_file_value_ending() #모든 크롤링을 마치고 페이지를 닫는 순서
 




















