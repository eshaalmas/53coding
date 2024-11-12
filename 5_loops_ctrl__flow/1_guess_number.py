import random


def guess_my_number():

    number_to_guess = random.randint(0, 99)

    guess = -1

    while guess != number_to_guess:

        guess = int(input("Guess a number between 1 and 99 : "))

        if guess < number_to_guess:
            print("Your guess is too low.")

        elif guess > number_to_guess:
            print("Your guess is too high.")

        else:
            print(f"Congrats! The number was: {number_to_guess}")


guess_my_number()
