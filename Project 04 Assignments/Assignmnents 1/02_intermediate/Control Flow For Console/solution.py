import random

MAX_ROUNDS: int  = 5

def main():

    score: int = 0

    print("Welcome to the High-Low Game!")
    print("-------------------------------")

    for i in range(MAX_ROUNDS):

        print(f"Round {i + 1} ")
        my_number: int = random.randint(1, 100)
        comp_number: int = random.randint(1, 100)
        print(f"your number is {my_number}")
        user_input: str = input("Do you think your number is higher or lower than the computer's?: ")
        if user_input.lower() == "higher":
            if my_number > comp_number:
                score += 1
                print("You were right! The computer's number was", comp_number)
                print("Your score is now", score)
            else:
                print("Aww, that's incorrect. The computer's number was ", comp_number)
                print("Your score is now", score)
        if user_input.lower() == "lower":
            if my_number < comp_number:
                score += 1
                print("You were right! The computer's number was", comp_number)
                print("Your score is now", score)
            else:
                print("Aww, that's incorrect. The computer's number was ", comp_number)
                print("Your score is now", score)

    print("Thanks for playing!")
    print("---------------------------------")


if __name__ == "__main__":
    main()



