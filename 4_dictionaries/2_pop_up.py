
fruit_prices = {
    'apple': 2.5,
    'durian': 5.0,
    'jackfruit': 3.0,
    'kiwi': 1.5,
    'rambutan': 4.0,
    'mango': 3.5
}


def calculate_total(fruit_prices):
    total_cost = 0  # Initialize total cost to 0

    for fruit, price in fruit_prices.items():

        quantity = int(input(f"How many ({fruit}) do you want?: "))

        total_cost += quantity * price

    # Print the total cost
    print(f"Your total is ${total_cost:.2f}")


# Run the program
calculate_total(fruit_prices)
