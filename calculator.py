import tkinter as tk


# Create the main window
window = tk.Tk()
window.title("Calculator")
window.geometry("350x500")
window.resizable(False, False)
window.configure(bg="#222222")


# Store the current expression
expression = ""


# Display the expression
display = tk.Entry(
    window,
    font=("Canva sans", 30, "bold"),
    justify="right",
    bg="#030958",
    fg="white",
    insertbackground="white",
    borderwidth=0
    corner_radius=15,

)

display.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=10,
    pady=20,
    ipady=15,
    sticky="nsew"
)


# Function to add numbers/operators
def button_click(value):
    global expression

    expression += str(value)

    display.delete(0, tk.END)
    display.insert(tk.END, expression)


# Function to calculate the result
def calculate():
    global expression

    try:
        result = eval(expression)

        display.delete(0, tk.END)
        display.insert(tk.END, str(result))

        expression = str(result)

    except ZeroDivisionError:
        display.delete(0, tk.END)
        display.insert(tk.END, "Cannot divide by zero")

        expression = ""

    except Exception:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

        expression = ""


# Function to clear the calculator
def clear():
    global expression

    expression = ""

    display.delete(0, tk.END)


# Function to delete the last character
def backspace():
    global expression

    expression = expression[:-1]

    display.delete(0, tk.END)
    display.insert(tk.END, expression)


# Calculator buttons
buttons = [
    ("C", 1, 0),
    ("⌫", 1, 1),
    ("(", 1, 2),
    (")", 1, 3),

    ("7", 2, 0),
    ("8", 2, 1),
    ("9", 2, 2),
    ("/", 2, 3),

    ("4", 3, 0),
    ("5", 3, 1),
    ("6", 3, 2),
    ("*", 3, 3),

    ("1", 4, 0),
    ("2", 4, 1),
    ("3", 4, 2),
    ("-", 4, 3),

    ("0", 5, 0),
    (".", 5, 1),
    ("=", 5, 2),
    ("+", 5, 3),
]


# Create buttons
for text, row, column in buttons:

    if text == "C":
        command = clear

    elif text == "⌫":
        command = backspace

    elif text == "=":
        command = calculate

    else:
        command = lambda value=text: button_click(value)

    button = tk.Button(
        window,
        text=text,
        font=("Arial", 18),
        bg="#030958",
        bg="#000107",
        fg="white",
        activebackground="#666666",
        activeforeground="white",
        borderwidth=0,
        command=command
        corner_radius=15,
    )

    button.grid(
        row=row,
        column=column,
        padx=5,
        pady=5,
        ipadx=10,
        ipady=15,
        sticky="nsew"
    )


# Make rows and columns expand evenly
for i in range(6):
    window.rowconfigure(i, weight=1)

for i in range(4):
    window.columnconfigure(i, weight=1)


# Start the calculator
window.mainloop()