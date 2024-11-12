# Ask the user for two numbers
num1 = float(input("Enter the first number (dividend): "))

num2 = float(input("Enter the second number (divisor): "))

if num2 != 0:

    result = num1 / num2

    remainder = num1 % num2

    print(f"The result of dividing {num1} by {num2} is: {result:.2f}")

    print(f"The remainder when dividing {num1} by {num2} is: {remainder:.2f}")

else:

    print("Error: Cannot divide by zero.")
