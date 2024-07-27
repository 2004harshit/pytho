class Complex :
    # constructor 
    def __init__ (self, real,img):
        self.real = real
        self.img= img

    def printNumber(self):
        print(f"{self.real} + {self.img}i" )

    # def sum(delf):
        

c1= Complex(1,3)
c2= Complex(7,8)
c1.printNumber()
c2.printNumber()
