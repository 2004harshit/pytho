def cube(x):
    return x*x*x
l= [ 1,2,3,4,4,1,2,3,5,6,7,8]

square =lambda x:x*x
# cubeList = []
# for item in l:
  
#     cubeList.append(cube(item))
# print(cubeList)

newlist =list( map(cube,l))
print(newlist)

squarelist = list(map(square,l))
print(squarelist)

newlist = ['a','b','c','d','e','f','g','h','i','j']

filterFun = lambda char: char if (char =='a'or char=='e' or char =='i' or char =='o' or char =='u') else ''

lis= list(filter(filterFun,newlist))
print(lis)


from functools import reduce
num = [1,2,3,4,5,6]

sum = reduce(lambda x,y: x+y,num)
print(sum)

