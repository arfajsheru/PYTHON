def multiplicationTable(number): 
    for i in range(1, 11): 
        print(f"{number} X {11-i} = {number * (11-i)}")



number=int(input("Enter the Multiplication table number: "))        
multiplicationTable(number)