Numbers = input("Enter Number With Spaces Separated: ").split()
nums = []
for num in Numbers:
    n = int(num)
    nums.append(n)

Number = float(input("Enter a Number: "))

Base = float(input("Enter Base Number: "))
Exponent = float(input("Enter Exponent Number: "))

print(f"Maximum Value: {max(nums)}")
print(f"Minimum Value: {min(nums)}")
print(f"Absolute value: {abs(Number)}")
print(f"Result: {pow(Base,Exponent)}")

print("Thank you for using the Math Operations Tool!")

