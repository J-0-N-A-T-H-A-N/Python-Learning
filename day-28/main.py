from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    title_label.config(text="Timer", fg=GREEN)
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    if reps == 8:
        title_label.config(text="Break", fg=RED)
        countdown(long_break_secs)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        countdown(short_break_secs)
    else:
        title_label.config(text="Work", fg=GREEN)
        countdown(work_secs)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global reps
    mins = count // 60
    secs = count % 60
    canvas.itemconfig(timer_text, text=f"{mins:02d}:{secs:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = reps // 2
        for _ in range(work_sessions):
            mark = "✔" * work_sessions
        checkmark_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
canvas.grid(column=1, row=1)
string = f"{WORK_MIN:02d}:00"
timer_text = canvas.create_text(100, 130, text=string, font=(FONT_NAME, 32, "bold"), fill=GREEN)

title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
title_label.grid(column=1, row=0)
button_presses = 2
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark_label = Label(fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3)

window.mainloop()

