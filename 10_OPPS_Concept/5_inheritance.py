class Employee:
    def __init__(self,name,id,phone):
        self.name =name
        self.id = id 
        self.phone = phone

class Programmer (Employee):
    def printDetail(self):
        print(f"Name : {self.name}")
        print(f"Id : {self.id}")
        print(f"Phone : {self.phone}")

P1 = Programmer("Harshit",123,'9549468215')
P1.printDetail()