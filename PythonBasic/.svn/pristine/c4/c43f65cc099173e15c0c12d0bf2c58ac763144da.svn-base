'''
Created on 2015. 6. 20.

@author: lee
'''
import re
import os

sample = "하나   두울    세엣 네엣    다섯"

result = re.split(r"[\t ]+", sample)

print("result:",result)

if re.search("세엣", result[2]):
    print("세엣 이라는 문자열이 존재해요")

dong = input("주소를 검색할 동이름 입력:")

#파일 열기 
f = open(os.getcwd()+r"\zipcode.txt", encoding="utf-8")

while True:
    #한줄을 읽어들인다. 
    data = f.readline()
    if data=="": #더이상 읽을 줄이 없다면 
        break # 반복문 빠져 나오기 
    #한줄의 정보를 list 의 각각 방에 담아서 가지고 온다.
    info = re.split(r"[\t ]+", data)
    if re.search(dong, info[3]):
        print(data)

if __name__ == '__main__':
    pass