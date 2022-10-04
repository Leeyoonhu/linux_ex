# API가 아닌 크롤링을 통해 페이지의 정보를 가져오기
# 할리스는 정적인 방법으로 (현재 페이지에 있는 정보를 크롤링)
# 커피빈은 동적인 방법으로 (store에서 자세히 보기 클릭 시의 정보를 크롤링)
from bs4 import BeautifulSoup
html='<div class="service_area"><a id="NM_set_home_btn" href="https://help.naver.com/support/welcomePage/guide.help" class="link_set" data-clk="top.mkhome">네이버를 시작페이지로</a><i class="sa_bar"></i><a href="https://jr.naver.com" class="link_jrnaver" data-clk="top.jrnaver"><i class="ico_jrnaver"></i><span class="blind">쥬니어네이버</span></a><a href="https://happybean.naver.com" class="link_happybin" data-clk="top.happybean"><i class="ico_happybin"></i><span class="blind">해피빈</span></a></div>'
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify()) #HTML 문서를 모두 출력

# 태그 parsing 하기
print('text only : ', soup.get_text()) # tag를 제외한 text만 출력
print('i : ', soup.i) # i 태그 내용

# 속성을 이용하여 parsing
# attrs : 속성 이름, 속성 값으로 dictionary 구성
# find() : 속성을 이용하여 특정 태그 parsing
# select() : 지정한 태그를 모두 parsing하여 list 구성 (태그#id 속성값 / 태그.class 속성값)

# i 태그 중에서, 클래스가 sa_bar 인놈 find()
print('attr : ', soup.find('i', attrs={'class':'sa_bar'}))

# id가 NM_set_home_btn 인 놈 find()
print('find() : ', soup.find(id="NM_set_home_btn"))

# div태그의 자식인 a의 자식인 i태그 선택
print('select() : ', soup.select("div>a>i")) 