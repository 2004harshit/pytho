#  Q demonstrate that object is passed  while calling a methos of the class

class Emp:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def printDetail():
        print(f"name = {self.name} and id = {self.id}")
    

E = Emp("harshit",'123')

# E.printDetail()   #TypeError: Emp.printDetail() takes 0 positional arguments but 1 was given -> E is passed as a argument


# Demonstration of instance variable and class variable 
# Instanc Variable -> variable associated with objects
# class variables -> variable associated with class

class Family:
    lastName ="Chauhan"
    No_of_member=0
    def __init__(self, name , age , gender,relation):
        # instance variable
        self.name = name
        self.age = age
        self.gender = gender
        self.relation = relation
        Family.No_of_member+=1
    def printDetail(self):
        print(f"{self.lastName}  family have {self.No_of_member} no of member")
        print(f"Name = {self.name} , Gender = {self.gender} , Age = {self.age} , Relation = {self.relation}")
Me = Family("harshit",20,"Male","Me")

Father = Family("Aman",12,"male","Father")

Brother = Family("Raju",14,'Male',"Brother")

Me.printDetail()
Father.printDetail()