#  doc string in python
import math
import pandas

def  printTable(n):
       ''' This function will take a number a  input and print the table of it  ''' #this is doc string
       for i in range(1,11):
              print(f" {n}  *  {i} = {n*i}")


def  PrintTable(n):
       print(n)
       ''' This function will take a number a  input and print the table of it  ''' #this is not a  doc string
       for i in range(1,11):
              print(f" {n}  *  {i} = {n*i}")


# printTable(5)

print(printTable.__doc__)
print(PrintTable.__doc__)



# print(math.__doc__)
# print(pandas.__doc__)
