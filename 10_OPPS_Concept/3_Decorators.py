# def temp():
#     pass

# class Temp:
#     pass
 

# decaorator function
# takes function as argument and return a function

def greet(fun):
    def new_fun():
        print("Good Morning")
        fun()
        print("Thank you for using me.")
    return new_fun
   
   
@greet
def hello():
    print("Hello.")

hello() 
def decorate_add(fun):
    def new_fun(*args, **kwargs):
        print("Welccome to decorate__add decorator function")
        fun(*args,**kwargs)
        print("Thank you for using..")
    return new_fun

@decorate_add
def add(a,b):
    print(a+b)

add( 1,2)