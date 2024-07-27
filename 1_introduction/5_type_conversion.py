# type conversion in python are divided into two parts 
# 1. Implicit type conversion             
#2.  Explicit type conversion

# Example1(Implicit type conversion)

a=10  #integer
b=1.5 #integer
c=a+b#float (implicit conversion into float)
print(c)

x=True 
y=1
z=x+y  #(x=1),x is converted into integer
print(z)

#Exqample (explicit type conversion)
s="10"
x=1
z=int(s)+1  #s is converted into integer
print(z)

string="harshit"
print(list(string))
print(tuple(string))
print(set(string))
# print(dict(string))

num=20
num1=10
print(bin(num)+bin(num1))  #integer->binary
print(oct(num))  #integer->octal
print(hex(num)) #integer->hexadecimal

binary="10100"
print(int(binary,2)) #binary->integer
octal="24"             
print(int(octal,8))    #octal->integer
hexa="14"
print(int(hexa,16))  #hexadecimal->integer




