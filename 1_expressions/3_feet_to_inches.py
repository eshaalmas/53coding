
# Function to convert feet to inches
def feet_to_inches(feet):
    inches = feet * 12
    return inches


# Ask the user for the number of feet
feet = float(input("Enter the number of feet: "))

# Convert feet to inches
inches = feet_to_inches(feet)

# Print the result
print(f"{feet} foot{'s' if feet != 1 else ''} is equal to {inches} inches.")
