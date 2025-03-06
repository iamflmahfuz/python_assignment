students_name=input("Enter Student's name :")
students_age=int(input("Enter age :"))
students_roll=int(input("Enter Roll :"))
english=int(input("Enter Marks in English:"))
math=int(input("Enter Marks in Math:"))
science=int(input("Enter Marks in Science:"))

total_marks= english+math+science
average=total_marks//3

print("Student Report: ")
print("-----------------------")
print("Name :",students_name)
print("Age :",students_age)
print("Roll Number :",students_roll)
print("Total Marks :",total_marks)
print("Average :",average)