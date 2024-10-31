import time
import random

name = input("What is your name? ")

print("Hello, " + name, "Time to play hangman!")



time.sleep(1)
print ("loading game 10%")
time.sleep(0.5)
print ("loading game 35%")
time.sleep(0.5)
print ("loading game 60%")
time.sleep(0.5)
print ("loading game 85%")
time.sleep(0.5)
print ("loading game 100%")
time.sleep(1)

difficulty= input("choose a difficulty (hard,medium,easy): ")
if difficulty == "easy" or difficulty == "Easy":
    word = ["secret", "stage", "table", "order", "action"]
elif difficulty == "medium" or difficulty == "Medium":
    word = ["revival", "load", "shatter", "addicted", "colorful"]
elif difficulty == "Hard" or difficulty == "hard":
    word = ["hierarchy","spectrum", "threshold", "syndrome", "circumstances" ]
else:
    print ("that's not a word")

ran = random.choice (word)

print("Start guessing...")
time.sleep (0.5)

guesses = ''

turns = 10


while turns > 0:

    failed = 0
    for char in ran:

        # see if the character is in the players guess
        if char in guesses:

            # print then out the character
            print(char, end=""),

        else:

            # if not found, print a dash
            print("_", end=""),

            # and increase the failed counter with one
            failed += 1

            # if failed is equal to zero

    # print You Won
    if failed == 0:
        print("\n You won")
        # exit the script
        break
        # ask the user go guess a character
    guess = input("\n guess a character:")

    # set the players guess to guesses
    guesses += guess

    # if the guess is not found in the secret word
    if guess not in ran:

        # turns counter decreases with 1 (now 9)
        turns -= 1

        # print wrong
        print("Wrong")

        # how many turns are left
        print("You have", + turns, 'more guesses')

        # if the turns are equal to zero
        if turns == 0:
            # print "You Lose"
            print("\n You Lose")
            print (ran)