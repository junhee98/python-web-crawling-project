def find_naver_class_(soup): #특정페이지의 제목들과 링크를 가져오는 함수
    title = soup.find_all("a",class_="_sp_each_title")
    posting_time = soup.find_all("dd",class_="txt_inline")
    title_text_naver = []
    title_link_naver = []
    posting_time_text_naver = []
    for i in title:
        title_text_naver.append(i.attrs['title'])
        title_link_naver.append(i.attrs['href'])
    
    for i in posting_time: 
        posting_time_text_naver.append(i.text)
    
    return title_text_naver , title_link_naver , posting_time_text_naver

def find_daum_class_(soup):
    title = soup.find_all("a",class_="f_link_b")
    posting_time = soup.find_all("span",class_="f_nb date")
    title_text_daum = []
    title_link_daum = []
    posting_time_text_daum = []
    for i in title:
        title_text_daum.append(i.text)
        title_link_daum.append(i.attrs['href'])

    for i in posting_time:
        posting_time_text_daum.append(i.text)

    return title_text_daum, title_link_daum , posting_time_text_daum

def find_google_class_(soup):
    title = soup.find_all("a",class_="l lLrAF")
    posting_time = soup.find_all("div",class_="dhIWPd")
    title_text_google = []
    title_link_google = []
    posting_time_text_google = []
    for i in title:
        title_text_google.append(i.text)
        title_link_google.append(i.attrs['href'])

    for i in posting_time:
        posting_time_text_google.append(i.text)
    return title_text_google, title_link_google, posting_time_text_google
        

