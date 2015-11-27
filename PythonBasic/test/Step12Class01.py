'''
    - 객체를 생성하기 위한 설계도 : class 정의하기
'''

# Car 클래스 정의하기
class Car:
    # 멤버 필드 (속성, 저장소)
    name = "소나타"
    
    # 멤버 메서드(함수)
    def drive(self):
        print("달려요!")
    
    def drive2(self):
        print(self.name, "이(가) 달려요!")
# Car 클래스를 이용해서 객체를 생성한 후 if값 얻어내기

car1 = Car() # Car 클래스의 생성자를 호출해서 객체 생성
car2 = Car()
# 기능 사용하기 (멤버 함수 호출하기)
car1.drive()
car2.drive()
# 저장소(속성) 참조하기
print("car1.name :", car1.name)
print("car2.name :", car2.name)

print("car1 type: ",type(car1))
print("car2 type: ",type(car2))

# 객체의 id값 비교하기
print("car1 == car2 :", car1 == car2)

# python 객체의 개념을 이해하기.
car3 = car2
car2.name = "프리우스"
print("car.name 수정 후...")
print("car1.name ", car1.name)
print("car2.name ", car2.name)
print("car3.name ", car3.name)

print("car1, car2, car3 의 drive2() 호출...")
car1.drive2()
car2.drive2()
car3.drive2()