# Convert Celsius to Fahrenheit
def  CelsiusToFahrenheit():
    Celsius = float(input("Enter Temperature in Celsius: "))
    Fahrenheit = (9 / 5 * Celsius) + 32
    print(f"Celsius to Fahrenheit: {Fahrenheit}")

# Convert Fahrenheit To Celsius
def FahrenheitToCelsius():
    Fahrenheit = float(input("Enter Temprature in Fahrenheit: "))
    Celsius = (Fahrenheit - 32) * 5 / 9
    print(f"Fahrenheit to Celsius: {Celsius}")

# Calculate Simple Interest
def simpleinterest():
    Principal = float(input("Enter Principal Amount: "))
    Rate = float(input("Enter Rate Of Interest: "))
    Time = float(input("Enter Time in Years: "))
    SimpleInterest = (Principal * Rate * Time) / 100
    print(f"Simple Interest: {SimpleInterest}")

print("1.Convert Celsius to Fahrenheit")
print("2.Convert Fahrenheit to Celsius")
print("3.Calculate Simple Interest")

Choice = int(input("Enter your Choice: "))
if Choice == 1:
    CelsiusToFahrenheit()
elif Choice == 2:
    FahrenheitToCelsius()
elif Choice == 3:
    simpleinterest()
else:
    print("Kindly Enter no. 1 to 3")
