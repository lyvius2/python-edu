'''
    1. 문자열을 입력받아서 입력한 문자열이 "man"이면
       "남자입니다"를 출력하고 "woman"이면
       "여자입니다"를 출력하고 그 이외의 문자열이면
       "잘못된 형식입니다"를 출력하도록 해보세요.
       
    2. 정수값 점수를 입력받아서 성적을 출력해보세요
       90 이상 => "수입니다."
       80 이상 => "우입니다."
       70 이상 => "미입니다."
       60 이상 => "양입니다."
       60 미만 => "가입니다."
'''
inputData = input("문자열을 입력하세요 : ")

if inputData == "man":
    print("남자입니다.")
elif inputData == "woman":
    print("여자입니다.")
else:
    print("잘못된 형식입니다.")
    
inputData2 = int(input("점수를 입력하세요 : "))

if inputData2 >= 90:
    print("수입니다.")
elif 90 > inputData2 >= 80:
    print("우입니다.")
elif 80 > inputData2 >= 70:
    print("미입니다.")
elif 70 > inputData2 >= 60:
    print("양입니다.")
else:
    print("가입니다.")
    
result=None
if inputData2 >= 90:
    result="수"
elif 90 > inputData2 >= 80:
    result="우"
elif 80 > inputData2 >= 70:
    result="미"
elif 70 > inputData2 >= 60:
    result="양"
else:
    result="가"
print("성적 결과는 {} 입니다.".format(result))