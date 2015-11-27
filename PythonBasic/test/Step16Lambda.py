'''
Created on 2015. 6. 20.

@author: 윤선
'''

def printHi():
    print("hi hi hi")
    
print("type(printHi):", type(printHi))

# printHi 안에 있는 function type id를 a 라는 변수에 복사(대입)
a = printHi

# 밑에는 동일한 함수 객체를 사용하는 것이 된다.
printHi()
a()

def useFunction(test):
    test()

print("useFunction()")
useFunction(printHi)
useFunction(a)

# lambda 함수 : javascript의 익명함수와 같다. function(){}

def getSum(x, y):
    return x + y

print("getSum() ...")
print(getSum(10,20))

print("lambda() ...")
print((lambda x , y : x+y)(10, 20))

# 한줄짜리 이름이 없는 함수 => lambda 함수 (축약함수)
lam = lambda x, y: x*y
print("lambda : ", lam(9, 99))

def useLambda(arg):
    result = arg(10, 1)
    print("result:",result)
    
useLambda(lambda x,y:x-y)

lam2 = lambda arg, *args, **kwargs: print(arg, args, kwargs) # None을 return

result = lam2("하나", "두울", "세엣", num=1, name="김구라")
print("result:", result)

lam3 = lambda x,y : x*y
result2 = lam3(9,9)
print("result:", result2)