import plus_numbering

def input_file_head():
    base='''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <meta http-equiv="refresh" content="10">
    <title>crawling-site</title>
    <link href="style.css" rel="stylesheet" type="text/css" />
</head>
<body>
    <div class="head_part">
    <a href="index.html">
        <h1 class="head_tag">WEBSITE-NEWS-CRAWLING</h1>
    </a>
    </div>
    '''
    with open("input_value.html","w",encoding="utf8") as files:
        files.write(base)
    with open("input_value_list.txt","w",encoding="utf8") as files:
        files.write("LIST")
        files.write("\n")
        files.write("\n")
    with open("input_value_lists.hwp","w",encoding="utf8") as files:
        files.write("LIST")
        files.write("\n")
        files.write("\n")

i=0 #파일추가시 인덱싱을 위한 변수.

def input_file_value(text_value,link_value,posting_time_value):
    with open("input_value.html","a+",encoding="utf8") as files:
        length = len(text_value)
        files.write("\r")
        files.write('''\t<div class="news_value">''')
        files.write("\r")
        for i in range(length):
            number = plus_numbering.plus()
            files.write("\t\t<a href=\'"+link_value[i]+"\' class=\'"+"news_head"+"\'"+"target=\'_blank\'>"+str(number)+". "+text_value[i]+"</a>")
            files.write('''<div class="time">'''+posting_time_value[i]+'''</div>''')
            files.write("</br></br>")
            files.write("\n")
        files.write('''\t</div>''')

    with open("input_value_list.txt","a+",encoding="utf8") as files:
        length = len(text_value)
        for i in range(length):
            files.write(text_value[i])
            files.write("\n")
            files.write(link_value[i])
            files.write("\n")
            files.write(posting_time_value[i])
            files.write("\n")
            files.write("\n")

    with open("input_value_lists.hwp","a+",encoding="utf8") as files:
        length = len(text_value)
        for i in range(length):
            files.write("\""+text_value[i]+"\"")
            files.write("\n")
            files.write(link_value[i])
            files.write("\n")
            files.write(posting_time_value[i])
            files.write("\n")
            files.write("\n")
        print("page")

#특정파일에 페이지로 부터 가져온 특정 html 정보를 예쁘게 저장시키는 함수
        
def input_file_value_google(text_value,link_value,posting_time_value):
    with open("input_value.html","a+",encoding="utf8") as files:
        length = len(text_value)
        files.write("\r")
        files.write('''\t<div class="news_value">''')
        files.write("\r")
        for i in range(length):
            number = plus_numbering.plus()
            files.write("\t\t<a href=\'"+link_value[i]+"\' class=\'"+"news_head"+"\'"+" target=\'_blank\'>"+str(number)+". "+text_value[i]+"</a>")
            files.write('''<div class="time">'''+posting_time_value[i]+'''</div>''')
            files.write("</br></br>")
            files.write("\n")
        files.write('''\t</div>''')

    with open("input_value_list.txt","a+",encoding="utf8") as files:
        length = len(text_value)
        for i in range(length):
            files.write("\""+text_value[i]+"\"")
            files.write("\n")
            files.write(link_value[i])
            files.write("\n")
            files.write(posting_time_value[i])
            files.write("\n")
            files.write("\n")

    with open("input_value_lists.hwp","a+",encoding="utf8") as files:
        length = len(text_value)
        for i in range(length):
            files.write(text_value[i])
            files.write("\n")
            files.write(link_value[i])
            files.write("\n")
            files.write(posting_time_value[i])
            files.write("\n")
            files.write("\n")
        print("pages")
#다음 페이지에서 가져오는 html 정보를 이미생성되어있는 파일에 이어서 기록하는 함수

def input_file_value_ending():
    end = '''
    <script src="script.js"></script>
</body>
</html>
        '''
    with open("input_value.html","a+",encoding="utf8") as files:
        files.write(end)


        
