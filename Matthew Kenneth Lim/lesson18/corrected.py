import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Tic Tac Toe")
window.geometry("380x400")

# Move
clicked = True
count = 0
win = 0

# Function to handle button click
def btn_clck(b):
    global clicked, count

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        checkwon()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        checkwon()
    else:
        messagebox.showerror("Error", "The box has been chosen!\n\nPlease choose another one.")

# Function to disable all buttons after game over
def disable_buttons():
    for button in buttons:
        button.config(state=tk.DISABLED)

# Function to check for a win or draw
def checkwon():
    global winner, win
    winner = False

    # Check rows
    if (buttons[0]["text"] == buttons[1]["text"] == buttons[2]["text"] != " " or
        buttons[3]["text"] == buttons[4]["text"] == buttons[5]["text"] != " " or
        buttons[6]["text"] == buttons[7]["text"] == buttons[8]["text"] != " "):

        winner = True

    # Check columns
    elif (buttons[0]["text"] == buttons[3]["text"] == buttons[6]["text"] != " " or
          buttons[1]["text"] == buttons[4]["text"] == buttons[7]["text"] != " " or
          buttons[2]["text"] == buttons[5]["text"] == buttons[8]["text"] != " "):

        winner = True

    # Check diagonals
    elif (buttons[0]["text"] == buttons[4]["text"] == buttons[8]["text"] != " " or
          buttons[2]["text"] == buttons[4]["text"] == buttons[6]["text"] != " "):

        winner = True

    if winner:
        win += 1
        if win == 1:
            if clicked:
                messagebox.showinfo("Winner!!", "Player O has won!")
            else:
                messagebox.showinfo("Winner!!", "Player X has won!")
        else:
            messagebox.showinfo("Winner!!", "Game Over!!")
        disable_buttons()
    elif count == 9:
        messagebox.showinfo("Tie Game", "It's a tie!")
        disable_buttons()

# Widgets
buttons = []

for i in range(3):
    for j in range(3):
        button = tk.Button(window, text=" ", font=("Helvetica", 50), width=3, bg="SystemButtonFace", command=lambda row=i, col=j: btn_clck(buttons[row * 3 + col]))
        button.grid(row=i, column=j)
        buttons.append(button)

window.mainloop()
