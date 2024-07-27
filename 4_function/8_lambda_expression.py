#  Small anonymous functions can be created with the lambda keyword. This function returns the sum of its two arguments: lambda a, b: a+b.

# Lambda expressions are often used in situations where a small, simple function is needed, such as in sorting or filtering operations, or when passing a function as an argument to another function. They are particularly useful in functional programming paradigms.


add = lambda x,y,z: x+y+z
print(add(1,2,3)) 


pairs = [('Harshit','Chauhan'),('Abhinav','Chauhan'),('Shashi','Chauhan')]

pairs.sort(key = lambda pair:pair[1])
print(pairs)







