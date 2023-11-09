def fizzbuzz(r):
 for i in range(1,r):
    if((i%3==0)&(i%5==0)):
                print( i,"FizzBuzz", sep='\t')
    else:    
       if(i%3==0):
         print(i,"Fizz",sep='\t')
       else:
           if(i%5==0):
            print(i,"Buzz",sep='\t')
           else:    
             print(i)
            
