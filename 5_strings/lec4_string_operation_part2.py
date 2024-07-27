# Case changing of a string 
string="harshit CHAUHAN"
string=string.lower()
print(string)
string=string.upper()
print(string)
string=string.title()
print(string)

# startswith() method. used to check wheather a sentence starts with particular string
str="my name is harshit chauhan"
print(str.startswith("is"))
print(str.startswith("m"))
print(str.startswith("my"))
print(str.startswith("my name is"))

# endswith() method,used to check wheather a sentence ends with particular string
print(str.endswith('n'))
print(str.endswith('chauhan'))

# split and join method
print(str.split())
print('-'.join(str.split()))
print(''.join(str.split()))
print("123".join(str.split()))
print(" ".join(str.split()))


# strip(),Istrip(),rstrip()
str="Hello friends , I am learning python HelloH"
print(str.strip('H'))  #delet leading and ending        character provided in argument
print(str.strip('e'))
print(str.strip('H'))
print(str.strip("Hello"))

# print(str.Istrip("e"))
print(str.rstrip("H"))  #ending with H
