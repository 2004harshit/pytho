print("Let us learn about costum errors : ")


'''
a= (input("enter a number between 0 - 9 : "))


if(a<'0' or a>'9'):
    raise ValueError("value should be between 0 - 9")
'''


str= input("enter any string  :")

if(str =="quit"):
    print(str)
else :
    raise ValueError("invalid string .")