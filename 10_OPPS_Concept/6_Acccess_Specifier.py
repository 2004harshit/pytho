# ther is no access modifier in python

class StudentDetail:
    def __init__(self, name, id, branch):
        self.name = name  #public access specifier
        self.__id = id
        self._branch = branch
    def __fun():
        print("This is private function.")

class Subject(StudentDetail):
    pass

s= StudentDetail("harshit",22045,'cse')
sub= Subject
print(s.name)

# print(s.__id)

s.__fun()     #private function
sub.__fun()   #private remain private 

sub._StudentDetail__fun()   

print(s._branch) 
print(s._StudentDetails_branch) 