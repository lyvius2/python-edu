"""
    class Coffee 를 정의하세요
    - 맴버함수 : eat() #가상으로 커피를 마시는 함수 print("얌얌") 

    class Starbucks 를 정의하세요
    
    - 맴버필드 : branch   # 지점명(str type)을 생성자에서 받아서 저장하도록
    - 맴버함수 : getBranchName() #지점명을 return 해주는 함수
    - 맴버함수 : showBranchName() #지점명을 콘솔에 출력하는 함수 
    - 맴버함수 : getCoffee() # Coffee type 객체를 리턴해주는 함수
    - 맴버함수 : getCoffees(10) # 인자로 전달한 int 의 수만큼
    Coffee Type 객체를 만들어서 list Type 에 담아서 리턴해주는 함수 
    
    ** Starbucks 객체를 생성해서 모든 함수를 사용해보세요  
     
"""

class Coffee:
    def eat(self):
        print("얌얌")
        
class Starbucks: # class Starbucks(object): 자동으로 object 상속
    branch = None
    def __init__(self, location):
        self.branch = location
    
    def getBranchName(self):
        return self.branch
    
    def showBranchName(self):
        print(self.branch)
        
    def getCoffee(self):
        return Coffee()
    
    def getCoffees(self, num):
        coffeeList = []
        #for i in range(num):
        #    tmp = self.getCoffee()
        #    coffeeList.append(tmp)
        i = 0
        while i < num:
            coffeeList.append(self.getCoffee())
            i += 1
        return coffeeList

starbucks1 = Starbucks("방학동")
resultStr = starbucks1.getBranchName()
print("리턴받은 지점명 :", resultStr)
starbucks1.showBranchName()
resultObj1 = starbucks1.getCoffee()
resultObj1.eat()
eaterList = starbucks1.getCoffees(7)
print("리턴받은 Coffee 객체수 :" , len(eaterList))
#for i in range(len(eaterList)):
#    tmp = eaterList[i]
#    tmp.eat()
    
for tmp in eaterList:
    tmp.eat()