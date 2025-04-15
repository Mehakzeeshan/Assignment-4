import random


def guess_the_number():
    number = random.randint(1, 100)
    guess_attempts: int = 7
   
    print('Welcome To Number Guessing Game!')

    print('I have selected a number between 1 and 100. Can you guess it?')

    while guess_attempts > 0:
        print(f'\nYou have {guess_attempts} attempts left.')
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
    
        if guess < number:
            print("Too low! Tell another.")
        elif guess > number:
            print("Too high! Tell another.")
        else:
            print(f"Congratulations! You've guessed the number {number} correctly in {7 - guess_attempts + 1} tries.")
            return
       
        guess_attempts -= 1
    
    print(f"\nSorry, you've run out of guesses. The number was {number}.")

guess_the_number()