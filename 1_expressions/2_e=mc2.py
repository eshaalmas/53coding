# Speed of light in meters per second (m/s)
c = 3.00e8

while True:
    # Ask the user for the mass in kilograms
    try:
        mass = float(
            input("Enter mass in kilograms (or type 'exit' to quit): "))

        # Calculate the energy using E = m * c^2
        energy = mass * c**2

        # Output the result
        print(f"Energy equivalent to {mass} kg of mass is {energy} joules.")

    except ValueError:
        # # If the user inputs 'exit', break the loop
        user_input = input(
            "Wrong input. Type 'exit' to quit or press Enter to try again: ")
