def find_total_page_naver(soup): #검색어와 관련된 게시물수를 페이지로 부터 가져오는 함수
    find_tag = soup.find(class_="title_desc all_my")
    finding = find_tag.string
    blank_index = finding.index(" ")
    total_blank_index = finding.index(" ",blank_index+1)
    last_index = finding.index("건")
    finally_number = finding[total_blank_index+1:last_index]
    del_comma = finally_number.replace(",", "")
    finally_number = int(del_comma)
    return finally_number

def find_total_page_daum(soup):
    find_tag = soup.find("span",class_="txt_info")
    finding = find_tag.string
    blank_index = finding.index(" ")
    total_blank_index = finding.index(" ",blank_index+1)
    last_index = finding.index("건")
    finally_number = finding[total_blank_index+1:last_index]
    del_comma = finally_number.replace(",", "")
    finally_number = del_comma.replace("약","")
    finally_number = finally_number.lstrip()
    finally_number = int(finally_number)
    print(finally_number)
    return finally_number

def find_total_page_google(soup):
    find_tag = soup.find({"id":"result-stats"})
    print(find_tag)
    finding = find_tag.string
    first_index = finding.index("약")
    last_index = finding.index("개")
    collect_number = finding[first_index+2:last_index]
    del_comma = collect_number.replace(",","")
    finally_number = int(del_comma)
    print(finally_number)
    return finally_number








