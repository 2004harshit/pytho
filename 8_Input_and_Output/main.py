# f = open('intro.txt', 'r')
# print(type(f))
# text = f.read()

# print(text)
# f.close() 


# readline () function

f= open("file.txt",'r')
print(f.readline())
print(f.readline())
print(f.readline())

print("-"*50)
# readlines() function

f = open('workfile.txt', 'r')
print("This will read all the line of file : ")
print(f.readlines())
f.close()

print("-"*50)

# write mode 
f = open("write.txt",'w')
str = input("Enter the string to write in the file : ")
f.write(str)
f.close()


# writelines() method 

f= open("write.txt", 'w')
# dict = {
#     "name ": "Harshit Chauhan",
#     "Roll No":"22ESKCS098",
#     "Branch":"CSE"
# }
list =["hello\n","My name is Harshit Chauhan\n","Currently  I am persuing B Tech in CSE branch\n"]
f.writelines(list)
f.close()

print("-"*50)

# seek(),tell() ,truncte() method


with open('sample.txt','r') as f:
    f.seek(5)
    print(f.tell())
    data = f.read(5)

    print(data)
  
f.close()

f=open("sample.txt",'w')
f.write("hello my name is harshit ")
f.truncate(5)
f.close()