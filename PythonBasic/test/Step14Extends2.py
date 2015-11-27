'''
Created on 2015. 6. 20.

@author: 윤선
'''

print("start!")
# __name__ 의 값을 참고해서 이 모듈이 main thread로 실행되었는지, 다른 모듈에서 import되어 실행되었는지를 알 수 있다.
if __name__ == '__main__':
    print("__main__")
print("end")

class Car(object):
    # 가상의 엔진
    engine = None
    
    # 생성자
    def __init__(self, engine):
        self.engine = engine
    # 멤버 메서드
    def drive(self):
        if self.engine == None:
            print("엔진 객체가 없어서 달릴 수가 없어요!")
        else:
            print("달려요!")
            
class SuperCar(Car):
    # 생성자
    def __init__(self, engine):
        # 부모 생성자에 값 전달하기, 2가지 방법
        # super().__init__(engine)
        Car.__init__(self, engine)
    # 빨리 달리는 기능 추가
    def driveFast(self):
        if self.engine == None:
            print("엔진 객체가 없어서 빨리 달릴 수가 없어요")
        else:
            print("매우 빨리 달려요!")
            
print("Car() 테스트...")
Car(None).drive()
Car("엔진").drive()
print("SuperCar() 테스트...")
# 상속 시 자식 클래스 객체가 생성되기 전에 부모 클래스 객체도 같이 형성된다. 매개변수가 있는 클래스를 상속받을 시에는 자식 클래스에는 부모 클래스의 생성자에 값을 전달하는 생성자가 있어야 한다.
#SuperCar().driveFast() # 오류
SuperCar("엔진").driveFast()