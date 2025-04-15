import random

print("I'm thinking of a number between 1 and 100.")

def main():
   secret_number = random.randint(1, 100)
   guess = int(input('Enter a guess: '))

   while guess != secret_number:
      if guess < secret_number:
         print('Your guess is too low.')
      else:
           print('Your guess is too high.') 
    
      print()
      guess = int(input('Enter a new guess: '))
   
   print('Congratulations! You guessed the right number and the number was', secret_number)
if __name__ == '__main__':
    main()