#  class 
# data Attribute
# method



class Person:
    name = "harshit"
    occupation =  "Ai Engineer"
    salary = "10K dollar"

    def showData(self):
        print(f"{self.name} is a {self.occupation} and earns {self.salary}.")


p1  = Person()
print(p1.name)
print(p1.occupation)
print(p1.salary) 

p1.showData()

p2= Person()
p2.name = "Aman"
p2.occupation= "Civil Engineer"
p2.salary = "20k Dollar"
p2.showData()