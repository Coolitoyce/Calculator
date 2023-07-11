from tkinter import *


def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)


def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total

    except SyntaxError:
        equation_label.set("Syntax Error")
        equation_text = ""

    except ZeroDivisionError:
        equation_label.set("Math Error")
        equation_text = ""


def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""


window = Tk()
window.title("Calculator")
window.geometry("500x635")

equation_text = ""
equation_label = StringVar()

label = Label(
    window,
    textvariable=equation_label,
    font=("Consolas", 20),
    bg="#D6E3D6",
    width=24,
    height=4,
)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(
    frame,
    text=1,
    bg="#EBEBEB",
    activebackground="#EBEBEB",
    height=4,
    width=9,
    font=35,
    command=lambda: button_press(1),
)
button1.grid(row=0, column=0)

button2 = Button(
    frame,
    text=2,
    bg="#EBEBEB",
    activebackground="#EBEBEB",
    height=4,
    width=9,
    font=35,
    command=lambda: button_press(2),
)
button2.grid(row=0, column=1)

button3 = Button(
    frame,
    text=3,
    bg="#EBEBEB",
    activebackground="#EBEBEB",
    height=4,
    width=9,
    font=35,
    command=lambda: button_press(3),
)
button3.grid(row=0, column=2)

button4 = Button(
    frame,
    text=4,
    bg="#EBEBEB",
    activebackground="#EBEBEB",
    height=4,
    width=9,
    font=35,
    command=lambda: button_press(4),
)
button4.grid(row=1, column=0)

button5 = Button(
    frame,
    text=5,
    bg="#EBEBEB",
    activebackground="#EBEBEB",
    height=4,
    width=9,
    font=35,
    command=lambda: button_press(5),
)
button5.grid(row=1, column=1)

button6 = Button(
    frame,
    text=6,
    bg="#EBEBEB",
    activebackground="#EBEBEB",
    height=4,
    width=9,
    font=35,
    command=lambda: button_press(6),
)
button6.grid(row=1, column=2)

button7 = Button(
    frame,
    text=7,
    bg="#EBEBEB",
    activebackground="#EBEBEB",
    height=4,
    width=9,
    font=35,
    command=lambda: button_press(7),
)
button7.grid(row=2, column=0)

button8 = Button(
    frame,
    text=8,
    bg="#EBEBEB",
    activebackground="#EBEBEB",
    height=4,
    width=9,
    font=35,
    command=lambda: button_press(8),
)
button8.grid(row=2, column=1)

button9 = Button(
    frame,
    text=9,
    bg="#EBEBEB",
    activebackground="#EBEBEB",
    height=4,
    width=9,
    font=35,
    command=lambda: button_press(9),
)
button9.grid(row=2, column=2)

button0 = Button(
    frame,
    text=0,
    bg="#EBEBEB",
    activebackground="#EBEBEB",
    height=4,
    width=9,
    font=35,
    command=lambda: button_press(0),
)
button0.grid(row=3, column=0)

plus = Button(
    frame,
    text="+",
    bg="#0bd483",
    activebackground="#0bd483",
    height=4,
    width=9,
    font=35,
    command=lambda: button_press("+"),
)
plus.grid(row=0, column=3)

minus = Button(
    frame,
    text="-",
    bg="#0bd483",
    activebackground="#0bd483",
    height=4,
    width=9,
    font=35,
    command=lambda: button_press("-"),
)
minus.grid(row=1, column=3)

multiply = Button(
    frame,
    text="x",
    bg="#0bd483",
    activebackground="#0bd483",
    height=4,
    width=9,
    font=35,
    command=lambda: button_press("*"),
)
multiply.grid(row=2, column=3)

divide = Button(
    frame,
    text="÷",
    bg="#0bd483",
    activebackground="#0bd483",
    height=4,
    width=9,
    font=35,
    command=lambda: button_press("/"),
)
divide.grid(row=3, column=3)

equal = Button(
    frame,
    text="=",
    bg="#C65A57",
    activebackground="#C65A57",
    height=4,
    width=9,
    font=35,
    command=equals,
)
equal.grid(row=3, column=2)

decimal = Button(
    frame,
    text=".",
    bg="#EBEBEB",
    activebackground="#EBEBEB",
    height=4,
    width=9,
    font=35,
    command=lambda: button_press("."),
)
decimal.grid(row=3, column=1)

clearbutton = Button(
    window,
    text="AC",
    bg="#FF7931",
    activebackground="#FF7931",
    height=2,
    width=12,
    font=35,
    command=clear,
)
clearbutton.pack()

window.mainloop()
