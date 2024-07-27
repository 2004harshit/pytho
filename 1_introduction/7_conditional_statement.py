# find wheather number is odd or even

a=input("enter the number")
a=int(a)
if a%2==0:
    print("even")
else:
    print("odd")

    #find wheather the number is positive ,negative or zero

if a>0:
        print("number is positive")
elif a==0:
        print("numbeer is equal to zero")    
else:
        print("number is negative")

        #using if else condition like a pro
        #below code is 8 line code 
score=90;
if score>90:
      grade="A"
elif score >60:
      grade="B"
else:
      grade="c"
print(grade)

#let us reduce loc
score = 85
grade = "A" if score >90 else "B" if score >60 else "C"
print(grade) # A
