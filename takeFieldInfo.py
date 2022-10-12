from cmath import isnan
from dataclasses import replace
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time

def Take_Field(result):
    options = webdriver.ChromeOptions()
    options.add_argument('lang=ko_KR')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) 
    
    for i in range(0, 5):
        try:
            driver.get("https://www.iamground.kr/futsal/detail/" + str(i))
            time.sleep(1)
            price1 = 100000
            price2 = 120000
            fName = driver.find_element("id", "infoName").text
            fAddress = driver.find_element("id", "infoAddr").text
            fAddress = fAddress.replace("길찾기", "")
            html = driver.page_source
            bs4 = BeautifulSoup(html, 'html.parser')
            tags = bs4.select("div.col-xs-12>h4")
            capacity = ""
            for tag in tags:
                if(tag.string is not None):
                    if("구장크기" in tag.string):
                        capacity = tag.string
                    if("추천인원" in tag.string):
                        fSize = tag.string
                    if("구장정보" in tag.string):
                        fInfo = tag.string 
            reserve = ""
            try:
                cantReserve = driver.find_element("id", "cannotResv")
                if(cantReserve is not None):
                    reserve = "불가"
            except NoSuchElementException:
                    reserve = "가능"
                            
        except:
            continue
        result.append([fName]+[fAddress]+[capacity]+[fSize]+[fInfo]+[reserve]+[price1]+[price2])
    return    

def main():
    result = []
    print("풋살 구장 위치 가져오기 >> ")
    # [CODE 1]
    Take_Field(result) 
    df = pd.DataFrame(result, columns=('fName','fAddress','capacity','fSize','fInfo','reserve','price1','price2'))
    df.to_csv('./FieldInfo2.csv', encoding='utf8', mode='w', index=False)

if __name__ == '__main__':
    main()