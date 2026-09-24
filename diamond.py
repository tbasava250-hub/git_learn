class A :
    def dispay(self) :
        print("HI I AM FROM  A")
class B(A) :
    def dispay(self):
        print("HI I AM FROM  B")
class C(A) :
    def display(self) :
        print("HI I AM FROM  C")
class D(B,C) :
    def display(self) :
        print("HI I AM FROM  D")

d1 = D()
d1.display()
print(D.mro())