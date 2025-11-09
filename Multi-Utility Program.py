def Main():
    while True:
        print("""
        ==============================
             🧮 Multi-Utility Tool
        ==============================
        1. Student Marks Report
        2. Temperature Conversion
        3. Simple Interest Calculator
        4. Math Operations
        5. Exit
        ==============================
        """)

        def StudentMarksReport():
            try:
                StudentName = input("Enter Student Name: ")
                MarksOfSubject1 = int(input("Enter Marks Of Subject1: "))
                MarksOfSubject2 = int(input("Enter Marks Of Subject2: "))
                MarksOfSubject3 = int(input("Enter Marks Of Subject3: "))
                TotalMarks = MarksOfSubject1 + MarksOfSubject2 + MarksOfSubject3
                Percentage = TotalMarks / 3
                print(f"Student Name Is:{StudentName}")
                print(f"Marks Of Subject1,Subject2,Subject3 Is {MarksOfSubject1},{MarksOfSubject2},{MarksOfSubject3}")
                print(f"Total Marks Is:{TotalMarks},Percentage Is:{Percentage}")
                if Percentage >= 90:
                    print("Grade Is:A+")
                elif Percentage >= 75:
                    print("Grade Is:A")
                elif Percentage >= 60:
                    print("Grade Is:B")
                else:
                    print("Grade Is:C")
            except ValueError:
                print("❌ Kindly enter numeric values.")

        def TemperatureConversion():
            print("""
            1.Celsius to Fahrenheit
            2.Fahrenheit to Celsius
            """)
            try:
                Choice = int(input("Enter Choice From 1 to 2: "))

                def CelsiusToFahrenheit():
                    Celsius = float(input("Enter Temperature In Celsius: "))
                    Fahrenheit = (9 / 5 * Celsius) + 32
                    print(f"Temperature From Celsius To Fahrenheit:{Fahrenheit}")

                def FahrenheitToCelsius():
                    Fahrenheit = float(input("Enter Temperature In Fahrenheit: "))
                    Celsius = (Fahrenheit - 32) * 5 / 9
                    print(f"Temperature From Fahrenheit To Celsius:{Celsius}")

                if Choice == 1:
                    CelsiusToFahrenheit()
                elif Choice == 2:
                    FahrenheitToCelsius()
                else:
                    print("❌ Invalid choice! Please select between 1 to 2.")

            except ValueError:
                print("❌ Kindly enter numeric values.")

        def SimpleInterestCalculator():
            try:
                Principal = float(input("Enter Principal Amount: "))
                RateOfInterest = float(input("Enter Rate Of Interest: "))
                TimeInYears = float(input("Enter Time In Years: "))
                SimpleInterest = (Principal * RateOfInterest * TimeInYears) / 100
                print(f"Principal Amount Is:{Principal}")
                print(f"Rate Of Interest Is:{RateOfInterest}")
                print(f"Time In Years:{TimeInYears}")
                print(f"Simple Interest Is:{SimpleInterest}")
            except ValueError:
                print("❌ Kindly enter numeric values.")

        def MathOperations():
            try:
                Numbers = input("Multiple numbers (space-separated): ").split()
                nums = []
                for i in Numbers:
                    num = int(i)
                    nums.append(num)
                print(f"Maximum Numbers:{max(nums)},Minimum Numbers:{min(nums)}")
                Number = int(input("A single number for absolute value: "))
                print(f"Absolute Value Is:{Number}")
                Base = int(input("Base for power calculation: "))
                Exponent = int(input("exponent for power calculation: "))
                print(f"Power Result Base ^ Exponent:{pow(Base, Exponent)}")
            except ValueError:
                print("❌ Kindly enter numeric values.")

        try:
            Choice = int(input("Enter Choice From 1 to 5: "))
            if Choice == 1:
                StudentMarksReport()
            elif Choice == 2:
                TemperatureConversion()
            elif Choice == 3:
                SimpleInterestCalculator()
            elif Choice == 4:
                MathOperations()
            elif Choice == 5:
                print("You Successfully Exit The Program")
                break
            else:
                print("❌ Invalid choice! Please select between 1 to 5.")
        except ValueError:
            print("❌ Invalid choice! Please select between 1 to 5.")



