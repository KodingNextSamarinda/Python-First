import tkinter as tk
from tkinter import ttk, messagebox

# Function to convert temperature
def convert_temperature():
    try:
        temp = float(entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number")
        return

    from_unit = from_combo.get()
    to_unit = to_combo.get()

    if from_unit == to_unit:
        result.set(f"{temp:.2f} {to_unit}")
        return

    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            converted_temp = (temp * 9/5) + 32
        elif to_unit == "Kelvin":
            converted_temp = temp + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            converted_temp = (temp - 32) * 5/9
        elif to_unit == "Kelvin":
            converted_temp = (temp - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            converted_temp = temp - 273.15
        elif to_unit == "Fahrenheit":
            converted_temp = (temp - 273.15) * 9/5 + 32

    result.set(f"{converted_temp:.2f} {to_unit}")

# Initialize the main Tkinter window
root = tk.Tk()
root.title("Temperature Converter")

root.geometry("440x310")

# Set the background color
root.config(bg='Alice Blue')

# Configure the grid to have one column that expands
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Labels and Entry widgets for temperature input
tk.Label(root, text="Temperature Converter", font=("Baskerville Old Face", 17, 'bold'), bg='Alice Blue').grid(row=0, column=0, columnspan=2, padx=30, pady=10, sticky='ew')
tk.Label(root, text="Enter Temperature:", font=("Baskerville Old Face", 15), bg='Alice Blue').grid(row=1, column=0, padx=10, pady=10, sticky='e')
entry = tk.Entry(root, width=20)
entry.grid(row=1, column=1, padx=10, pady=10)

# Combobox for selecting units
tk.Label(root, text="From:", font=("Baskerville Old Face", 15), bg='Alice Blue').grid(row=2, column=0, padx=10, pady=10, sticky='e')
from_combo = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
from_combo.grid(row=2, column=1, padx=10, pady=10)
from_combo.current(0)

tk.Label(root, text="To:", font=("Baskerville Old Face", 15), bg='Alice Blue').grid(row=3, column=0, padx=10, pady=10, sticky='e')
to_combo = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
to_combo.grid(row=3, column=1, padx=10, pady=10)
to_combo.current(1)

# Button to trigger conversion
convert_button = tk.Button(root, text="Convert", font=("Baskerville Old Face", 15), bg="cornflower blue", fg="white", command=convert_temperature)
convert_button.grid(row=4, column=0, columnspan=2, pady=10)

# Label to display result
result = tk.StringVar()
result_label = tk.Label(root, font=("Baskerville Old Face", 17), textvariable=result, bg='Alice Blue')
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
