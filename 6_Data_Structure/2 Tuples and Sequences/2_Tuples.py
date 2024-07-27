tup = (1,2,3,4,4)

print(tup, "  Type = ",type(tup))

tup1 = (1,)
  
# tup[0]=5   #this will generate an error because tuple ar immutable
 

print(tup.index(2))
print(len(tup))
print(tup.__doc__)
print(tup)


tup = 1,2,3,'harsh'
print(tup,"  Type  = ",type(tup))

tup = ()
print(len(tup))

