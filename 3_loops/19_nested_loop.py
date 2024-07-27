
# below piece of code print table of n 
# n=int(input("Enter the number whose table you want to print: "))
# for i in range(1,11):
#     print(n*i)

# if we want to print table of number from 1 to n then nested loops are required;

# n=int(input("Enter the number whose table you want to print: "))
# for num in range(1,n+1):
#     print("Table of ",num," : ")
#     for i in range(1,11):
#         print(i*num)

n=int(input("enter the number: "))
for i in range(n):
    print()
    for j in range(n):
        print("*",end=" ")