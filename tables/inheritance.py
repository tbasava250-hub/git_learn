class A:
    def __init__(self,i,j) :
        self.i = i
        self.j = j

    def show (self):
        print(f"the  numbers are {self.i}i , {self.j}j")

class B(A) :
    def __init__(self,i,j,k) :
        super().__init__( i , j)
        self.k = k

    def show(self) :
        print(f"the  numbers are {self.i}i , {self.j}j, {self.k}k")

a = A(1,2)
a.show()

b = B(1,5,6)
b.show()


