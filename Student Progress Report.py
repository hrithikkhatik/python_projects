StudentName = input("Enter Student Name: ")
StudentAge = float(input("Enter Age: "))
ProgrammingLanguage = input("Enter Programming Language They Are Learning: ")
StudyHours = float(input("Number Of Study Hours Per Day: "))
print(f"\nName Is:{StudentName}. Age is:{StudentAge}")
print(f"Programming Language Learning:{ProgrammingLanguage} Number of study hours per day{StudyHours}\n")
Sub1 = float(input("Enter Marks Of Subject1: "))
Sub2 = float(input("Enter Marks Of Subject2: "))
Sub3 = float(input("Enter Marks Of Subject3: "))
TotalMarks = Sub1+Sub2+Sub3
Percentage = TotalMarks / 3
print(f"Total Marks Is:{TotalMarks}")
print(f"Percentage is:{Percentage:.2f}\n")
if Percentage >= 90:
    print("Excellent! Keep it up!")
elif Percentage >= 75:
    print("Very Good! You’re doing great.")
elif Percentage >= 60:
    print("Good job! Keep improving.")
else:
    print("Needs Improvement. Don’t give up!")



