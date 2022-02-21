import tkinter

def miles_to_km():
    miles = float(input1.get())
    km = miles * (8 / 5)
    label3.config(text=f"{(km):.2f}")

window = tkinter.Tk()
window.minsize(width=100, height=80)
window.config(padx=50, pady=50)
window.title("Miles to KM")

input1 = tkinter.Entry(width=10, justify="center")
input1.grid(column=1, row=0)
input1.focus()

label1 = tkinter.Label(text="Miles")
label1.grid(column=2, row=0)

label2 = tkinter.Label(text="is equal to: ")
label2.grid(column=0, row=1)

label3 = tkinter.Label()
label3.grid(column=1, row=1)

label4 = tkinter.Label(text="km")
label4.grid(column=2, row=1)

button = tkinter.Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=3)
window.mainloop()