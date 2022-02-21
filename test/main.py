from tkinter import *

def myfunc():
    label.config(text="Hello!")

def add():
    print(number)
    print(a + b)


window = Tk()
window.config(width=200, height=200, pady=50, padx=50)

button = Button(text="Press", command=myfunc)
button.pack()
label = Label(text="")
label.pack()

number = 4
a = 3
b = 4
add()


window.mainloop()
