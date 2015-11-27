'''
    -set type
    1. 순서가 없다
    2. 중복을 허용하지 않는다
'''

set1 = {10,20,30,40,50}
print("set1:",set1)
print("len(set1):",len(set1))
set1.add(60)
set1.add(70)
set1.add(70)
set1.add(70)
print("set 1에 원소 추가 후:", set1)

set2 = {60, 70, 80, 90, 100}

# 합집합
resultSet = set1.union(set2) # 합집합
print("set1 U set2:", resultSet)

# 교집합
resultSet2 = set1.intersection(set2)
print("set1 n set2:", resultSet2)

print(set1 | set2) # 합집합
print(set1 & set2) # 교집합
print(set1 - set2) # 차집합

# set 에 list type이나 tuple type에 있는 원소 추가하기
set3={'김구라', '해골'}
list1=['원숭이','주뎅이','덩어리']
tuple1=('해골','주뎅이')

set3.update(list1)
# set3.update(tuple1)
print("list1 병합 후 set3:", set3)

# 값 삭제 (해당 없으면 무시)
set3.discard("해골")
print("해골 삭제 후 set3:", set3)
set3.discard("돼지")

# 값 삭제 : 해당 값이 없으면 예외 발생
# set3.remove("해골")

# 값 모두 삭제
set3.clear()
print("clear() 후 set3:", set3)

print("set1 에 있는 모든 값 출력해보기...")
for item in set1:
    print(item)

# list => set으로 변환
list3 = [10,20,30,40,50,10,10,20,30]

# 중복데이터를 set() 을 이용해서 제거
set4 = set(list3)
print("set4:",set4)

# 다시 list type으로 만들기
list4 = list(set4)

print("list4:",list4)