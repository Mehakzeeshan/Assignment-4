import random

def guess_by_computer(x):
    low = 1
    high = x

    feedback = "" 
 
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low       # or high since low = high

        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    
    print(f"Yay! The computer guessed your number, {guess}, correctly!")

guess_by_computer(10)