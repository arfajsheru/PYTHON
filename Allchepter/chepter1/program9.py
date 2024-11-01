


average=float(input("Enter Average Percentage obtained by student: "))
if(average >= 75 and average <= 100) :
    print("Your grade is FD")
elif(average >= 60 and average < 75 ) :
    print("Your grade is FC")
elif(average >= 50 and average < 60 ) :
    print("Your grade is SC")       
elif(average >= 40 and average < 50 ) :
    print("Your grade is HS")
elif(average >= 35 and average < 40 ) :
    print("Your grade is PASS")        
elif(average >= 0 and average < 35 ) :
    print("Your grade is FAIL")    
else:
    print("Enter percentage ismore than 100........!!");    