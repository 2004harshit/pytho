# sequence of characeter
# used to store data

# assci value
# A to Z --65 to 90
# a to z -- 97 to 

# PROGRAM 1:

print(ord("a"))
print(ord("b"))
print(chr(97))
print(chr(122))
print(chr(1))

# PROGRAM 2
str1="harshit"  #string are created using both double and single quote
str2='harshit'
print(str1)
print(str2)
#  ACCESSING INFIVIDUAL CHARACTER IN A STRING 
print(str1[0])
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[4])
print(str1[5])
print(str1[6])
# print(str1[7])   string index out of range

# STRING ALSO SUPPORT NEGATIVE INDEXING 
print(str1[-1])
print(str1[-2])
print(str1[-3])
print(str1[-4])
print(str1[-5])
print(str1[-6])
print(str1[-7])

# PROGRAM 3
# strings are immutable
# str[1]="z"
print(str1)

# PROGRAM 4
# Multiline string
# double -single
# triple-double,single
S=""" Hi
My name is Harshit chauhan
I 'a'm learning "python"

 """
print(S)

# PROGRAM 5
# reversing a string
string="harshit chauhan"
print(string[::-1])

#PROGRAM 6
# String Slicing

string1="abcdefghijklmnopqrstuvwyz"
print("string before slicing:", string1)
print(string1[0:5])


# ord function in python
# it returns unicode 
print(ord("a"))
print(ord("b"))
print(ord("A"))
print(ord("A"))
print(ord("*"))


# chr function in python
# convert unicode into string
print(chr(78))
print(chr(45))
print(chr(78))
print(chr(478))
print(chr(200))