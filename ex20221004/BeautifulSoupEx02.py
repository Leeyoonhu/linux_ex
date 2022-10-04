# 정적 웹 페이지 크롤링 실습 [할리스 커피]
# pandas 필요
# urllib 필요

# step 1. 홈페이지에 대한 정보 확인 (가져올 정보 색출)
# step 2. td 정보 가져올 것 (1 : 구정보, 2: 지점 정보, 3: 영업중여부, 4: 주소, 5: 매장 서비스, 6: 전화번호)

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
result = []
encText = urllib.parse.quote('서울')
# 서울인 곳 17페이지 조회
for page in range(1,17):
    Hollys_url = 'https://www.hollys.co.kr/store/korea/korStore.do?pageNo=%d&gugun=&store=&sido=' %(page)
    Hollys_url+=encText
    print(Hollys_url)
    html = urllib.request.urlopen(Hollys_url)
    soupHollys = BeautifulSoup(html, 'html.parser')
    tag_tbody = soupHollys.find('tbody')
    # tr의 길이가 3보다 작거나 같을 때(할리스에서는 6개의 열을 제공하고 있어서 3보다 작을경우는 없는 지점으로 판단) == 색출한 지점 정보가 없을 때 까지
    for store in tag_tbody.find_all('tr'):
        if len(store) <= 3:
            break
        # 지점의 td에 저장된 모든 td값 배열 store_td 선언
        store_td = store.find_all('td')
        # 홈페이지 상의 td 정보 가져올 것 (0 : 구정보, 1: 지점 정보, 2: 영업 중 여부, 3: 주소, 4: 매장 제공 서비스, 5: 전화번호)
        store_name = store_td[1].string # 지점
        store_sido = store_td[0].string # 구
        store_address = store_td[3].string # 주소
        store_phone = store_td[5].string # 전화번호
        result.append([store_name]+[store_sido]+[store_address]+[store_phone])
# 테이블로 재구성
hollys_tbl = pd.DataFrame(result, columns=('store', 'sido-gu', 'address', 'phone'))
# 추려온 값 csv로 작성
hollys_tbl.to_csv('hollys.csv', encoding='utf8', mode='w', index=True)
