# import string 
# import random 
# A=string.ascii_letters
# n = int(input())
# for i in range (n):
#   l=[]
#   for j in range(n):
#          l.append(random.choice(A))
#   for element in l:
#           print(element , end  =('\t'))
#   print()

# import string
# import random

# A = string.ascii_letters
# n = int(input("Enter the value of n: "))

# for i in range(n):
#     l = []
#     for j in range(n):
#         l.append(random.choice(A))
#     for element in l:
#         print(element, end='\t')  # Use '\t' for tab character
#     print()

# import random

# l = []
# for i in range(10):
#     l.append(random.randint(0, 10))

# l.sort()
# l.reverse()

# print(l)
for i in range(101):
      flag=0
      for j in range(2,i):
             if(i%j==0):
                    flag=1
                    break
      if(flag==0):
              print(i) 