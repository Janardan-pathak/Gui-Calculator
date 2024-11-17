import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("Calculator")

# Display widget (where input and output will appear)
display = tk.Entry(root, font=("Arial", 16), borderwidth=2, relief="solid")
display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)


# Button click handler
def on_button_click(value):
    # Append the clicked button's value to the display
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current_text + str(value))


# Function to evaluate the expression (for the "=" button)
def evaluate():
    try:
        # Get the expression from the display
        expression = display.get()
        # Evaluate the expression and display the result
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except Exception as e:
        # In case of an error, display "Error"
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")


# Function to clear the display (for the "C" button)
def clear_display():
    display.delete(0, tk.END)


# Button labels in the order you want to display them
buttons = [
    "7",
    "8",
    "9",
    "+",
    "4",
    "5",
    "6",
    "-",
    "1",
    "2",
    "3",
    "*",
    "C",
    "0",
    "=",
    "/",
]

# Create buttons in a 4x4 grid
row, col = 1, 0
for button in buttons:
    if button == "=":
        btn = tk.Button(root, text=button, width=5, height=2, command=evaluate)
    elif button == "C":
        btn = tk.Button(root, text=button, width=5, height=2, command=clear_display)
    else:
        btn = tk.Button(
            root,
            text=button,
            width=5,
            height=2,
            command=lambda b=button: on_button_click(b),
        )

    btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Configure grid weight to make the calculator responsive
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Start the main loop
root.mainloop()
