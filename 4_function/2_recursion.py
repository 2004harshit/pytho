# def factorial( n):
#          result=1
#          while n>0:
#               result *=n
#               n=n-1
#          return result 

# x=int(input("Enter the value : "))

# ans=factorial(x)
# print(ans)

# def factorial( n):
#   if(n==0 or n==1):
#          return 1
#   else :
#          return n * factorial(n-1)
  
  
# x=int(input("Enter the value : "))

# ans=factorial(x)
# print(ans)

# PRINT FIBONACCI SERIRES

def fibonacci(f1=0,f2=1):
        series =f1+f2
        if(series>100):
                return 0
        print(series)
        
        fibonacci(f2, series)

fibonacci()