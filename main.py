from tkinter import *

top = Tk()

top.geometry('224x310')
top.title('Calculator')

# calculation of characters inputed
def calculation():
    try:
        # if blank or only one element, pass
        if number_entry.get() == "" or check_one_element(number_entry.get()):
            pass
        else:
            calc = number_entry.get()
            calc = replace_x_operator(calc)
            calc = eval(remove_leading_zeros(calc))
            clear()
            number_entry.insert(END, calc)
    # if calculation error, display error message
    except SyntaxError:
        error_message = "ERROR - click 'Clear'"
        clear()
        number_entry.insert(END, error_message)

# clear all characters at option of the user
def clear():
    number_entry.delete(0, END)

# remove last character at option of the user
def backspace():
    number_entry.delete(len(number_entry.get())-1, END)

# remove leading zeros
def remove_leading_zeros(string):
    arr = string.split(' ')
    arr1 = [i.lstrip('0') for i in arr]
    new_string = ' '.join(arr1)
    return new_string

# change 'x' operator to '*' operator
def replace_x_operator(string):
    arr = string.split(' ')
    arr1 = [ '*' if i == 'x' else i for i in arr]
    new_string = ' '.join(arr1)
    return new_string

# if only one number or operator (total 1 element) in entry widget, return True
def check_one_element(string):
    arr = string.split(' ')
    return len(arr) == 1

# entry widget
number_entry = Entry(top, width=24)
number_entry.grid(column=0, row=0, sticky=W, columnspan=3, padx=5, pady=5)

# buttons for calculator
btn0 = Button(top, text='/', height=2, width=5, command=lambda: number_entry.insert(END, ' / '))
btn0.grid(column=3, row=0, sticky=W, padx=5, pady=5)

btn1 = Button(top, text='7', height=2, width=5, command=lambda: number_entry.insert(END, '7'))
btn1.grid(column=0, row=1, sticky=W, padx=5, pady=5)

btn2 = Button(top, text='8', height=2, width=5, command=lambda: number_entry.insert(END, '8'))
btn2.grid(column=1, row=1, sticky=W, padx=5, pady=5)

btn3 = Button(top, text='9', height=2, width=5, command=lambda: number_entry.insert(END, '9'))
btn3.grid(column=2, row=1, sticky=W, padx=5, pady=5)

btn4 = Button(top, text='x', height=2, width=5, command=lambda: number_entry.insert(END, ' x '))
btn4.grid(column=3, row=1, sticky=W, padx=5, pady=5)

btn5 = Button(top, text='4', height=2, width=5, command=lambda: number_entry.insert(END, '4'))
btn5.grid(column=0, row=2, sticky=W, padx=5, pady=5)

btn6 = Button(top, text='5', height=2, width=5, command=lambda: number_entry.insert(END, '5'))
btn6.grid(column=1, row=2, sticky=W, padx=5, pady=5)

btn7 = Button(top, text='6', height=2, width=5, command=lambda: number_entry.insert(END, '6'))
btn7.grid(column=2, row=2, sticky=W, padx=5, pady=5)

btn8 = Button(top, text='-', height=2, width=5, command=lambda: number_entry.insert(END, ' - '))
btn8.grid(column=3, row=2, sticky=W, padx=5, pady=5)

btn9 = Button(top, text='1', height=2, width=5, command=lambda: number_entry.insert(END, '1'))
btn9.grid(column=0, row=3, sticky=W, padx=5, pady=5)

btn10 = Button(top, text='2', height=2, width=5, command=lambda: number_entry.insert(END, '2'))
btn10.grid(column=1, row=3, sticky=W, padx=5, pady=5)

btn11 = Button(top, text='3', height=2, width=5, command=lambda: number_entry.insert(END, '3'))
btn11.grid(column=2, row=3, sticky=W, padx=5, pady=5)

btn12 = Button(top, text='+', height=2, width=5, command=lambda: number_entry.insert(END, ' + '))
btn12.grid(column=3, row=3, sticky=W, padx=5, pady=5)

btn13 = Button(top, text='0', height=2, width=13, command=lambda: number_entry.insert(END, '0'))
btn13.grid(column=0, row=4, sticky=W, columnspan=2, padx=5, pady=5)

btn14 = Button(top, text='.', height=2, width=5, command=lambda: number_entry.insert(END, '.'))
btn14.grid(column=2, row=4, sticky=W, padx=5, pady=5)

btn15 = Button(top, text='=', height=2, width=5, command=calculation)
btn15.grid(column=3, row=4, sticky=W, padx=5, pady=5)

btn16 = Button(top, text='Clear', height=2, width=21, command=clear)
btn16.grid(column=0, row=5, sticky=W, columnspan=3, padx=5, pady=5)

btn17 = Button(top, text='Del', height=2, width=5, command=backspace)
btn17.grid(column=3, row=5, sticky=W, padx=5, pady=5)

top.mainloop()



