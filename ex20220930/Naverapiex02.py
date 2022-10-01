from http import client
import os
from platform import node
from pydoc import describe
import sys
from tracemalloc import start
from urllib import response
import urllib.request
import datetime
import time
import json

# naver client id
client_id = "s3SKlARx4M5gtCyBNSwG"
# naver client secret  
client_secret = "3Td083OqAE"
# 요청 성공, 실패 시 시간을 나타내기 위한 now 선언
now = datetime.datetime.now()


def getRequestUrl(url):
    # 매개변수 url에 보낼 요청 객체 req 생성
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)

    # 요청 객체로 오픈한 url인 객체(서버에서의 응답) response 생성
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            # 응답 코드가 200(정상)일경우
            print("[%s] URL Request Success" %now)
            # 응답 받아온 response를 utf-8로 decoding
            return response.read().decode("utf-8")
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" %(now, url))
        return None

def getNaverSearch(node, srcText, start, display):
    # 네이버 검색 api 검색이 base
    base = "https://openapi.naver.com/v1/search"
    # 네이버 검색 api에서 검색할 대상 노드
    node = "/%s.json" %node
    parameters = "?query=%s&start=%s&display=%s" %(urllib.parse.quote(srcText), start, display)
    url = base + node + parameters
    print ("URL : " + url)
    # 응답 받아온 response를 utf-8로 decoding 한 객체 responseDecode 선언
    responseDecode = getRequestUrl(url)
    if(responseDecode == None):
        return None
    else:
    # JSON 을 python 의 dictionary로 변환하는 함수 .loads()
        return json.loads(responseDecode)

def getPostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']
    pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')
    jsonResult.append({'cnt':cnt, 'title':title, 'description':description, 'org_link':org_link, 'link':link, 'pDate':pDate})
    return
    
def main():
    # 크롤링 대상을 node 변수에 선언
    node = 'news' 
    # 사용자가 입력한 검색어
    srcText = input("검색어를 입력하세요 : ")
    cnt = 0
    # 검색 결과 저장할 list
    jsonResult = []
    jsonResponse = getNaverSearch(node, srcText, 1, 100)
    print("jsonResponse", jsonResponse)
    # 전체 검색 결과 개수
    total = jsonResponse['total']
                                            
    while(jsonResponse != None) and (jsonResponse['display'] != 0):
        # items로 받은 결과마다 cnt 1씩 증가시킴
        for post in jsonResponse['items']:
            cnt = cnt + 1
            getPostData(post, jsonResult, cnt)
        start = jsonResponse['start'] + jsonResponse['display']
        jsonResponse = getNaverSearch(node, srcText, start, 100)
    print("전체 검색 : %d" %total)
    
    

    with open('%s_naver_%s.json' %(srcText, node), 'w', encoding='utf-8') as outFile:
        # dictionary를 json으로 변환하는 함수 .dumps()
        jsonFile = json.dumps(jsonResult, indent=4, sort_keys= True, ensure_ascii=False)
        # File I.O 에서 배웠듯이 outFile에 write
        # 가져온 파일을 writer할것임
        outFile.write(jsonFile)
    
    print("가져온 데이터 : %d건" %(cnt))
    print("%s_naver_%s.json 저장됨" %(srcText, node))

if __name__=='__main__':
    main()

    