import random


def number_guessing_agent():

    secret_number = random.randint(1, 100)

    attempts = 0

    print("Think of a number between 1 and 100.")
    print("I will try to guess it!")

    low = 1
    high = 100

    while low <= high:

        guess = (low + high) // 2
        attempts += 1

        print("\nMy Guess:", guess)

        feedback = input(
            "Enter Higher / Lower / Correct: "
        ).lower()

        if feedback == "correct":

            print("Correct! I guessed your number.")
            print("Total Attempts:", attempts)
            return

        elif feedback == "higher":
            low = guess + 1

        elif feedback == "lower":
            high = guess - 1

        else:
            print("Invalid feedback. Try again.")

    print("Invalid feedback sequence or inconsistent answers.")


number_guessing_agent()