def printPattern (n): 
    if n == 0:
        return
    print("*" * n)
    return printPattern(n-1) 



n=int(input("Enter the number: "))
printPattern(n)