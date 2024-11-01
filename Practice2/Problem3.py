number = int(input("Enter the number: "))

is_prime = True  # Assume the number is prime initially

if number < 2:  # Check for numbers less than 2
    is_prime = False  # Numbers less than 2 are not prime
else:
    for i in range(2, int(number**0.5) + 1):  # Check up to the square root of the number
        if (number % i) == 0:
            is_prime = False  # Found a divisor, not a prime
            break

if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
