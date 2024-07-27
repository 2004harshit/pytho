# write a python program which greet you good morning sir good afternoon sir and and good evening use time module

import time



 

hour = int(time.strftime('%H'))
if hour >=0  and hour <12:
    print("Good Morning Sir")
elif hour >=12 and  hour <16 :
    print("Good Afternoon Sir")
else:
    print("Good Evening Sir")
