class programmer() :
    def __init__(self,name ,salary,pin) :
        self.name = name
        self.salary = salary
        self.pin = pin
    def info(self)  :    
        print(f"programmer name is {self.name} and his salary is {self.salary} and pin code is {self.pin}")


w1 = programmer()
w2 = programmer()
w3 = programmer()

w1.info("basava",120000,584138)
w2.info("mercy",100000,5630036)
w3.info("chandu",122000,538028)