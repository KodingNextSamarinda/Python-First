"""
https://www.geeksforgeeks.org/rock-paper-and-scissor-game-using-tkinter/
"""
import random
import tkinter as tk

window = tk.Tk()
window.geometry("400x400")
window.title("Rock paper scissors or die By James")

#computer value
computer_value = {"0": "Rock","1": "Paper","2": "Scissor"}

def reset_game():
    button1["state"] = "active"
    button2["state"] = "active"
    button3["state"] = "active"
    label1.config(text="player farmer")
    label3.config(text="zombie")
    label4.config(text="")
def button_disable():
    button1["state"] = "disable"
    button2["state"] = "disable"
    button3["state"] = "disable"

def isrock():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Rock":
        match_result = "Match Draw"
    elif c_v == "Scissor":
        match_result = "Farmer Win"
    else:
        match_result = " The zombie ate your brain"
    label4.config(text=match_result)
    label1.config(text="Rock")
    label3.config(text=c_v)
    button_disable()

def ispaper():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Paper":
        match_result = "Match Draw"
    elif c_v == "Scissor":
        match_result = "Zombies ate your brain"
    else:
        match_result = "Farmer Win"
    label4.config(text=match_result)
    label1.config(text="Paper")
    label3.config(text=c_v)
    button_disable()

def isscissor():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Rock":
        match_result = "Zombie ate your brain"
    elif c_v == "Scissor":
        match_result = "Match Draw"
    else:
        match_result = "Farmer Win"
    label4.config(text=match_result)
    label1.config(text="Scissor")
    label3.config(text=c_v)
    button_disable()

#widget
label = tk.Label(window, text = "Rock paper scissors or die", font = "normal 20 bold")
label1 = tk.Label(window, text = "player farmer", font = "normal 15")
label2 = tk.Label(window, text = "vs", font = "normal 15")
label3 = tk.Label(window, text = "zombie", font = "normal 15")
label4 = tk.Label(window, text = "", font = "normal 20", bg = "Red", width = 20, borderwidth = 2, relief = "solid")
button1 = tk.Button(window, text = "Rock", font = "normal 15", command = isrock)
button2 = tk.Button(window, text = "Paper", font = "normal 15", command = ispaper)
button3 = tk.Button(window, text = "Scissors", font = "normal 15", command = isscissor)
button4 = tk.Button(window, text = "Reset game", font = "normal 15", command = reset_game)

#grid
label.grid(row = 0, columnspan = 3, pady = 10)
label1.grid(row = 1, column = 0, pady = 10)
label2.grid(row = 1, column = 1, pady = 10)
label3.grid(row = 1, column = 2, pady = 10)
label4.grid(row = 2, columnspan = 3, pady = 10)
button1.grid(row = 4, column = 0, pady = 10)
button2.grid(row = 4, column = 1, pady = 10)
button3.grid(row = 4, column = 2, pady = 10)
button4.grid(row = 5, column = 1, pady = 10)


window.mainloop()