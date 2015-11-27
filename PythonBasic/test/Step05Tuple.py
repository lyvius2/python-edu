'''
    - tuple
    
    1. list 와 유사
    2. 읽기 전용(수정, 삭제 불가)
'''

tuple1 = ('하나', '두울', '세엣')

print(tuple1[0])
# tuple1[0] = '김구라' # 수정 불가
# tuple1.append('네엣') # 아이템 추가 불가

list1 = list(tuple1) # tuple type을 list type로 변환
print(list1)

result = list1 == tuple1
print(result)

# list type을 tuple type으로 변환해서 얻어내기
tuple2 = tuple(list1)
print(tuple2)

# slice 기능도 가능
print(tuple1[1:2])

tuple3 = '김구라','해골','원숭이'   # tuple type이 만들어지고 해당 객체의 id가 대입됨.
print(tuple3)

# 각각의 변수에 tuple에 있는 데이터를 순서대로 담기
a, b, c = tuple3 # tuple type의 데이터를 각 변수에 담기
print('a:{} b:{} c:{}'.format(a, b, c))

# 아래의 작업을 위에서 편하게 할 수 있다
a2 = tuple3[0]
b2 = tuple3[1]
c2 = tuple3[2]

# 두 변수에 있는 값을 서로 바꾸려면?
first = 'girl'
second = 'boy'
'''
tmp = first
first = second
second = tmp
'''
# 아래와 같이 처리할 수 있다
second, first = first, second
print("first:", first)
print("second:", second)
