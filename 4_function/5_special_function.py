
def Intro(name, *args, **kwrgs):
    print(f"My name is {name}.")
    print("My family contains following member : ")
    for member in args:
        print(member ,end=" ")
    print("\n")
    print("My relationship with my members : ")
    for key in kwrgs : 
        print(key,' : ' , kwrgs[key])
        
Intro("Harshit Chauhan"," 'Abhinav','Shashi','Naresh','Tanmay' ",
Me = "Harshit Chauhan",
Father_Name = "Naresh Kumar Chauhan",
Mother_name = "Shashi Chauhan",
Elder_brother = "Abhinav Chauhan",
Younger_Brother = "Tanmay Chauhan",
)
