cube = [ ]

for i in range(10):
    cube.append(i**3)

print(cube)


# recalling the lambda function

x = lambda a :a**3
print(x(2))
print(x(3))

print("\n")
print("LIST COMPHERENSION TYPE 1 : ")
cube = list(map(lambda x: x**3,range(10)))
print(cube)

print("\n")
print("LIST COMPHERENSION TYPE 2 : ")
cube = [ i**3 for i in range(10)]
print(cube)

print("\n QUESTIONS : ")
# Q two list l1 and 2 are given which contain a number create a new list which contain pair x,y where x belongs to l1 and y belongs to l2 , such tha  x!= y


l2= [1,2,3]
l1= [1,2,3]
comb= [ ]

# ordinary method

# for i in l1:
#     for j in l2:
#         if(i!=j):
#             comb.append((i,j))


# using list compherensions

comb = [ (x,y) for x in l1 for y in l2  if x!=y]


print(comb)


print("\n")
#  Q 2 create a 5*5  2d matrix and  print the vlue  present at i,j position  where i=2*k and j = 3*k

matrix = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
] 

# x=[ [ matrix[i][j] [ i in range (6)] j in range(6) if i%2==0 and j%3==0]]
# print(x)

# new_matrix = [ [row[i] for row in matrix if row%2==0] for i in range(4)  if  i%3==0]
# print(new_matrix)
     
