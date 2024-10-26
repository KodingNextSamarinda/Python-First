import time
import random
from art import asci

print(asci)

#Welcoming the player
print("\nWelcome to the Hangman game.")

#Wait 2 second
time.sleep(1.4)

#Inputing the player name
playername = input("Before you play please enter your name : ")
zx = input(f"\nHi {playername},do you want to know how to play hang man enter 'yes' if you want to know, enter 'no' if you dont want :")
if zx == "yes":
    print(f"Player guess one letter at a time - or he or she can use a turn to guess the entire word or words. \nFill in the letter everywhere it appears on the appropriate dash (or dashes) each time the person guesses correctly. \nCircle the letter on the alphabet if is guessed correctly. \n\nNow you've know how to play, let's begin.")

elif zx == "no":
    print(f"Ok then {playername}, let's begin the game.")

time.sleep(5)
#The word to guess
worddic = ["ayam", "sapi", "subscribe", "manusia", "makan", "pesawat", "basket", "ular"]
wordtoguess = random.choice(worddic)
guesses = ""
#Attempt
nyawa = 0

#Selecting the difficulty if easy = 10 attempts, if hard = 5 attempts
easy = 10
hard = 5
difficulty = input("\nSelect your difficulty 'easy'(10 attempt)/'hard'(5 attempt): ")

if difficulty == "easy" or "Easy":
    nyawa = easy
elif difficulty == "hard" or "Hard":
    nyawa = hard
else:
    nyawa = easy



while nyawa > 0:


    failed = 0
    for char in wordtoguess:


        if char in guesses:


            print(char, end=""),

        else:
            print("_", end=""),

            failed += 1



# When the player has guessed the correct answer
    if failed == 0:
        print("\n\nYou won")
# Finished the game/exit script
        break

# The player guess is not correct
    guess = input(". Guess a letter:")
    guesses += guess


    if guess not in wordtoguess:

#reduce the attempt
        nyawa -= 1


        print("Wrong")


        print("You have", nyawa, 'more guesses')

# There is no more attempt
        if nyawa == 0:

            print("You Lose, maybe try again next time")
            break










