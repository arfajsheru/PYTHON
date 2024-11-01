'''
1 for snake
-1 for water
0 for gun
'''
import random
computer = random.choice([1, -1, 0])
youstr = input("Enter your choice: ")

youDict = {"s": 1, "w": -1, "g": 0}
reverseDic = {1 : "Snack", -1: "Water", 0 : "gun"}
you = youDict[youstr]
print(f"Your choice is: {reverseDic[you]} \nComputer choice is: {reverseDic[computer]}")

if(computer == you) :
    print("Its a draw")
else :
    # if(computer == -1 and you == 1) :
    #     print("You win!")

    # elif(computer == -1 and you == 0) :
    #     print("You lose!")

    # elif(computer == 1 and you == -1) :
    #     print("You lose!")
    
    # elif(computer == 1 and you == 0) :
    #     print("You win!")

    # elif(computer == 0 and you == -1) :
    #     print("You win!")

    # elif(computer == 0 and you == 1) :
    #     print("You lose!")
    # else :
    #     print("Invalid your choice!")

    if((computer - you == -1) or (computer - you == 2)) :
        print("You lose!")
    else :
        print("You win!")