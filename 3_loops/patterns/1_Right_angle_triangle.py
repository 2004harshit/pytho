# THIS WILL PRINT * IN RIGHT ANGLED FORMAT
row=int(input("Enter the number of row present in the triangle: "))
col=int(input("enter the number of column present in the triangle"))
for i in range(1,row+1):
    for j in range(1,i):
        print("*",end=" ")
    print()        

    # THIS WILL  PRINT COUNTING IN RIGHT ANGLED FORMAT
for i in range(1,row+1):
    for j in range(1,i):
        print(j,end=" ")
    print()


for i in range(1,row+1):
    for j in range(1,i):
        print(i-1,end=" ")
    print()