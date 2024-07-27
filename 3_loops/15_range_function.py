
# Range function generates integer number from 0 to n-1

r=range(5)  #range function return an object not a list
print(r)
l=list(r)  #we construct a list by providing a range type object
print(l)

# let us ,find type of r varible
print(type(r))

# we can generate number by providing two parameter in range function
# let us find the output

R=range(15,45) #this will generate number between 15 to 44
L=list(R)
print(L)

# THink what happen if we pass three parameter in range ffunction

n=range(1,10,2)   #this will print number t to 10 and the difference of two consecutive numbers are 2 ,the third paramater mybe positive or negative
li=list(n)
print(li)