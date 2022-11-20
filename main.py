## Import library
from tkinter import *
import tkinter as tk

expression = ""

def press(num):
    global expression

    expression = expression + str(num)

    equation.set(expression)

def equal_press():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ''
    except:
        equation.set(" error ")
        expression = ''

def clear_press():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    # create a window
    window = tk.Tk()

    ## widgets
    window.title("Simple calculator")
    window.geometry("370x200")

    equation = StringVar() #set, get
    expression_field = Entry(window, textvariable=equation)

    expression_field.grid(columnspan=4, ipadx=100, row=0)

    button1 = Button(window, text = " 1 ", fg="black", bg="red", command=lambda: press(1), 
        height=1, width=7)
    button1.grid(row=1, column=0)

    button2 = Button(window, text=" 2 ", fg="black", bg="red", command=lambda: press(2), 
        height=1, width=7)
    button2.grid(row=1, column=1)

    button3 = Button(window, text = " 3 ", fg="black", bg="red", command=lambda: press(3), 
        height=1, width=7)
    button3.grid(row=1, column=2)

    button4 = Button(window, text=" 4 ", fg="black", bg="red", command=lambda: press(4), 
        height=1, width=7)
    button4.grid(row=2, column=0)

    button5 = Button(window, text = " 5 ", fg="black", bg="red", command=lambda: press(5), 
        height=1, width=7)
    button5.grid(row=2, column=1)

    button6 = Button(window, text=" 6 ", fg="black", bg="red", command=lambda: press(6), 
        height=1, width=7)
    button6.grid(row=2, column=2)

    button7 = Button(window, text = " 7 ", fg="black", bg="red", command=lambda: press(7), 
        height=1, width=7)
    button7.grid(row=3, column=0)

    button8 = Button(window, text=" 8 ", fg="black", bg="red", command=lambda: press(8), 
        height=1, width=7)
    button8.grid(row=3, column=1)

    button9 = Button(window, text = " 9 ", fg="black", bg="red", command=lambda: press(9), 
        height=1, width=7)
    button9.grid(row=3, column=2)

    button0 = Button(window, text=" 0 ", fg="black", bg="red", command=lambda: press(0), 
        height=1, width=7)
    button0.grid(row=4, column=0)

    button_plus = Button(window, text=" + ", fg="black", bg="red", command=lambda: press("+"), 
        height=1, width=7)
    button_plus.grid(row=1, column=3)

    button_minus = Button(window, text=" - ", fg="black", bg="red", command=lambda: press("-"), 
        height=1, width=7)
    button_minus.grid(row=2, column=3)

    button_multiply = Button(window, text=" x ", fg="black", bg="red", command=lambda: press("*"), 
        height=1, width=7)
    button_multiply.grid(row=3, column=3)

    button_divide = Button(window, text=" / ", fg="black", bg="red", command=lambda: press("/"), 
        height=1, width=7)
    button_divide.grid(row=4, column=3)

    equal = Button(window, text=" = ", fg="black", 
        bg="red", command = equal_press, 
        height=1, width=7)
    equal.grid(row=4, column=2)

    clear = Button(window, text=" C ", fg="black", 
        bg="red", command = clear_press, 
        height=1, width=7)
    clear.grid(row=4, column=1)

    # Run program
    window.mainloop()