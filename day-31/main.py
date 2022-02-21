from tkinter import *
import pandas
import random


def correct():
    if len(words_dict) <= 1:
        print("All Done")
    else:
        words_dict.remove(selection)
        select_card()
        df = pandas.DataFrame(words_dict)
        df.to_csv("data\words_to_learn.csv", index=False)
        print(len(words_dict))


def select_card():
    global flip_timer, selection
    window.after_cancel(flip_timer)
    selection = random.choice((words_dict))
    rand_fr_word = selection["French"]
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=rand_fr_word, fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    eng_translation = selection["English"]
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=eng_translation, fill="white")


BACKGROUND_COLOR = "#B1DDC6"
flip_timer = NONE
known_words = []
words_dict = {}

window = Tk()
window.title("Language Flash")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front)   # position x,y where centre of image will be
title_text = canvas.create_text(400, 150, text="", font=("courier", 40, "italic", "bold"))
word_text = canvas.create_text(400, 300, text="", font=("courier", 68, "bold"))
canvas.grid(column=0, row=0, columnspan=3)

wrong_image = PhotoImage(file="images/wrong.png")
correct_image = PhotoImage(file="images/right.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, pady=0, borderwidth=0, command=select_card)
correct_button = Button(image=correct_image, highlightthickness=0, pady=0, borderwidth=0, command=correct)
wrong_button.grid(row=1, column=0)
correct_button.grid(row=1, column=2)

try:
    data = pandas.read_csv("data/words_to_learn.csv")
    if len(data) < 1:
        data = pandas.read_csv("data/french_words.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    words_dict = data.to_dict(orient="records")
else:
    words_dict = data.to_dict(orient="records")

print(len(words_dict))
select_card()

window.mainloop()
