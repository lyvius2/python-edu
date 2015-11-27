
# test1 이라는 이름의 함수 만들기

def test1():
    pass

test1()

# test2 라는 이름의 함수 만들기
def test2():
    print("test2 라는 함수가 호출됨")
    
print("-----")
test2()

# 함수의 인자를 1개 전달받는 함수
def test3(a):
    print("전달받은 내용:", a)
    
test3("김구라")
test3(9999)
# test3()

# 함수의 인자를 2개 전달받는 함수
def test4(arg1, arg2):
    print("arg1:",arg1)
    print("arg2:",arg2)
    
test4("하나", "두울")

# 함수를 호출하고 나서 함수가 모두 실행된 후 리턴되는 값 확인하기
result1 = test4("세엣", "네엣")
print("result1:", result1)

# 두 수를 전달받아서 합을 리턴해주는 함수
def getSum(num1, num2):
    result = num1 + num2
    return result

getSum(10, 20)
print("result2:",getSum(10, 20))
print(getSum(1, 999))
result2 = getSum(1,1) # 함수호출(사용)
f1 = getSum # 함수 참조 (id 값 불러오기)
print(result2)
print(f1(1000,2000))

# 두 수를 전달받아서 합을 출력해주는 함수
def showSum(num1, num2):
    result = num1+num2
    print("전달받은 두 수의 합:", result)
    
result3 = showSum(5,5)
print("result3:", result3)

# 전달된 인자가 tuple type으로 받아진다.
def test5(*args): # '*' 자동으로 Tuple 버전으로 받음, 레퍼런스 변수 갯수를 동적으로 활용하고자 할 때
    print(args)
    
test5()
test5(10)
test5("김구라")
test5("김구라","해골")
test5(10,20,30,40,50)

# 고정적으로 받아야되는 인자와, 동적으로 받는 인자의 조합
def test6(arg1, *args):
    print("arg1:",arg1)
    print("args:",args)
    
test6("인자1")
test6("김구라", "해골", "원숭이")

def test7(num, name, addr, gender):
    result = "번호:{} 이름:{} 주소:{} 성별:{}".format(num, name, addr, gender)
    print(result)
    
test7(1, "김구라", "노량진", "Male")

# 전달받는 인자의 default값을 지정할 수도 있다.
def test8(num=0):
    print("num:",num)
    
test8()
test8(888)

def test9(num=0, name="이름", addr="주소"):
    result = "번호:{} 이름:{} 주소:{}".format(num, name, addr)
    print(result)
    
test9()
test9(2,"해골","행신동")
test9("행신동","해골",2)
test9(addr="행신동",name="해골",num=2)

def test10(**kwargs):
    print("kwargs:",kwargs) # **kwargs : keyword arguments, dict 타입으로 받는다.
    
test10(addr="행신동", name="해골", num=2)

def test11(num1, *args, **kwargs):
    print(num1)
    print(args)
    print(kwargs)
    
test11(7, "a", "b", "c", 72, addr="방학동", city="서울", num=9)
test11(999)
test11(888, "김구라", "해골", "원숭이", name="주뎅이", addr="봉천동")

