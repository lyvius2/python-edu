'''
    -정규 표현식 사용하기
    1. 대소문자를 구분한다.
    2. 눈에 보이지 않는 기호도 일치해야 한다(tab, line, space)
    3. 어떤문자는 특별한 의미를 가지고 있다.
       ^는 매칭할 문자열의 시작을 의미한다.
       $는 매칭할 문자열의 마지막을 의미한다.
    4. 특별한 의미를 가지고 있는 문자열의 literal 값이 필요하면 역슬래쉬를 사용.('\')
    5. 점은 모든 문자를 의미한다.
    6. [] 대괄호 안에는 매칭될 수 있는 문자의 목록을 넣는다. 목록의 순서는 중요하지 않다.
    7. 문자의 범위는 [-] 문법으로 나타낼 수 있다.
    8. 문자클래스 안에 [^abc] 처럼 첫문자로 ^가 있다면 a,b,c 문자는 각각 매칭하지 않을 문자 목록이 된다.
    9. 문자열을 교차 매칭시키려면 소괄호 안에 | 로 구분해서 문자열을 나열하면 된다. (문자열1|문자열2|문자열3)
    10. 수량자 *, +, ?
        * : 0번 이상 (없어도 되고 여러번 있어도 된다)
        + : 1번 이상
        ? : 없거나 있어도 1번
        [^]+ : 공백을 제외한 모든글자
    11. {}는 정확한 문자의 반복횟수를 정의한다
        {m}은 m번 반복
        {m,n}은 최소 m번, 최대 n번
        {m,}은 최소 m번
    12. * 는 {0,}과 같다
        + 는 {1,}과 같다
        ? 는 {0,1}과 같다
'''
# 검증할 문자열
import re   # 외부 패키지 삽입

myStr = "Hello,World"

# .search("찾을 표현식", 검증할 문자열)
print(bool(re.search("Hello", myStr)))

myStr2 = "who is who"
print(myStr2)
print("^who : ",bool(re.search("^who", myStr2)))
print("who$ : ",bool(re.search("who$", myStr2)))

myStr3 = "$25$ and $50$"
print("\$ : ",bool(re.search(r"\$", myStr3)))
print("find all \$ :",re.findall(r"\$", myStr3)) # list type으로 return

myStr4 = "Regular Expression is Powerful!"
print(myStr4)
print("find all . : ",re.findall(r".", myStr4))
print("find all ...... : ",re.findall(r"......", myStr4))

'''
    ^ $ \ .
'''

myStr5="O.K."
print(myStr5)
print("find all \.",re.findall(r"\.", myStr5))

myStr6="How do you do?"
print(myStr6)
print("find all [dH]. : ",re.findall(r"[dH].", myStr6))

myStr7="abcdefghijklmn0123456789ABCDEFGHIJKLMN!@#$%^&*()"
print(re.findall(r"[a-c5-9]", myStr7))
print(re.findall(r"[a-zA-Z0-9]", myStr7))   # 특수문자를 허용하지 않음
print(re.findall(r"[\w]", myStr7))          # 특수문자를 허용하지 않음
# [a-zA-Z0-9] = [\w] 특수문자를 제외한 모든 문자.
print(re.findall(r"[^a-zA-Z0-9]", myStr7)) #특수문자만 허용
print(re.findall(r"[\W]", myStr7))
print(re.findall(r"[가-힝]", "김구라abcd해골1234#$%^"))

myStr8="Monday Tuesday Friday"
print(re.findall(r"(on|ues|rid)", myStr8))
print(re.findall(r".(on|ues|rid)ay", myStr8)) # ???

# 회원 가입 id를 입력받는다고 가정한다.
# 조건 : 첫글자는 영문자 소문자로 5~10글자 이내로 작성

inputId = input("ID를 입력하세요 : ")
reg1 = r"^[a-z].{4,9}$" # ^ 와 $로 시작과 끝을 명시해놓는게 좋다 
# 정규 표현식과 매칭이 되는 문자열이 있는지 찾아서 결과를 bool type으로 얻어내기
result1 = bool(re.search(reg1, inputId))
if result1:
    print("ID를 제대로 입력했습니다.")
else:
    print("ID를 확인하세요")
    
'''
    회원가입 id를 입력받는다고 가정하자
    조건 : 첫글자는 영문자 소문자, 특수문자 허용하지 않음
           최소5글자 최대10글자
'''
inputId2 = input("ID를 입력하세요(2) : ")
reg2 = r"^[a-z][\w]{4,9}$"
result2 = bool(re.search(reg2, inputId2))
if result2:
    print("ID를 제대로 입력했습니다(2)")
else:
    print("ID를 확인하세요(2)")
    
# 휴대폰 번호 첫자리 검증하는 정규 표현식을 작성해보세요
reg3 = r"^01[016789]$"

# E-Mail 주소를 검증하는 정규 표현식
reg4=r"^([0-9a-zA-Z_-]+)@([0-9a-zA-Z_-]+)(\.[0-9a-zA-Z_-]+){1,2}$"
