def in_t_cm (inch):
    centiMeters = 2.54 * inch
    return centiMeters

inch = int(input("Enter the inch: "))
print(in_t_cm(inch))