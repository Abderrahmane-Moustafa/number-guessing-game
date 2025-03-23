import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

right_num = random.randint(1, 100)
print(right_num)

def check_result(tries):
    while tries > 0:
        print(f"You have {tries} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess < right_num:
            print("Too low. \nGuess again.")
        elif guess > right_num:
            print("Too high. \nGuess again.")
        else:
            print(f"You got it! The answer was {right_num}.")
            return  # Exit the function when the player wins

        tries -= 1  # Reduce attempts after each guess

    print(f"You've run out of attempts! The number was {right_num}.")

# Assign attempts based on difficulty level
if level == "easy":
    check_result(10)
elif level == "hard":
    check_result(5)
else:
    print("Invalid input. Please restart the game and enter 'easy' or 'hard'.")
