import tkinter as tk


# MAIN WINDOW

window = tk.Tk()
window.title("Calculator")
window.geometry("350x520")
window.resizable(False, False)

# Main background color
window.configure(bg="#0F172A")


# FONT SETTINGS

FONT = "Canva Sans"

# If Canva Sans is not installed on your computer,
# Tkinter will use another available font.


# STORE EXPRESSION

expression = ""


# DISPLAY

display = tk.Entry(
    window,
    font=(FONT, 28, "bold"),
    justify="right",
    bg="#1E293B",
    fg="#FFFFFF",
    insertbackground="white",
    borderwidth=0,
    highlightthickness=0
)

display.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=15,
    pady=20,
    ipady=18,
    sticky="nsew"
)


# FUNCTIONS

def button_click(value):
    global expression

    expression += str(value)

    display.delete(0, tk.END)
    display.insert(tk.END, expression)


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


def clear():
    global expression

    expression = ""

    display.delete(0, tk.END)


def backspace():
    global expression

    expression = expression[:-1]

    display.delete(0, tk.END)
    display.insert(tk.END, expression)


# ROUNDED BUTTON FUNCTION

def create_rounded_button(
    parent,
    text,
    row,
    column,
    command,
    bg="#334155",
    fg="#FFFFFF"
):

    canvas = tk.Canvas(
        parent,
        bg="#0F172A",
        highlightthickness=0,
        borderwidth=0,
        height=65
    )

    canvas.grid(
        row=row,
        column=column,
        padx=6,
        pady=6,
        sticky="nsew"
    )

    def draw_button(event=None):

        canvas.delete("all")

        width = canvas.winfo_width()
        height = canvas.winfo_height()

        radius = 8

        # Rounded rectangle
        canvas.create_polygon(
            radius, 0,
            width - radius, 0,
            width, radius,
            width, height - radius,
            width - radius, height,
            radius, height,
            0, height - radius,
            0, radius,
            smooth=True,
            fill=bg,
            outline=""
        )

        # Button text
        canvas.create_text(
            width / 2,
            height / 2,
            text=text,
            font=(FONT, 18, "bold"),
            fill=fg
        )

    def on_click(event):
        command()

    def on_enter(event):
        canvas.configure(cursor="hand2")

    canvas.bind("<Configure>", draw_button)
    canvas.bind("<Button-1>", on_click)
    canvas.bind("<Enter>", on_enter)

    return canvas


# CALCULATOR BUTTONS

buttons = [

    ("C", 1, 0),
    ("DEL", 1, 1),
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


# CREATE BUTTONS

for text, row, column in buttons:

    if text == "C":
        command = clear

    elif text == "DEL":
        command = backspace

    elif text == "=":
        command = calculate

    else:
        command = lambda value=text: button_click(value)

    # Different colors for buttons
    if text in ["/", "*", "-", "+"]:
        button_bg = "#2563EB"

    elif text == "=":
        button_bg = "#22C55E"

    elif text in ["C", "⌫"]:
        button_bg = "#EF4444"

    else:
        button_bg = "#334155"

    create_rounded_button(
        window,
        text,
        row,
        column,
        command,
        bg=button_bg
    )


# GRID SETTINGS

for i in range(6):
    window.rowconfigure(i, weight=1)

for i in range(4):
    window.columnconfigure(i, weight=1)


# START APPLICATION

window.mainloop()