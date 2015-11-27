'''
    - dict type
    
    1. key:value 형태로 데이터를 저장한다.
    2. 순서가 없는 데이터이다.
    3. key 값을 이용해서 저장된 값을 참조할 수 있다.
'''

dict1={"num1":1, "name":"김구라", "addr":"노량진", "isMan":True}

# 데이터 참조
print(dict1["name"])
print(dict1["addr"])

dict1["name"] = "개구라"
print("수정 후 dict1:",dict1)

# 특정방 삭제
del dict1["addr"]
print("addr 삭제 후 dict1:",dict1)

# 모든방 삭제
dict1.clear()
print("clear() 후 dict1:",dict1)

dict2 = {"car":"자동차", "house":"집", "phone":"전화기"}

print("keys : ", dict2.keys())
print("values : ", dict2.values())

print("dict2 의 key 값 추출...")
for key in dict2.keys():
    print(key)
    
print("dict2 의 value 값 추출...")
for value in dict2.values():
    print(value)
    
print("dict2 의 key 값을 추출해서 원하는 작업하기...")
for key in dict2.keys():
    # key 값을 이용해서 dict type에서 value 값을 읽어온다.
    tmp = dict2[key]
    # 원하는 작업을 한다...
    print("key:{}, value:{}".format(key, value))
    