# '"in" operator  
# check character or substring present in string

string="Geeks For geeks"
s1="Geeks"
s2="For"
s3="geeks"
print(s1 in string)
print(s2 in string)
print(s3 in string)

string="Geeks"
s4="geeks"
print(s4 in string)

# string concatenation using + operator
string1="harshit"
string2="chauhan"
string3=string1+string2
print(string3)
string1=string1+string2
print(string1)

# index() method
string="swami keshwanand institute of technology"
print(string.index('swami'))   #retun the index from which target begins
print(string.index('wami'))
print(string.index('ogy'))
print(string.index('d'))
print(string.index(' '))

print(string.index(' ',6))  #searching starts from given index
print(string.index('s',1))

# rindex() method
string="harshit chauhan harshit chauhan harshit chauhan"
print(string.rindex('harshit'))
print(string.rindex('chauhan'))
print(string.rindex('harshit',0,15))
print(string.rindex('chauhan',0,15))
print(string.rindex('harshit',0,-15))
print(string.rindex('chauhan',0,-15))