# membership test operator
#  in,not in
# string: checks for substring
#Dictionary: check for key
# List,Set,Tuples: check for membership
s="geeksforgeeks"
print("g" in s)
print("for" in s)
print("gk" in s)
print()

d={10:"abc",20:"efg"}
print(10 in d)
print(30 not in d)
print("efg"  in d)
print()

list=[10,20,"gfg"]
print(10 in list)
print("gfg" in list)
print("abc" not in list)
print([10,20] in list)

string="gfg";
print(not("g"or"")not in  s)

print(oct(23)+oct(23))