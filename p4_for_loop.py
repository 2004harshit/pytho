# print("hi how are you")
# print("hi how are you")
# print("hi how are you")
# print("hi how are you")
# print("hi how are you")
# print("hi how are you")
# print("hi how are you")
# print("hi how are you")
# print("hi how are you")
# print("hi how are you ")
# for i in range(10):
 
#  print("hi how are you ")
#  Write a program to print sum of n  numbers;
print("hi!")
print("choose a number:")
n=int(input())
sum=0
for i in range(n+1):
    sum=sum+i
    if( i % 1000000 == 0):  # Print every 1 million iterations
        print("Progress:", i)
print("the sum of number from 0 to",n,"is",sum)


