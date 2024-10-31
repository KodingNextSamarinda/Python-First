import tkinter as tk

window = tk.Tk()
window.title("Kakkulatoer 2.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0")
window.geometry("300x300")

def close():
    window.destroy()

button_destrock = tk.Button(window, text="destroy kakkulatoer",command = close)
button_destrock.pack()


window.mainloop()















