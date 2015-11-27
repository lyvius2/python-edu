class Car:
    # 멤버필드(속성, 저장소) 정의하기
    company=None #제조사
    name=None #이름
    color=None #색상
    
    # 생성자정의(객체를 생성할때 호출되는 부분) * java: public void main(String[] args)...
    #def __init__(self):
    #    print("__init__()")
    def __init__(self, company, name, color): # 객체 생성시 레퍼런스 변수 설정.
        print("__init__()")
        self.company = company
        self.name = name
        self.color = color
    # 멤버 메서드 정의
    def showInfo(self):
        print("제조사:{}, 이름:{}, 색상:{}"\
              .format(self.company, self.name, self.color))
    
car1 = Car("TOYOTA","PRIUS","SILVER")
print("car1 의 제조사:{}, 이름:{}, 색상:{}".format(car1.company, car1.name, car1.color))

car2 = Car("SUZUKI","WAGON R","ZET BLACK")
print("car2 의 제조사:{}, 이름:{}, 색상:{}"\
      .format(car2.company, car2.name, car2.color))

car1.showInfo()
car2.showInfo()