

def fintGrestesNumber(num1, num2, num3): 
    if(num1 > num2 and num1 > num3) :
        print(f"The {num1} is gretest of all this numbers {num2}, {num3}")
    elif(num2 > num1 and num2 > num3) :
        print(f"The {num2} is gretest fo all this numbers {num1}, {num3}")
    else :
        print(f"The {num3} is gretest of all this numbers {num2}, {num1}")


num1 = int(input(f"Enter the number: "))
num2 = int(input(f"Enter the number: "))
num3 = int(input(f"Enter the number: "))

fintGrestesNumber(num1, num2, num3)
