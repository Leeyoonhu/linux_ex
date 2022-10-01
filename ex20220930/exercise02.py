# 사용자의 표준 입력을 '인상율' 받아 'title' 또는 'description'에서 일치하는 결과를 찾아 출력할 것
# db에서 title이나 description 에 인상율을 포함하는 애들만 뽑아서 출력
from pymongo import MongoClient
import json

client = MongoClient(port=27017)
db = client.bitDB
srcText = input("검색어를 입력하세요 : ")
# inventory = db.inventory.find({"title" : "^인상율"})
inventory = db.inventory.find({'$or' : [
    {'title' : {'$regex' : srcText}}, {'description' : {'$regex' : srcText}}]
})
for inv in inventory:
    print(inv)

