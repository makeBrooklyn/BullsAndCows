import random

def get_secret_number():
   digits = [str(i) for i in range(10)]
   random.shuffle(digits)
   return ''.join(digits[:4])

def count_bulls_and_cows(guess, secret):
   bulls = sum([a == b for a, b in zip(guess, secret)])
   cows = len(set(guess) & set(secret)) - bulls
   return bulls, cows

def play_game():
   games_played = 0
   total_guesses = 0

   surrender = False
   secret = get_secret_number()
   attempts = 0
   bulls = 0
   cows = 0

   print("\nWelcome to Bulls and Cows!\n")
   print("I've prepared a secret 4 digit number where none of the digits are repeated.")
   print("Keep guessing 4 digit numbers until you get the secret number.")
   print("If you get tired of guessing you can enter the word 'quit', 'bye', or 'exit'")
   print("Good Luck\n")

   while True:
      guess = input("Enter a 4-digit number: ")
      if guess.lower() in ["bye", "quit", "end"]:
         surrender = True
      elif not guess.isdigit() or len(guess) != 4:
         print("Invalid input. Please enter a 4-digit number.")
      else:
         attempts += 1
         bulls, cows = count_bulls_and_cows(guess, secret)
         print(f"Attempt: {attempts}, Bulls: {bulls}, Cows: {cows}")
      if (bulls == 4) or surrender:
         games_played += 1
         total_guesses += attempts



         if bulls == 4:
            avg_guesses_per_game = round(total_guesses / games_played) if games_played > 0 else 0
            print(f"Congratulations! You found the secret number in {attempts} attempt(s). The secret number was {secret}")
            print(f"\nGames: {games_played}, Guesses: {total_guesses}, Average: {avg_guesses_per_game}\n")
            play_again = input("Would you like to play again? (Y/n): ")
         else:
            print(f"Good try! You gave up after {attempts} attempt(s). The secret number was {secret}")
            play_again = "n"
         while play_again.lower() not in ["y", "n",""]:
               play_again = input("Invalid input. Please enter 'y' or 'n': ")
         if play_again.lower() in ["y",""]:
               secret = get_secret_number()
               attempts = 0
               bulls = 0
               cows = 0
               print("\nOk, I've got a new numer. Let's go!\n")
         else:
               print("Thanks for playing!")
               break

play_game()