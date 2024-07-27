a=input("enter the number")
print(f"Multiplication table of {a} is : " )

try : 
   for i in range(1,11):
        print(f" {int(a)} * {i} = {int(a)*i}")

except :
# except Exception as e:
    print("Invalid Input!")

print("some lines of code")
print("End Of Program")