import json

# JSON 형식의 데이터:
x = '{"name" : "코난", "age" : 10, "address" : "미란이네"}'

# JSON 을 python 의 dictionary로 변환하는 함수 .loads()
y = json.loads(x)

# y의 key가 address인 값 출력
print(y["address"]) 

# y의 현재 타입 확인
print(y, type(y)) 

# dictionary 객체 x2 선언
x2 = {
    "name" : "장미",
    "age" : 18,
    "address" : "브라운 박사네"
}

# dictionary를 json으로 변환하는 함수 .dumps()
# 인코딩 참고 ==> https://daewoonginfo.blogspot.com/2019/04/python-json.html
# json 파일 내에 읽을 수 있는 형태로 문자열을 그대로 저장하고 싶다면 ensure_ascii=False를 주어야 함.
# indent='\t'를 주지 않으면 json 모듈이 값을 일렬로 출력
y2 = json.dumps(x2, ensure_ascii= False)

# the result is a JSON string
print(y2, type(y2))