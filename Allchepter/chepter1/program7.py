# A compnay decided to five a bonus of 10% to the empolyee if his/her year service is more than 5 yeas. Ask the user for their basic salary and year of service and print the net bonus amount
salary=float(input("Please enter your Salary: "))

service_yrs=int(input("Please etner your Years of service: "))


if(service_yrs > 5) : 
    print("Your Salary (+Bonus) =", salary  + (salary) * 10 / 100 )
else: 
    print("You rae not eligible for bouns as your have less service years.")    