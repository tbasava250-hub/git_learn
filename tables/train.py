from random import randint 

class train :
    def __init__(self,trainno) :
        self.trainno = trainno

    def bookticket(self,fro,to) :
        print(f"train tickcet booked which has number : {self.trainno} from {fro} to {to}")

    def getstatus(self) :
        print(f"train with number : {self.trainno} is running on time")

    def getfare(self,fro,to) :
        print(f"ticket is fare in train number : {self.trainno} from {fro} to {to} is {randint(222,555)}")

t = train(54)

t.bookticket("sindhanur" , "bengaluru")
t.getstatus()
t.getfare("sindhanur" , "bengaluru")