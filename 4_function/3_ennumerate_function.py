# enumerate function is a built in function that allows us to loop over a sequence and get the index of each element

list =[1,2,3,4,5,6]
print('index' ,"   ",'value')
for index ,i in  enumerate(list):
    print(index ,"        ",i)
 

fruits =[ 'Apple','Banana','Guvava','Papaya','Oranges']

for ind , fruit in enumerate(fruits):
    print(ind,"   ",fruit)