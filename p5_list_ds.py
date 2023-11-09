# list

shopping=["bread","coffee","sugar"]
# print(shopping)
# for  i in range(3):
#     print(i)

# print element one by one in next line
# for item in shopping:
#     print(item)

#append
#inserting element at the last of list
# shopping.append("Curd")
# print(shopping)



#if i want to print a item of a particular position --
#let us understand indexing
# print(shopping[1])
# print(shopping[0])
# print(shopping[2])

# print item of list as we print element of array in c
# for i in range(3):
#  print(shopping[i])


# traking input in list using ,index mechanism
# product=[]
# for i in range(3):
#     product[i]=input("enter product number i")


#if i want to insert a item of a particular position --
# shopping.append("shampoo")
# shopping.append("curd")



# shopping.insert(1,"oil")
# print(shopping) 


# list having repetations
ages=[12,23,35,55,78,61,23,12,12,36,78,91,5,69,61,35,36,20]

# counting the number of item present in list
# ages.count(25)
# print(ages.count(25))
# print(ages.count(36))

# number of elements present in list
# print(len(ages))



# shorting the list
# ages.sort() #shorting in asending order
# print(ages)

# shorting in desending order
# ages.reverse()
# print(ages)



# CONCEPT OF SLICING
# LET US CONSIDER FOLLOWING LIST OF THE STUDENTS:-

student=["aman","ankit","abhay","anirudh","aditya","abhishek"]
# print(student)

# for item in student:      #printing using for loop
#     print(item)

# for i in range(len(student)):    #using len
#     print(student)

#   syntax    list_name[star_index t:end_index+1]
# Default start index is 0
#Default end index is len(list)

student.sort()
print(student)
print(student[0:3])

