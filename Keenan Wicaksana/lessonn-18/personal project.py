import tkinter as tk
import tkinter.messagebox as msgbox #untuk menggunakan message box
expression = ""

def insert_number(number):
    global expression
    expression = expression + str(number)
    input_text.set(expression)

def button_clear():
    global expression
    expression = ""
    input_text.set("")

def result():
    global expression
    try:
        result = str(eval(expression))
        if result == "Infinity":
            input_text.set("Division by zero error")
        else:
            input_text.set(result)
    except Exception as e:
        input_text.set("Error")

def sqrt():
    global expression
    try:
        result = eval(expression) ** 0.5
        input_text.set(result)
        expression = str(result)
    except Exception as e:
        input_text.set("Error")

def close():
    ANSWER = msgbox.askokcancel("WARNING", "ALL PROGRESS ON KAKKULATOER 2.0.0...  IS GOING TO BE DESTROYED")
    if ANSWER == True:
        msgbox.showinfo("DESTINED DEATH", "THE destroy system WAS INITIATED SUCCESSFULLY")
        window.destroy()


window = tk.Tk()
window.title("Kakkulatoer 2.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0")
window.geometry("400x330")
window.resizable(False, False)


#components
input_text = tk.StringVar()#CREATE STRING TYPE OF VARIABLE
entry = tk.Entry (window, width = 18, borderwidth= 5, font=("arial", 18),textvariable= input_text, justify="right")
button_0 = tk.Button(window, text="0", padx=20, pady=20,bg="white", command= lambda : insert_number(0))
button_1 = tk.Button(window, text="1", padx=20, pady=20,bg="white", command= lambda : insert_number(1))
button_2 = tk.Button(window, text="2", padx=20, pady=20,bg="white", command= lambda : insert_number(2))
button_3 = tk.Button(window, text="3", padx=20, pady=20,bg="white", command= lambda : insert_number(3))
button_4 = tk.Button(window, text="4", padx=20, pady=20,bg="white", command= lambda : insert_number(4))
button_5 = tk.Button(window, text="5", padx=20, pady=20,bg="white", command= lambda : insert_number(5))
button_6 = tk.Button(window, text="6", padx=20, pady=20,bg="white", command= lambda : insert_number(6))
button_7 = tk.Button(window, text="7", padx=20, pady=20,bg="white", command= lambda : insert_number(7))
button_8 = tk.Button(window, text="8", padx=20, pady=20,bg="white", command= lambda : insert_number(8))
button_9 = tk.Button(window, text="9", padx=20, pady=20,bg="white", command= lambda : insert_number(9))

button_plus = tk.Button(window, text="+", padx=22, pady=20,bg="white", command= lambda : insert_number("+"))
button_minus = tk.Button(window, text="-", padx=22, pady=20,bg="white", command= lambda : insert_number("-"))
button_times = tk.Button(window, text="x", padx=22, pady=20,bg="white", command= lambda : insert_number("x"))
button_divide = tk.Button(window, text="/", padx=24, pady=20,bg="white", command= lambda : insert_number("/"))
button_equal = tk.Button(window, text= "=", padx=20, pady=20,bg="white", command= lambda : result())
button_clear = tk.Button(window, text= "clear", padx=10, pady=20,bg="white", command= button_clear)
button_squared = tk.Button (window,text = "^", padx= 20, pady=20 ,bg="white",command= lambda : insert_number("**"))
button_sqrt = tk.Button(window, text="√", padx=20, pady=20, bg="white", command=sqrt)
button_pi = tk.Button(window, text="phi", padx=20, pady=20, bg="white", command= lambda : insert_number(3.141592653589793))
button_destrock = tk.Button(window, text="destroy",padx=20, pady=20 ,command=close)
button_dot = tk.Button(window, text=".", padx=20, pady=20, bg="white", command= lambda : insert_number("."))
button_prison1 = tk.Button(window, text="(", padx=20, pady=20, bg="white", command= lambda : insert_number("("))
button_prison2 = tk.Button(window, text=")", padx=20, pady=20, bg="white", command= lambda : insert_number(")"))
button_persens = tk.Button(window, text="%", padx=20, pady=20, bg="white", command= lambda : insert_number("/100"))
#placement
entry.grid(row = 0, column= 0, columnspan=4)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_minus.grid(row=1, column=3)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_plus.grid(row=2, column=3)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_divide.grid(row=3, column=3)
button_clear.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_times.grid(row=1, column=4)
button_squared.grid(row=4, column=3)
button_sqrt.grid(row=1, column=5)
button_pi.grid(row=2, column=4)
button_destrock.grid(row=4, column=4)
button_dot.grid(row=3,column=4)
button_prison1.grid(row=2,column=5)
button_prison2.grid(row=3,column=5)
button_persens.grid(row=4, column=5)
window.mainloop()

