'''
Created on 2015. 6. 20.

@author: 윤선
'''
import re
import os

sample = "하나   두울   세엣 네엣    다섯"

result = re.split(r"[\t ]+", sample)

print("result:",result)

if re.search(r"세엣", result[2]):
    print("세엣 이라는 문자열이 존재합니다.")

dong = input("주소를 검색할 동 이름 입력 :")

addrText = open(os.getcwd()+r"\zipcode.txt", encoding="utf-8")

# 내가 만든 코드
'''
addrLines = addrText.readlines()
for i in range(len(addrLines)):
    tmp = addrLines[i]
    addrline = re.split(r"[\t ]+", tmp)
    #print("result:",addrline)
    try:
        if(re.search(dong, addrline[2]) or re.search(dong, addrline[3])):
            print(tmp)
    except Exception as e:
        print(e)
'''

# 예시 코드
while True:
    # 한줄을 읽어들인다
    data = addrText.readline()
    if data=="": # 더 이상 읽을 내용이 없으면
        break # 반목문 빠져나오기
    # 한줄의 정보를 list의 각각 방에 담아서 가지고 온다.
    info = re.split(r"[\t ]+", data)
    if re.search(dong, info[3]):
        print(data)
        
if __name__ == '__main__':
    pass