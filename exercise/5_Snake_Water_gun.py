import random

# print(dir(random))
# print(random.__doc__)

# num = random.random()

computer_score= []
your_score = []

round = int(input("Enter the number of round :"))

print("Enter -1 for  water,0 for snake and 1 for gun")

while(round):
    choice = int(input("Enter your choice"))
    num = random.randint(-1,1)
    print("computer choose :",num)
    if choice == num:
        your_score.append(0)
        computer_score.append(0)

    elif choice ==-1 and num==0:
        your_score.append(0)
        computer_score.append(1)

    elif choice ==0 and num==-1:
        your_score.append(1)
        computer_score.append(0)

    elif choice ==0 and num==1:
        your_score.append(0)
        computer_score.append(1)

    elif choice ==1 and num==0:
        your_score.append(1)
        computer_score.append(0)


    elif choice ==-1 and num==1:
        your_score.append(0)
        computer_score.append(1)

    else :
        your_score.append(1)
        computer_score.append(0)

    
    round -=1

your_total_score = 0
computer_total_score=0
for i in your_score:
    your_total_score+=i

for j in computer_score:
    computer_total_score+=j


print("----------------------------Score Board----------------------------")
print(f"Your Score              -         {your_total_score}")
print(f"Computer Score     -         {computer_total_score}")
print("-----------------------------Result-----------------------------------")
if your_total_score >computer_total_score:
    print("YOU WON THE MATCH!")
elif your_total_score<computer_total_score:
    print("YOU LOST THE MATCH!")
else:
    print("MATCH TIE :")