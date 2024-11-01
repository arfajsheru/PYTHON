# Write a python program to calculate the attendance of student. If his/her attendance is <75 % then the student is not allowed to sit in the examination. Read the total number of classes held and attended by the user. Calulte percentage and display allowed to sit or not.
lec_held=int(input("Enter Total number of lecture Conducted: "))
lec_attend=int(input("Enter Total number of lecture attended: "))

attendance = (lec_attend / lec_held) * 100
print("Attendance:-", attendance)
if attendance >= 75:
    print("You are allowed to sit in exam")
else:
    print("You are not allowed to sit in exam")     
