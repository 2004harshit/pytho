# PROBLEM    SOME LINES ARE MISMATCHING DUE TO UNORDERLY PLACED\

# POSSIBLE SOLN   COPY THE CONTENT OF FILE INTO TEXT AND CONVERT TEXT FILE INTO PDF 

# EXPLORE THE LIBRARY AND REMOVE THE HEADER AND FOOTER 

from PyPDF2 import PdfReader
import random

reader  = PdfReader("sentence.pdf")
x = random.randint(5,400)
page = reader.pages[x]
print(type(page))
content = page.extract_text()

print(type(content))

# print(content)

# content is str type ,splitting the content 
# list[0] == [question+answer]
list = content.split('\n')
length = len(list)    #length of the list 
# for i in range(2,len(list)) :
#     print(f"{i}  = {list[i]}")
#     newlst = list[i].split("\n")
#     print(newlst)

# for i in list:
#     print(i)

for i in range(2,len(list)):
    print(list[i])
 

# question = []
# answer = []

# for i in range(2,length-1):
# #   splitting each elemetn of list 
#     lst = list[i].split('\n')   #lst = lst[0],lst[1]
#     #lst[0]==question
#     # lst[1]==answer 
#     # storing question and answer into seperate lists
#     question.append( lst[0])
#     answer.append(lst[1])


#     # print(question)
# # print("-"*50)
# # print(answer)

# # question list contain some unnecessary spaces as  values so removing it from the list 
# for item in question:
#     if item == "  ":
#         question.remove(item)


# print(question)



# for ans in answer:
#     print(f"{ans}      :  {type(ans)}")


# # answer list contains unnecessary integer in str format so removing it 
# new_answer = []
# length = len(answer)
# for i in range(0,length):
#     print(i)
#     if i%2!=0:
#        continue
#     new_answer.append(answer[i])

#     # if answer[i]-'0'>0 and answer[i]-'0'<100:
#     #     answer.remove(answer[i])
# print(answer)
# print(new_answer)