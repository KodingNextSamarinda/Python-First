import tkinter


def show():
    def show1A():
        window.destroy()
        windowA = tkinter.Tk()
        windowA.geometry("1200x800")
        windowA.config(background='black')

    def show2A():
        window.destroy()
        window2A = tkinter.Tk()
        window2A.geometry("1200x800")
        window2A.config(background='black')

    def showA():
        window.destroy()
        window3A = tkinter.Tk()
        window3A.geometry("1200x800")
        window3A.config(background='black')

    window.destroy()
    window1A=tkinter.Tk()
    window1A.geometry("1200x800")
    window1A.config(background='black')

    label1 = tkinter.Label(window, text="""e
    """, font=("sans", 15), fg="white", bg="black")

    label2A = tkinter.Label(window, text="""
    25 Sepetember 2100



    """, font=("impact", 15), fg="white", bg="black")

    button1A = tkinter.Button(windowA, text="""Eee""", bg="white", fg="cadetblue", command=showA)
    button2A = tkinter.Button(window1A, text="Eee", bg="white", fg="cadetblue", command=show1A)
    button3A = tkinter.Button(window2A, text="Eee", bg="white", fg="cadetblue", command=show2A)

    labelE = tkinter.Label(window)
    labelXA = tkinter.Label(window, bg="black")

    # label1.pack()
    label2A.pack()
    button1A.pack()
    button2A.pack()
    button3A.pack()
    labelXA.pack()
    # labelE.pack()




def show1():
    window.destroy()
    window1B = tkinter.Tk()
    window1B.geometry("1200x800")
    window1B.config(background='black')

    def showB():
        window.destroy()
        windowB = tkinter.Tk()
        windowB.geometry("1200x800")
        windowB.config(background='black')

    def show2B():
        window.destroy()
        window2B = tkinter.Tk()
        window2B.geometry("1200x800")
        window2B.config(background='black')

    def show1B():
        window.destroy()
        window1B = tkinter.Tk()
        window1B.geometry("1200x800")
        window1B.config(background='black')

    label1 = tkinter.Label(window, text="""e
    """, font=("sans", 15), fg="white", bg="black")

    label2B = tkinter.Label(window, text="""
    25 Sepetember 2100

eeeee

    """, font=("impact", 15), fg="white", bg="black")

    button1B = tkinter.Button(window, text="E", bg="white", fg="cadetblue", command=showB)
    button2B = tkinter.Button(window, text="E", bg="white", fg="cadetblue", command=show1B)
    button3B = tkinter.Button(window, text="E", bg="white", fg="cadetblue", command=show2B)

    labelE = tkinter.Label(window)
    labelXB = tkinter.Label(window, bg="black")

    # label1.pack()
    label2B.pack()
    button1B.pack()
    button2B.pack()
    button3B.pack()
    labelXB.pack()
    # labelE.pack()




def show2():
    window.destroy()
    window1C = tkinter.Tk()
    window1C.geometry("1200x800")
    window1C.config(background='black')

    def show1C():
        window.destroy()
        window1B = tkinter.Tk()
        window1B.geometry("1200x800")
        window1B.config(background='black')

    def show2C():
        window.destroy()
        window1B = tkinter.Tk()
        window1B.geometry("1200x800")
        window1B.config(background='black')

    def showC():
        window.destroy()
        window1B = tkinter.Tk()
        window1B.geometry("1200x800")
        window1B.config(background='black')

    label1 = tkinter.Label(window, text="""eeee
    """, font=("sans", 15), fg="white", bg="black")

    label2C = tkinter.Label(window, text="""
    25 Sepetember 2100

eee

    """, font=("impact", 15), fg="white", bg="black")

    button1C = tkinter.Button(window, text="Ee", bg="white", fg="cadetblue", command=showC)
    button2C = tkinter.Button(window, text="Ee", bg="white", fg="cadetblue", command=show1C)
    button3C = tkinter.Button(window, text="Ee", bg="white", fg="cadetblue", command=show2C)

    labelE = tkinter.Label(window)
    labelXC = tkinter.Label(window,text = "eeee", bg="black")

    # label1.pack()
    label2C.pack()
    button1C.pack()
    button2C.pack()
    button3C.pack()
    labelXC.pack()
    # labelE.pack()





window = tkinter.Tk()
window.title("A Pro-ject")

window.geometry("1200x800")
window.config(background='black')



label1 = tkinter.Label(window, text = """eeee
""", font=("sans", 15), fg="white", bg="black")

label2 = tkinter.Label(window, text = """eee
25 Sepetember 2100
eeee


""", font=("impact", 15), fg="white", bg="black")

button1 = tkinter.Button(window, text="", bg="white", fg="cadetblue", command=show)
button2 = tkinter.Button(window, text="", bg="white", fg="cadetblue", command=show1)
button3 = tkinter.Button(window, text="", bg="white", fg="cadetblue", command=show2)

labelE = tkinter.Label(window)
labelX = tkinter.Label(window, bg="black")








#label1.pack()
label2.pack()
button1.pack()
button2.pack()
button3.pack()
labelX.pack()
#labelE.pack()


window.mainloop()


































