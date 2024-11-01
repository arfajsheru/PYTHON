def nuaturalNumber (number):
    if(number == 0):
        return 0
    elif(number == 1):
        return 1
    return number + nuaturalNumber(number - 1)


number = int(input("Enter the number: "))    
print(f"1 to {number} nuatural number sum : {nuaturalNumber(number)}")