    # Print factorial using recursion.
# Recursion: Recursion is when a function calls itself to solve a problem in smaller steps until a base condition is met

def factorial(n) :
    if n == 0 or n == 1 :
        return 1
    else : 
        return n * factorial(n-1)
    
n= int(input("Eneter the factorial number : "))
print(f"The factorial of {n} number is: {factorial(n)}")    