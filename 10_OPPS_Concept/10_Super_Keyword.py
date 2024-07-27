#   The super() keyword in Python is used to refer to the parent class. 
# sometimes you might want to use the parent class method in the child class. This is where the super() keyword comes in handy.

class ParentClass:
    def parentMethod(self):
        print("This is the parent method.")

class ChildClass(ParentClass):
    def ChildMethod(self):
        print("This is the child method .")
        super().parentMethod()
        

childObj = ChildClass()
childObj.ChildMethod()
