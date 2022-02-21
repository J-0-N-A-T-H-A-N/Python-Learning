from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):      # Make sure quiz_brain is of type QuizBrain (from class)
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", font=("courier", 12, "bold"), bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(self.window, bg="white", height=250, width=300, highlightthickness=0, borderwidth=0)
        self.q_text = self.canvas.create_text(150, 125,
                                              text="Questions: ",
                                              width=280,
                                              font=("Arial", 20, "italic"),
                                              fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=30)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_image, highlightthickness=0, borderwidth=0, command=self.check_true)
        self.false_button = Button(image=false_image, highlightthickness=0, borderwidth=0, command=self.check_false)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            new_q = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=new_q)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.q_text, text="You have finished the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def check_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
