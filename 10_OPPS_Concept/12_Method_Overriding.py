class shape:
    def area(self):
        print("Area method of base Class")

    def  createCircle(self, type, radius):
        self.type = type
        self.radius = radius
        
    def printType(self):
     return self.type

class Circle(shape):
    def area(self):
        print(f"Calculating area of {super().printType()} ")

        return 3.14*self.radius*self.radius
    
    


    
C = Circle()
C.createCircle('Circle',5)
print(C.area())