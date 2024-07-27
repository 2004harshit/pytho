#Arithmetic operators
x=9
y=4
print(x+y)  #addition
print(x-y)   #subtraction
print(x*y)   #multiplication
print(x/y)   #division(return float type value)
print(x//y)  #division(return floor(x/y))
print(x%y)  #modulo
print(x**y)  #exponent

#precedence of operator
# 1. + - (left to right)
# 2. *,/,// (left to right)
# 3. **  (right to left)

print(4*9/2+7-6*9//2)
print(4+8-6)
print(2**2**-1)  #evaluated left to right
print((2**1)**-1) #precedence does not matter

