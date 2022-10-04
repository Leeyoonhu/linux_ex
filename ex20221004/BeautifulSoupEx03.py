# 동적 웹 페이지 크롤링[커피빈]
# Selenium lib 필요
# Chrome WebDriver 필요

# coffee bean 에서 자세히 보기 버튼의 함수는 <a href="javascript:storePop2('31');void(0);"></a>

from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 빈 배열 result 에게 append해서 담아주는 함수
def CoffeeBean_store(result):
    chrome_options = webdriver.ChromeOptions()
    # 현재 OS에 설치된 크롬 브라우저 사용하도록 수정
    wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options) 
    
    # 매장 수 만큼
    for i in range(1, 50):
        wd.get("https://www.coffeebeankorea.com/store/store.asp")
        # 1초 대기
        time.sleep(1)
        try:
            # 자세히 보기 버튼 함수는 storePop2('숫자'), 
            wd.execute_script("storePop2(%d)"%i)
            # 1초 대기
            time.sleep(1)
            # 자세히 보기 눌렀을때의 화면 html 변수에 저장
            html = wd.page_source
            soupCB = BeautifulSoup(html, 'html.parser')
            # soupCB 
            store_name_h2 = soupCB.select("div.store_txt>h2")
            # h2태그의 0번째가 지점 이름
            store_name = store_name_h2[0].string
            print(store_name)
            store_info = soupCB.select("div.store_txt > table.store_table > tbody > tr > td")
            # store_info의 [0] : 영업시간, [1] : 주차, [2] : 주소, [3] : 전화번호, [4] : 기타정보
            store_address_list = list(store_info[2])
            store_address = store_address_list[0]
            store_phone = store_info[3].string
            result.append([store_name]+[store_address]+[store_phone])
        except:
            continue
    return

# 작성한 CoffeeBean_store(result) 를 통해 매장 위치 가져오기
def main():
    result = []
    print("CoffeeBean 매장 위치 가져오기 >> ")
    # [CODE 1]
    CoffeeBean_store(result) 
    
    CB_tbl = pd.DataFrame(result, columns= ('store', 'address', 'phone'))
    CB_tbl.to_csv('./CoffeeBean.csv', encoding='utf8', mode='w', index=True)

# 메인 함수 실행(실행 시 result 를 테이블 재구성 한 뒤, csv 파일로 저장)
if __name__ == '__main__':
    main()