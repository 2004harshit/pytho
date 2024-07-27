'''''
classmethod(function) -> method

Convert a function to be a class method.

A class method receives the class as implicit first argument, just like an instance method receives the instance. To declare a class method, use this idiom:

  class C:
      @classmethod def f(cls, arg1, arg2, argN):
          ...

It can be called either on the class (e.g. C.f()) or on an instance (e.g. C().f()). The instance is ignored except for its class. If a class method is called for a derived class, the derived class object is passed as the implied first argument.

'''

class Truck:
    companyName = "Tata"

    def show(self):
        print(f"The {self.name} truck belongs to {self.companyName} company")
    
    @classmethod
    def changeCompany(cls ,newName):
        print(cls)
        cls.companyName = newName

T = Truck()
T.name = "Hulk"
T.companyName = "Ashoka" # the companyname is changed for object
print(Truck.companyName)   # class variable remain unchanged
T.show()

T.changeCompany("Ashoka")
print(Truck.companyName)
