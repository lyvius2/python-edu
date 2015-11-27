'''
Created on 2015. 6. 20.

@author: 윤선
'''

class Engine():
    # 시동 거는 메서드
    def startUp(self):
        print("부릉부릉")

class Car(object):
    engine = None # Engine type id를 담을 공간
    isStartedEngine = False # 시동을 걸었는지에 대한 여부를 담을 공간
    # 생성자
    def __init__(self, engine):
        self.engine = engine
        
    # 엔진 시작시키는 메서드
    def startEngine(self):
        if self.isStartedEngine:
            self.isStartedEngine = False
            print("시동을 껐습니다.")
        else:
            self.isStartedEngine = True
            self.engine.startUp()
            print("시동을 켰습니다.")
            
    # 달리는 기능
    def drive(self):
        if self.isStartedEngine:
            print("달려요!")
        else:
            print("시동을 먼저 켜주세요!")
            
if __name__ == '__main__':
    e1 = Engine()
    car1 = Car(e1)
    car1.startEngine()
    car1.drive()
    print("-----")
    car1.startEngine()
    car1.drive()