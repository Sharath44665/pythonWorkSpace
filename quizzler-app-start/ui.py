from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quizBrain: QuizBrain):
        self.quiz=quizBrain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.scoreLable = Label(text="Score: 0", foreground="white", background=THEME_COLOR)
        self.scoreLable.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, highlightthickness=0, background="white")
        # self.canvas.config(background=THEME_COLOR)
        self.questionText = self.canvas.create_text(125, 150,
                                                    width=250,
                                                    text="bleh bleh ",
                                                    font=("Arial", 16, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        trueImage = PhotoImage(file="images/true.png")
        self.trueButton = Button(image=trueImage)
        self.trueButton.grid(row=2, column=0)

        falseImage = PhotoImage(file="images/false.png")
        self.falseButton = Button(image=falseImage)
        self.falseButton.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text=self.quiz.next_question()
        self.canvas.itemconfig(self.questionText, text=q_text)
