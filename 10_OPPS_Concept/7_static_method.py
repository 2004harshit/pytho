class String:
    def __init__(self,str):
        self.str = str
    
    def printString(self):
        print(self.str)

    @staticmethod
    def staticMethod():
        print("this is static method : ")

S= String('harshit')
S.printString()
# S.staticMethod()
String.staticMethod()
