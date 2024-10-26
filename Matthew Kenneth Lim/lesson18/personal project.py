import tkinter as tk
from tkinter import messagebox
from tkinter import *

window = tk.Tk()
window.title("Tic Tac toe")
window.geometry("380x400")

#move
clicked = True
count = 0
win = False
#function
def btn_clck(b):
    global clicked,count

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
        messagebox.showerror("Error", "The box have been choosed!!\n\nPlease choose antoher one.")

#won the game

def checkwon():
    global winner
    winner = False
#rows
    if (b1["text"] and b2["text"] and b3["text"] != " " or b4["text"] == b5["text"], b6["text"] != " " or b7["text"] == b8["text"], b9["text"] != " " ):

        winner = True
#collumn
    elif(b1["text"] == b4["text"], b7["text"] != " " or b2["text"] == b5["text"], b8["text"] != " " or b3["text"] == b6["text"], b9["text"] != " " ):

        winner = True
#diagonal
    elif (b1["text"] == b5["text"], b9["text"] != " " or b3["text"] == b5["text"] == b7["text"] != " "):

        winner = True



#widget
b1 = tk.Button(window, text=" ", font=("Helvetica",50), width=3 ,bg ="SystemButtonFace",command=lambda: btn_clck(b1))
b2 = tk.Button(window, text=" ", font=("Helvetica",50), width=3 ,bg ="SystemButtonFace",command=lambda: btn_clck(b2))
b3 = tk.Button(window, text=" ", font=("Helvetica",50), width=3 ,bg ="SystemButtonFace",command=lambda: btn_clck(b3))

b4 = tk.Button(window, text=" ", font=("Helvetica",50), width=3 ,bg ="SystemButtonFace",command=lambda: btn_clck(b4))
b5 = tk.Button(window, text=" ", font=("Helvetica",50), width=3 ,bg ="SystemButtonFace",command=lambda: btn_clck(b5))
b6 = tk.Button(window, text=" ", font=("Helvetica",50), width=3 ,bg ="SystemButtonFace",command=lambda: btn_clck(b6))

b7 = tk.Button(window, text=" ", font=("Helvetica",50), width=3 ,bg ="SystemButtonFace",command=lambda: btn_clck(b7))
b8 = tk.Button(window, text=" ", font=("Helvetica",50), width=3 ,bg ="SystemButtonFace",command=lambda: btn_clck(b8))
b9 = tk.Button(window, text=" ", font=("Helvetica",50), width=3 ,bg ="SystemButtonFace",command=lambda: btn_clck(b9))




#placement
b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)

b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)






window.mainloop()
