def fibonacci_up_to_max(max_value):
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1

    # Print the Fibonacci sequence as long as the next number is <= max_value
    while a <= max_value:
        print(a, end=" ")
        # Update the Fibonacci numbers for the next iteration
        a, b = b, a + b


# Example usage:
max_value = int(input("Enter the maximum value for the Fibonacci sequence: "))
fibonacci_up_to_max(max_value)
