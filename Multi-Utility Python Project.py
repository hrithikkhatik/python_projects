print("1.Student Marks Report")
print("2.Temperature Conversion")
print("3.Simple Interest Calculator")
print("4.Exit")
def Main():
    while True:
        def StudentMarksReport():
            try:
                StudentName = input("Enter Student Name: ")
                Subject1 = float(input("Enter Subject1 Marks: "))
                Subject2 = float(input("Enter Subject2 Marks: "))
                Subject3 = float(input("Enter Subject3 Marks: "))
                TotalMarks = Subject1 + Subject2 + Subject3
                Percentage = TotalMarks / 3
                print(f"Marks in Subject 1: {Subject1}, Marks in Subject 2: {Subject2}, Marks in Subject 3: {Subject3}, Total of Subject: {TotalMarks}, Percentage: {Percentage:.2f}")
                print(StudentName)
                if Percentage >= 90:
                    print("Grade: A+")
                elif Percentage >= 75:
                    print("Grade: A")
                elif Percentage >= 60:
                    print("Grade: B")
                else:
                    print("Grade: C")
            except ValueError:
                print("kindly enter number not alphabet")

        def TemperatureConversion():
            try:
                print("1.Celsius to Fahrenheit")
                print("2.Fahrenheit to Celsius")
                choice = int(input("Enter Choice From 1 to 2: "))
                if choice == 1:
                    Celsius = float(input("Enter Temperature in Celsius"))
                    Fahrenheit = (9 / 5 * Celsius) + 32
                    print(f"Temperature Celsius To Fahrenheit: {Fahrenheit:.2f}")
                elif choice == 2:
                    Fahrenheit = float(input("Enter Temperature In Fahrenheit: "))
                    Celsius = (Fahrenheit - 32) * 5 / 9
                    print(f"Temperature in Celsius: {Celsius:.2f}")
                else:
                    print("Enter number from 1 To 2")
            except ValueError:
                print("kindly enter number not alphabet")

        def SimpleInterest():
            try:
                Principal = float(input("Enter Principal Amount: "))
                Rate = float(input("Enter Rate Of Interest: "))
                Time = float(input("Enter Time In Years: "))
                simpleInterest = (Principal * Rate * Time) / 100
                print(f"Principal : {Principal}, Rate: {Rate}, Time: {Time}, Simple Interest: {simpleInterest:.2f}")
            except ValueError:
                print("kindly enter number not alphabet")

        Choice = int(input("Enter Choice From 1 To 4: "))
        if Choice == 1:
            StudentMarksReport()
        elif Choice == 2:
            TemperatureConversion()
        elif Choice == 3:
            SimpleInterest()
        elif Choice == 4:
            print("You Exit From Program")
            break
        else:
            print("Enter Valid Number")
Main()