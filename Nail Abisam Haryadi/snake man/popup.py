import tkinter as tk



window1 = tk.Tk()
window1.geometry("600x600")
window1.title("Main")
window1.configure(bg='black')


def showup1():
    window2.deiconify()
    window1.withdraw()

def showup2():
    window3.deiconify()
    window1.withdraw()

def showback():
    window1.deiconify()
    window2.withdraw()
    window3.withdraw()

pic = tk.PhotoImage(file="snake1.png")
pic1 = tk.PhotoImage(file="lay.png")
smallpick = pic1.subsample(5,5)
pic2 = tk.PhotoImage(file="htp.png")


LP = tk.Label(window1, image=pic)
btn1 = tk.Button(window1,image=smallpick,command=showup1)
btn2 = tk.Button(window1,image=pic2,command=showup2)


LP.pack(pady=10)

btn1.pack(ipadx=50,ipady=20)
btn2.pack(ipadx=30,ipady=10,pady=20)




window2 = tk.Tk()
window2.geometry("600x600")
window2.title("Game")


btn4 = tk.Button(window2,text="Back",command=showback)


btn4.pack()



window3 = tk.Tk()
window3.geometry("600x600")
window3.title("Tutorial")

btn3 = tk.Button(window3,text="Back",command=showback)


btn3.pack()




window3.withdraw()
window2.withdraw()
window1.mainloop()