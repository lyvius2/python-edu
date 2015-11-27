'''
Created on 2015. 6. 20.

@author: 윤선
'''
import os

def divide(a, b):
    return a/b

print("start")
result = None

try :
    result = divide(10, 0)
except ZeroDivisionError as zde:
    print("어떤 수를 0으로 나눌 수는 없습니다! 에러정보 : ", zde)
except TypeError as te:
    print("숫자 Type이 아닙니다. 에러정보 : ", te)
except Exception as e: # 모든 종류의 에러를 catch 한다
    print("알 수 없는 오류입니다. 에러정보 : ", e)
else : # 오류 없을 때 수행되는 블럭
    print("오류 없이 수행되었습니다.")
finally :
    print("오류가 발생하던 안하던 실행이 보장되는 블럭")
    
print("result:", result)

print("end!")


# os 모듈 사용
os.getcwd() # 현재 작업중인 디렉터리
print("현재 작업 중인 디렉터리 : ", os.getcwd())

try:
    # 읽어올 파일의 경로 구성하기
    filePath=os.getcwd()+r"\testFile.txt"
    # 파일 열기
    f = open(filePath, encoding="utf-8")
    print("fileType:", type(f))
    # 텍스트 문서의 내용을 읽어들여서 str type으로 받기
    result = f.read()
    print(result)
    # 파일 닫기
    f.close()
    
    # 파일을 만들어서 문자열 기록하기
    letter = open(os.getcwd()+r"\testFile2.txt",\
                            encoding="utf-8", mode="w") # 쓰기 모드로 열기
    letter.write("To my Friend")
    letter.close() # close() 하는 순간 파일이 만들어진다.
    
    # 'r'은 문자 그대로 봐달라는 뜻.
    # 파일을 열어서 문자열 추가하기
    letter2 = open(os.getcwd()+r"\testFile2.txt",\
                            encoding="utf-8", mode="a") # 추가 모드로 열기
    for i in range(10):
        letter2.write("\n하이")
    letter2.close()
    
    print(".readline() 테스트")
    letter3 = open(os.getcwd()+r"\testFile2.txt", encoding="utf-8")
    #한줄씩 읽어오기 테스트
    print(letter3.readline())
    print(letter3.readline())
    print(letter3.readline())
    letter3.close()
    
    print(".readlines() 테스트")
    letter4 = open(os.getcwd()+r"\testFile2.txt", encoding="utf-8")
    # 한 줄씩 읽어서 각각의 내용을 list type으로 리턴해주는 함수
    lines = letter4.readlines()
    print("lines :" ,lines)
    letter4.close()
    
except Exception as e:
    print(e)


if __name__ == '__main__':
    pass