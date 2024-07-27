# write a progrm to print all those numbers in a list that are not multiple of 5

list=[]

n=int(input("Enter number of elements present in list: "))

for i in range (0,n):
    num=int(input())
    list.append(num)

print(list)

for item in list:
    if item%5==0:
         continue
    print(item)