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
        5. String Operations
        6. Exit
        ==============================
        """)
        def StudentMarksReport():
            Name = input("Enter Student Name: ")
            MarksOfSubject1 = float(input("Enter Marks Of Subject1: "))
            MarksOfSubject2 = float(input("Enter Marks Of Subject2: "))
            MarksOfSubject3 = float(input("Enter Marks Of Subject3: "))
            TotalMarks = MarksOfSubject1 + MarksOfSubject2 + MarksOfSubject3
            Percentage = TotalMarks / 3
            if Percentage >= 90:
                print("Grade Is:A+")
            elif 75 <= Percentage <= 89:
                print("Grade Is:A")
            elif 60 <= Percentage <= 74:
                print("Grade Is:B")
            else:
                print("Grade Is:C")
        def TemperatureConversion():
            print("""
        1.Celsius → Fahrenheit
        2.Fahrenheit → Celsius
        """)
            Choice = int(input("Enter Choice From 1 to 2: "))
            def CelsiusToFahrenheit():
                Celsius = float(input("Enter Temperature In Celsius: "))
                Fahrenheit = (Celsius * 9 / 5) + 32
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
                print("Error,Enter Choice From 1 to 2")
        def SimpleInterestCalculator():
            Principal = float(input("Enter Principal Amount: "))
            RateOfInterest = float(input("Enter Rate Of Interest: "))
            TimeInYears = float(input("Enter Time In Years: "))
            SimpleInterest = (Principal * RateOfInterest * TimeInYears) / 100
            print(f"Simple Interest Is:{SimpleInterest}")
        def MathOperations():
            Numbers = input("Enter Multiple Numbers (space-separated): ").split()
            nums = []
            for i in Numbers:
                num = int(i)
                nums.append(num)
            print(f"Maximum Value Is:{max(nums)},Minimum Value Is:{min(nums)}")
            Numbers = int(input("Enter Number For Find Absolute Value: "))
            print(f"Absolute value of a given number:{abs(Numbers)}")
            Base = float(input("Enter Base Value: "))
            exponent = float(input("Enter Exponent Value: "))
            print(f"base^exponent Is:{pow(Base,exponent)}")
        def StringOperations():
            s1 = "Hello World"
            print(f"Length Of String Is:{len(s1)}")
            print(f"First And Last Character:{s1[0]},{s1[-1]}")
            print(s1[2:7:1])
            print(s1[2:9:2])
            print(s1[1:12:3])
            print(type(s1[2:7:1]))
            print(type(s1[2:9:2]))
            print(type(s1[1:12:3]))


        Choice = int(input("Enter Choice From 1 to 6: "))
        if Choice == 1:
            StudentMarksReport()
        elif Choice == 2:
            TemperatureConversion()
        elif Choice == 3:
            SimpleInterestCalculator()
        elif Choice == 4:
            MathOperations()
        elif Choice == 5:
            StringOperations()
        elif Choice == 6:
            print("You Successfully Exit The Program")
            break
        else:
            print("Error,Enter A Number From 1 To 6")








