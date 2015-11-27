'''
    - list type
    1. 순서가 있다
    2. 여러 type의 데이터를 저장할 수 있다.
    3. 값 변경 가능
'''

a=[1,2,3]
b=[10, True, "문자열"]
c=[10,20,30]
d=a #id값 복사

print("a id:",id(a))
print("b id:",id(b))
print("c id:",id(c))
print("d id:",id(d))

print("a[0]:",a[0]) #a[0] 값 불러오기
a[0] = 999; # a[0] 값 수정하기
print("a : ",a)
print("d : ",d)

family = ['엄마','아빠','나']
print('가족 구성원 목록:', family)
print('가족 구성원 수:', len(family))

# list type에 데이터 추가하기
family.append("남동생")
family.append("여동생")

print("데이터 추가 후 .... ")
print("가족 구성원 목록:", family)
print("가족 구성원 수:", len(family))

# list type에서 데이터 제거
# 값에 의한 삭제
family.remove("남동생")
print("남동생 삭제 후 .... ")
print("가족 구성원 목록:", family)

# 인덱스에 의한 삭제
del family[3]
print("여동생 삭제 후 .... ")
print("가족 구성원 목록:", family)

# 
popedData = family.pop() # pop() 함수의 리턴타입으로 데이터를 가지고 온다.

print("pop() 후 .... ")
print("가족 구성원 목록:", family)
print("popedData:", popedData)

familyHistory = []
familyHistory.append(popedData)
print("familyHistory:", familyHistory)

# dict type에 회원정보를 담아서
mem1={'num':1, 'name':'김구라', 'addr':'노량진'}
mem2={'num':2, 'name':'해골', 'addr':'행신동'}
mem3={'num':3, 'name':'원숭이', 'addr':'상도동'}

print("mem1 의 name 이라는 키값으로 저장된 값 참조...")
print(mem1['name'])

# list type 에 저장하기
members = [mem1, mem2, mem3]

# list type에 저장된 dict type 참조해보기

print(members[0])
print(members[1])
print(members[2])

# members의 1번 방에 있는 dict type에 addr이라는 키값으로 저장된
# 값 참조해보기
dic1 = members[1]
result = dic1['addr']
print('result:', result)

result2 = members[1]['addr']
print('result2:', result2)

# 특정방을 참조해서 대입연산자를 이용해서 값 수정하기
members[0]['name'] = '개구라'
print('개구라 수정후:', members)

print('개구라 수정후:', mem1)

numbers=[]
numbers.append(10)
numbers.append(40)
numbers.append(50)
numbers.append(20)
numbers.append(30)

print('numbers:',numbers)

# 오름차순 정렬
numbers.sort()

print("정렬 후....")
print(numbers)

# 내림차순 정렬
numbers.sort(reverse=True)

print("numbers 내림차순 정렬 후...")
print(numbers)

# slice 연습
numbers2 = [1,2,3,4,5,6,7,8,9,10]

print(numbers2[0:2]) # 0번 이상 2번 미만
print(numbers2)
print(numbers2[-5:-1])

examData1 = {'num':1, 'name':'김구라', 'eng':100, 'math':80}
examData2 = {'num':2, 'name':'해골', 'eng':90, 'math':70}
examData3 = {'num':3, 'name':'원숭이', 'eng':80, 'math':100}

resultList = [examData1, examData2, examData3]

print(type(range(10)))
# 반복문
for i in range(10):
    print(i)
    
for i in range(len(resultList)):
    print(i)
    
'''
    - 다음과 같이 출력해보세요
    
    번호:1 이름:김구라 영어:xx 수학:xx
    번호:2 이름:해골 영어:xx 수학:xx
    번호:3 이름:원숭이 영어:xx 수학:xx
'''
    
for i in range(len(resultList)):
    print("번호:{} 이름:{} 영어:{} 수학:{}".format(resultList[i]['num'],resultList[i]['name'],resultList[i]['eng'],resultList[i]['math']))
    
for i in range(len(resultList)):
    # i번째 회원정보를 담고 있는 dict객체를 얻어온다.
    tmp = resultList[i]
    result = "번호:{} 이름:{} 영어:{} 수학:{}"\
    .format(tmp['num'],tmp['name'],tmp['eng'],tmp['math'])
    print(result)
    
for a in [10,20,30]:
    print(a)
    
for item in resultList:
    result = "번호:{} 이름:{} 영어:{} 수학:{}"\
    .format(item['num'],item['name'],item['eng'],item['math'])
    print(result)