'''
Created on 2015. 6. 13.

@author: user
'''

# 한줄 주석
"""
    1. 여러줄 주석
    2. 두번째 라인
    3. 세번째 라인
"""
'''
    1. 여러줄 주석
    2. 두번째 라인
    3. 세번째 라인
'''
print(type(1))
print(type(10.1))
print(type("kimgura"))

print(type(1)) # int type
print(type(10.1))# float type
print(type(True)) # bool type
print(type(False)) # bool type
print(type('abcd')) # str type 
print(type("abcd")) # str type
print(type([])) #list type
print(type(["김구라","해골","원숭이"])) #list type
print(type(())) #tuple type
print(type(("하나","두울","세엣"))) #tuple type => list type 의 read only version
print(type({"num":1})) #dict type
print(type({"빨강사탕","초록사탕","노랑사탕"}))#set type
print(type(None)) # None type (빈상태, null 상태)

def myFunction():
    # pass
    print("1. 호랑이를 데려온다.")
    print("2. 냉장고 문을 연다.")
    print("3. 호랑이를 집어 넣는다.")
    print("4. 냉장고 문을 닫는다.")

print("함수를 사용합니다.")
myFunction()
print(type(myFunction))

a = myFunction
print("a 함수를 사용합니다.")
a()