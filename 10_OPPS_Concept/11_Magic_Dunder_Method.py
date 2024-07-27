from typing import Any


class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    # convert object into string
    def __str__(self) -> str:
        return self.name
    
    # recreate object
    def  __repr__(self):
        return f"Employee('{self.name}')"
    
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i
    
    def __call__(self) :
        print(self.name)
        print(self.age)
        
    
e = Employee("Aman",15)
# print(e.name)

#  print(e)    which method is called 
print(str(e))
print(repr(e))

print(len(e))

# e()      this will generate error e is not callable

e()

# Q implement the method for list 