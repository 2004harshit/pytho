def printString( str= "No string is passed in argument."):
    print(str)
print("Function calling without any argument : ")

printString()

print("-"*50)

print("Function calling with argument : ")

printString("HELLO")

print(" "*50)
print(" "*50)


print('CASE 1 : ')
def insert_Into_List(a=0, l=[100]):
    l.append(a)
    print('list l = ',l)

print("Passing parameter : ")
insert_Into_List(5,[5])
print('-'*50)

print('passing no arguments : ')
insert_Into_List()


print(' '*50)
print(' '*50)

print("CASE 2  :")
def insert_Into_ist(a=0, l=[]):
    l.append(a)
    print('list l = ',l)
print('list is shared across different function calling : ')
insert_Into_ist(1)
insert_Into_ist(2)

print(" "*50)
print(" "*50)


print("CASE 3  :")
def insertInto_ist(a=0, l =  None):
    if l is None:
        l = []
    l.append(a)
    print('list l = ',l)
print('different list is created during  different function calling : ')
insertInto_ist(1)
insertInto_ist(2)