from tkinter import *
from datetime import datetime
from tkinter import messagebox

root = Tk()
root.title("Number to Words")
root.geometry('1200x700+10+100')
root.resizable(False, False)


def show():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    try:
        value = int(num.get())
        if value > -1:
            words = convert_to_words(value)
            t1.insert(END, f"{dt_string}\t\t\t{value}\t\t{words.capitalize()}\n")
        else:
            messagebox.showerror("showerror", "Invalid Input!\nPlease enter a positive number.")
            clear()
    except ValueError:
        messagebox.showerror("showerror", "Invalid Input!\nPlease enter a valid number.")
        clear()


def clear():
    e1.delete(0, END)
    # t1.delete(1.0, END)

num = StringVar()

def convert_to_words(number):
    # Define lists for the words
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    # Function to convert a number less than 100 into words
    def convert_below_100(num):
        if num < 10:
            return ones[num]
        elif num < 20:
            return teens[num - 10]
        else:
            return tens[num // 10] + " " + ones[num % 10]

    # Function to convert a number less than 1000 into words
    def convert_below_1000(num):
        if num < 100:
            return convert_below_100(num)
        else:
            if num % 100 == 0:
                return ones[num // 100] + " hundred"
            else:
                return ones[num // 100] + " hundred and " + convert_below_100(num % 100)

    # Handle special case for zero
    if number == 0:
        return "zero"

    # Convert the number based on its magnitude (thousands, millions, etc.)
    result = ""
    magnitudes = ["", "thousand", "million", "billion", "trillion", "quadrillion"]
    magnitude_index = 0

    while number > 0:
        chunk = number % 1000
        if chunk != 0:
            result = convert_below_1000(chunk) + " " + magnitudes[magnitude_index] + " " + result
        number //= 1000
        magnitude_index += 1

    return result.strip()

Label(root,text="Enter a Number:", font=('helvetica 12 bold')).place(x=10,y=10)
Label(root,text="Datetime:", font=('helvetica 10 bold')).place(x=5,y=85)
Label(root,text="Number:", font=('helvetica 10 bold')).place(x=220,y=85)
Label(root,text="Words:", font=('helvetica 10 bold')).place(x=365,y=85)
e1 = Entry(root, textvariable=num, font=('helvetica 12 bold'), width=26, bg='white')
e1.place(x=150,y=10)
e1.focus()
Button(root, text='Submit', font=('helvetica 10 bold'), width=10, command=show).place(x=150,y=50)
Button(root, text='Clear', font=('helvetica 10 bold'), width=10, command=clear).place(x=260,y=50)
t1 = Text(root, width=132, height=30,font=('sans-serif 12 bold'))
t1.place(x=5,y=110)

root.mainloop()
