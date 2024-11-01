
def c_t_f (celsius) :
    fahrenheit = celsius * (9/5) + 32
    return fahrenheit

celsius = int(input("Enter the celsius value: "))
print(f"clesius to fahrenheit: {c_t_f(celsius)}°C")

