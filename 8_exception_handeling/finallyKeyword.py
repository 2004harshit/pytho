def func1():
        try:
          l=[1,2,3,4,5]
          i= int(input("Enter the index : "))
          print(f"l[{i}] = ",l[i])
          return 0
        except :
            print("Some Error occured !")
            return 1
        finally : 
           print("I am always executed")
        print("I am always executed")

x= func1()
print(f"func1 returns : ",x)