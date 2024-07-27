# Syntax
# for x in seq:   //for loops give  every item of iterable or sequence 
#     statement 1
#     statement 2
    
# 'seq' can be list,string,touple,set,range


# LET US FIND SUM OF N NATURAL NUMBER USING LOOP

N=int(input("Enter the range : "))
sum=0
for i in range(1,N+1):
    # print(i,"+",end="")
    # sum=sum+i;
    sum+=i
print(sum)

d={'foo':1,'bar':2,'baz':3}
while len(d)>0:
    print(d.popitem())
    print('done')

x='gfg'
for i in range(x):
     print(i)