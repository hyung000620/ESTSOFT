from bs4 import BeautifulSoup
import requests
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

def makePgNum(num):
    if num == 1:
        return num
    elif num == 0:
        return num + 1
    else:
        return num + 9 * (num - 1)

def makeUrl(search, start_pg, end_pg):
    urls = []
    if start_pg == end_pg:
        start_page = makePgNum(start_pg)
        url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=" + search + "&start=" + str(
            start_page)
        urls.append(url)
        print("생성url: ", urls)
        return urls
    else:
        for i in range(start_pg, end_pg + 1):
            page = makePgNum(i)
            url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=" + search + "&start=" + str(
            page)
        print("생성url: ", urls)
        return urls

def input_start():

    # 사용자 입력
    search = input("검색할 단어?\n")

    page_start = int(input("시작페이지?"))
    print(f"시작할 페이지: {page_start}")

    page_end = int(input("종료페이지?"))
    print(f"종료할 페이지: {page_end}")

    # 네이버 url 생성
    search_urls = makeUrl(search, page_start, page_end)

    driver = webdriver.Chrome()
    driver.implicitly_wait(3)

    naver_urls = []

    for i in search_urls:
        driver.get(i)
        time.sleep(3)

        a = driver.find_elements(By.CSS_SELECTOR, 'a.info')

        for i in a:
            i.click()

            driver.switch_to.window(driver.window_handles[1])
            time.sleep(3)

            url = driver.current_url
            print(url)

            if "news.naver.com" in url:
                naver_urls.append(url)
        
            driver.close()

            driver.switch_to.window(driver.window_handles[0])

if __name__ == "__main__":
    search="나비"
    
    # input_start()
    naver_urls = ['https://sports.news.naver.com/news.nhn?oid=442&aid=0000163350', 'https://n.news.naver.com/mnews/article/001/0014045673?sid=103', 'https://n.news.naver.com/mnews/article/366/0000913600?sid=101', 'https://n.news.naver.com/mnews/article/025/0003290622?sid=102']
    
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"}
    titles = []
    contents = []

    for url in naver_urls:
        orginial_html = requests.get(url,headers = headers)
        html = BeautifulSoup(orginial_html.text, "html.parser")
        # print(html)
        
        title = html.select("div#ct > div.media_end_head.go_trans > div.media_end_head_title > h2")
        title = ''.join(str(title))
        
        pattern1 = r'<[^>]>'
        title = re.sub(pattern=pattern1, repl='', string=title)
        titles.append(title)

        content = html.select("div#dic_area")
        content = ''.join(str(content))
        content = re.sub(pattern=pattern1, repl='', string=content)
        pattern2 = """[\n\n\n\n\n// flash 오류를 우회하기 위한 함수 추가\nfunction _flash_removeCallback() {}"""
        content = content.replace(pattern2,  '')
        contents.append(content)
        
        
print(titles)
print(contents)

news_df = pd.DataFrame({'title':titles, 'link': naver_urls, 'content': contents})
news_df.to_csv(f'NaverNews_{search}.csv', index=False,  encoding='utf-8')