# Ask the user for the temperature in Fahrenheit
fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

# Convert the temperature to Celsius using the formula
celsius = (fahrenheit - 32) * 5/9

# Output the result
print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius.")
