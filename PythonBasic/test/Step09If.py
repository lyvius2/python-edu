'''
    -if 문 사용하기
    
    1. 조건부로 어떠한 작업을 수행하고자 할 때 사용한다.
    2. 들여쓰기로 특정 블럭을 구성한다.
'''

# 단일 if 문(특정 블럭을 조건부로 수행하고자 할 때)

if True:
    print("출력될까요?")
    print("하나")
    print("두울")
    
if False:
    print("2 출력될까요?")
    print("2 하나")
    print("2 두울")
'''
inputData = input("문자입력:")
print("inputData:",inputData)
print("inputData type:", type(inputData))
'''
# 사용자가 입력한 str type을 int type으로 바꿔서 얻어오기
inputNum = int(input("숫자입력:"))

if inputNum>0:
    print("{} 은 양수입니다.".format(inputNum))
    
if inputNum<0:
    print("{} 은 음수입니다.".format(inputNum))
    
if inputNum==0:
    print("{} 은 zero입니다.".format(inputNum))
    
print("if else 문을 이용해서 구성하기")

name = "개구라"

if name == "김구라":
    print("이름은 김구라 입니다.")
else:
    print("이름이 김구라가 아닙니다.")
    
num = 99

# % => 나머지값을 얻어내는 연산자
if num%2 == 0:
    print("num은 짝수입니다.")
else:
    print("num은 홀수입니다.")
    
print("-- 다중 id문 사용 --")

if inputNum>0:
    print("{} 은 양수입니다.".format(inputNum))
elif inputNum<0:
    print("{} 은 음수입니다.".format(inputNum))
#elif inputNum==0:
#    print("{} 은 zero 입니다.".format(inputNum))
else: # 다중 if문에서 마지막에 else: 블럭은 디폴트 수행블럭의 의미...
    print("{} 은 zero 입니다.".format(inputNum))
    
# 3항 연산
isMan = True
result = "남자입니다." if isMan else "여자입니다." # if와 else 사이의 결과가 True이면 남자입니다, False이면 여자입니다 출력
print("result:",result)

result2=None
if isMan:
    result2="남자입니다."
else:
    result2="여자입니다."
    
print("result2:",result2)

# 참고
result3=("여자입니다","남자입니다")[isMan]
print("result3:",result3)