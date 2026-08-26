import customtkinter as ctk


# Create the main window
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

window = ctk.CTk()
window.title("Calculator")
window.geometry("350x500")
window.resizable(False, False)
window.configure(fg_color="#222222")


# Store the current expression
expression = ""


# Display the expression
display = ctk.CTkEntry(
    window,
    font=("Canva sans", 30, "bold"),
    justify="right",
    fg_color="#030958",
    text_color="white",
    border_width=0,
    corner_radius=30,
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
    display.delete(0, ctk.END)
    display.insert(ctk.END, expression)


# Function to calculate the result
def calculate():
    global expression

    try:
        result = eval(expression)
        display.delete(0, ctk.END)
        display.insert(ctk.END, str(result))
        expression = str(result)

    except ZeroDivisionError:
        display.delete(0, ctk.END)
        display.insert(ctk.END, "Cannot divide by zero")
        expression = ""

    except Exception:
        display.delete(0, ctk.END)
        display.insert(ctk.END, "Error")
        expression = ""


# Function to clear the calculator
def clear():
    global expression

    expression = ""
    display.delete(0, ctk.END)


# Function to delete the last character
def backspace():
    global expression

    expression = expression[:-1]
    display.delete(0, ctk.END)
    display.insert(ctk.END, expression)


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

    button = ctk.CTkButton(
        window,
        text=text,
        font=("Arial", 18),
        fg_color="#030958",
        hover_color="#000107",
        text_color="white",
        border_width=0,
        corner_radius=28,
        height=52,
        command=command,
    )

    button.grid(
        row=row,
        column=column,
        padx=5,
        pady=5,
        ipadx=10,
        ipady=10,
        sticky="nsew",
    )


# Make rows and columns expand evenly
for i in range(6):
    window.rowconfigure(i, weight=1)

for i in range(4):
    window.columnconfigure(i, weight=1)


# Start the calculator
window.mainloop()