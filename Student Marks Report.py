print("Welcome to Student Marks Report")
StudentName = input("enter student name: ")
MarksOfSubject1 = int(input("enter marks of subject 1: "))
MarksOfSubject2 = int(input("enter marks of subject 2: "))
MarksOfSubject3 = int(input("enter marks of subject 3: "))
TotalMarks = MarksOfSubject1 + MarksOfSubject2 + MarksOfSubject3
Percentage = TotalMarks / 3
print("-------------Report-----Card-------------------\n")
print(f"Student Name: {StudentName}")
print(f"Total Marks: {TotalMarks}")
print(f"Percentage: {Percentage}")
print("Thank you!")
if Percentage >= 90:
    print("Grade: A+")
elif Percentage >= 75:
    print("Grade: A")
elif Percentage >= 60:
    print("Grade: B")
else:
    print("Grade: C")