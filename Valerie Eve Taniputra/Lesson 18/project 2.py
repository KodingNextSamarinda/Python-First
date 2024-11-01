import tkinter as tk
import random

# Function to start the game
guesses = ''

def start_game():
    global ran, guesses, turns
    guesses = ''
    difficulty = Difficulty.get()
    if difficulty == "Easy":
        words = ["secret", "stage", "table", "order", "action"]
    elif difficulty == "Medium":
        words = ["revival", "load", "shatter", "addicted", "colorful"]
    elif difficulty == "Hard":
        words = ["hierarchy", "spectrum", "threshold", "syndrome", "circumstances"]
    else:
        lbl_result.config(text="Please select a difficulty level")
        return

    ran = random.choice(words)
    turns = 10
    update_display()
    lbl_result.config(text="Game started! Good luck!")
    win2.deiconify()

# Function to update the display
def update_display():
    display_word = ''.join([char if char in guesses else '_' for char in ran])
    lbl_word.config(text=display_word)
    lbl_turns.config(text=f"You have {turns} guesses left")

# Function to process the guess
def process_guess():
    global turns, guesses
    guess = entry_guess.get().lower()
    entry_guess.delete(0, tk.END)

    if guess in guesses:
        lbl_result.config(text="You already guessed that letter!")
        return

    guesses += guess
    if guess not in ran:
        turns -= 1

    update_display()

    if turns == 0:
        lbl_result.config(text=f"You Lose! The word was: {ran}")
    elif all(char in guesses for char in ran):
        lbl_result.config(text="You won!")

win = tk.Tk()
win.geometry("500x400")
win.title("Hangman")

Difficulty = tk.StringVar()
Difficulty.set(None)

# Widgets for main window
lbl = tk.Label(win, text="Hangman", font=("Showcard Gothic", 15))
lbl2 = tk.Label(win, text="Difficulty (Easy, Medium, Hard)", font=("Sagoe UI Variable", 10))
entry_guess = tk.Entry(win, font=("Sagoe UI Variable", 10))
btn_guess = tk.Button(win, text="Guess", command=process_guess)
btn_start = tk.Button(win, text="Start Game", command=start_game)
Rad1 = tk.Radiobutton(win, text="Easy", value="Easy", variable=Difficulty)
Rad2 = tk.Radiobutton(win, text="Medium", value="Medium", variable=Difficulty)
Rad3 = tk.Radiobutton(win, text="Hard", value="Hard", variable=Difficulty)

# Placement for main window
lbl.grid(column=0, row=0, columnspan=3)
lbl2.grid(column=0, row=1, columnspan=3)
Rad1.grid(column=0, row=2, padx=50)
Rad2.grid(column=1, row=2, padx=80)
Rad3.grid(column=2, row=2, padx=30)
btn_start.grid(column=1, row=3)

# Create and setup win2 window
win2 = tk.Toplevel(win)
win2.geometry("500x400")
win2.title("GAME START")
win2.withdraw()

lblwin2 = tk.Label(win2, text="GAME START HERE", font=("Showcard Gothic", 15))
lbl_word = tk.Label(win2, text="", font=("Sagoe UI Variable", 20))
lbl_turns = tk.Label(win2, text="", font=("Sagoe UI Variable", 10))
lbl_result = tk.Label(win2, text="", font=("Sagoe UI Variable", 10))
entry_guess = tk.Entry(win2, font=("Sagoe UI Variable", 10))
btn_guess = tk.Button(win2, text="Guess", command=process_guess)

# Placement for win2 window
lblwin2.pack()
lbl_word.pack()
lbl_turns.pack()
entry_guess.pack()
btn_guess.pack()
lbl_result.pack()

win.mainloop()
win2.mainloop()
