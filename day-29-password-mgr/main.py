from tkinter import *
from tkinter import messagebox   # Doesn't get import with the '*'
import random
import pyperclip        # for copy to clipboard
import json

default_email = "jonathan_garvin@hotmail.com"
json_file = "data.json"


def generate_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Using list comprehensions     ( new_list = [new_item for item in list] )
    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)

    entry_password.delete(0, END)
    entry_password.insert(0, password)


def add_entry():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    good_to_go = FALSE
    # create new dict for json data
    new_dict = {
                website:
                {
                        "email": email,
                        "password": password
                }
            }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops!", message="No blank fields please!")
    elif len(password) < 8:
        messagebox.showwarning(title="Oops!", message="Password not long enough (min 8 chars)")
    else:
        good_to_go = TRUE

    if good_to_go:
        response = messagebox.askokcancel(title=website, message=f"Username: {email}\nPassword: {password}\n\nSave?")

        if response:
            try:
                with open(json_file, "r") as data_file:
                    try:
                        data = json.load(data_file)                 # Exception check here if file exists but blank
                    except json.decoder.JSONDecodeError:
                        data = {}
            except FileNotFoundError:
                with open(json_file, "w") as data_file:
                    json.dump(new_dict, data_file, indent=4)
            else:
                data.update(new_dict)
                with open(json_file, "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                if check_clip.get() == 1:
                    pyperclip.copy(password)
                entry_website.delete(0, END)
                entry_password.delete(0, END)


def search():
    try:
        with open(json_file, "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="File not found", message="Password file does not exist")
    else:
        website = entry_website.get()
        if entry_website.get() in data:
            messagebox.showinfo(title=website,
                                message=f"Username: {data[website]['email']}\nPassword: {data[website]['password']}")
            entry_website.delete(0, END)
        else:
            messagebox.showwarning(title="Not found", message=f"Couldn't find an entry for {website}")


window = Tk()


window.title("Password Manager")
window.config(pady=50, padx=50)
canvas = Canvas(width=200, height=200)
padlock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)
label_email = Label(text="Email/Username:")
label_email.grid(column=0, row=2)
label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

entry_website = Entry(width=35)
entry_website.grid(column=1, row=1, sticky="EW")
entry_email = Entry(width=35)
entry_email.grid(column=1, row=2, columnspan=2, sticky="EW")
entry_email.insert(0, default_email)
entry_password = Entry(width=21)
entry_password.grid(column=1, row=3, sticky="EW")

button_password = Button(text="Generate Password", width=14, command=generate_password)
button_password.grid(column=2, row=3)
button_add = Button(text="Add", width=36, command=add_entry)
button_add.grid(column=1, row=4, columnspan=2, sticky="EW")
button_search = Button(text="Search", width=14, command=search)
button_search.grid(column=2, row=1, sticky="E")
entry_website.focus()

check_clip = IntVar()
clipboard_check = Checkbutton(text="Copy password to clipboard?", onvalue=1, offvalue=0, variable=check_clip)
clipboard_check.grid(column=1, row=5, sticky="W")
clipboard_check.select()

window.mainloop()
