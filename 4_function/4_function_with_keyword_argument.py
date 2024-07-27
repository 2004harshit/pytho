def studentDetail(Name='NA', RollNo='NA', branch='NA'):
    print('Name = ', Name)
    print('Roll No = ', RollNo)
    print('Branch = ', branch)


print("Function calling wihtout arguments : ")
studentDetail()

print(" "*50)
print("Function calling with positional arguments :")
studentDetail('Harshit', '22ESKCS098', 'CSE')

print(" "*50)
print("Function calling with keyword arguments : ")
studentDetail(RollNo='22ESKCS098', branch='CSE', Name='Harshit')

print(" "*50)
# keyword arguments must follow positional arguments.
print("Function calling with keyword  and positional arguments : ")
studentDetail('Harshit', branch='cse', RollNo='22ESKCS098')
