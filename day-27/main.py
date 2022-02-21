import tkinter

def click():
    string = input.get()
    label["text"] = string
`
window = tkinter.Tk()

window.title("First GUI")
window.minsize(width=500, height=350)

label = tkinter.Label(text="This is a label", font=("courier", 14, "bold"))
label.pack()

button = tkinter.Button(width=7, height=1, text="Exit", command=click)
button.pack(side="bottom", pady=20)

input = tkinter.Entry(bg="lightgray", width=10)
input.pack()



window.mainloop()





# def add(*args):
#     print(args)
#     return sum(args)
#
# print(add(1,2,3,4,5,6,7,8,9,10))

# def newadd(**kwargs):
#     return kwargs["c"]
#
# print(newadd(a=1, b=2, c=3))