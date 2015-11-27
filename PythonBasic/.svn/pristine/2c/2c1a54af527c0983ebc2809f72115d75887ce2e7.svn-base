'''
Created on 2015. 6. 20.

@author: 윤선
'''
# python에서 기본으로 제공해주는 object class 상속받아서 클래스 정의
class Phone(object):
    # 전화거는 기능
    def call(self):
        print("전화를 걸어요")

# 우리가 정의한 Phone 클래스를 상속받아서 클래스 정의하기
class HandPhone(Phone):
    # 이동 중에 전화를 거는 기능
    def mobileCall(self):
        print("이동 중에 전화를 걸어요")
    # 사진을 찍는 기능    
    def takePicture(self):
        print("30만 화소의 사진을 찍어요")
        
# 상속의 개념 : 기능을 확장, 기능에 따라 필요한 기능을 선택적으로 물려받아 사용할 수 있다.
class SmartPhone(HandPhone):
    # 인터넷을 하는 기능
    def doInternet(self):
        print("인터넷을 해요")
    # HandPhone 의 기능 재정의(오버라이딩)
    def takePicture(self):
        print("1000만 화소의 사진을 찍어요")
        
phone1 = Phone()
phone2 = HandPhone()

print("phone1 type:", type(phone1))
print("phone2 type:", type(phone2))

print("phone1 객체의  call() 호출")
phone1.call()
print("phone2 객체의  mobileCall() 호출")
phone2.mobileCall()

phone3 = SmartPhone()
phone3.doInternet()
phone3.takePicture()