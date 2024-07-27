import random

def rollDice(x):
    if x==1:
       return random.randint(1,6)

while 1:
    X=int (input("enter 1for roll dice or 0 for not:"))
    result=rollDice(X)
    print(result) 