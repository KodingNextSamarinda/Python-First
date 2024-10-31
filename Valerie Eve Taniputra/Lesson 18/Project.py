import tkinter as tk
import time
import random

win = tk.Tk ()
win. geometry ("500x400")
win.title ("kdjv")


#function
Difficulty = tk.StringVar()
Difficulty.set(False)

if Difficulty == "Easy":
    words = ["secret", "stage", "table", "order", "action"]
elif Difficulty == "Medium":
    words = ["revival", "load", "shatter", "addicted", "colorful"]
elif Difficulty == "hard":
    words = ["hierarchy","spectrum", "threshold", "syndrome", "circumstances" ]


ran= random.choice(words)

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

#Widgets

lbl = tk.Label(win, text= "Hangman", font= ("Showcard Gothic", 15))
lbl2= tk.Label(win, text= "Difficulty (Easy,Medium, Hard)", font= ("Sagoe UI Variable",10))
Trial= tk.Label(win, text = f"you have {turns} guesses")
Rad1= tk.Radiobutton (win, text= "Easy",value= "Easy",variable= Difficulty)
Rad2= tk.Radiobutton (win, text= "Medium",value= "Medium",variable= Difficulty)
Rad3= tk.Radiobutton (win, text= "Hard",value= "Hard",variable= Difficulty)



#Placement

lbl.grid (column= 0, row= 0, columnspan= 3)
lbl2.grid(column= 0, row= 1, columnspan= 3)
Rad1.grid (column= 0, row= 2 , padx= 50)
Rad2.grid (column= 1, row= 2, padx= 80)
Rad3.grid (column= 2, row= 2, padx= 30)
Trial.grid (column= 1, row= 3)

win.mainloop()