BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas, random

data = pandas.read_csv("data/french_words.csv")
# toLearn=data.to_dict()
# print(toLearn)
toLearn=data.to_dict(orient="records")



def nextCard():
    currentCard=random.choice(toLearn)
    # print(currentCard)
    # canvas.config(cardTitle, text="French")
    canvas.itemconfig(cardTitle, text="French")
    canvas.itemconfig(cardWord, text=currentCard["French"])
    pass


myWindow = Tk()
myWindow.title("Flashy")
myWindow.config(padx=50,pady=50, background=BACKGROUND_COLOR)

rightImg=PhotoImage(file="images/right.png")
wrongImg=PhotoImage(file="images/wrong.png")
frontImg=PhotoImage(file="images/card_front.png")

canvas= Canvas(height=526, width=800, highlightthickness=0)
canvas.create_image(400,263, image=frontImg)
canvas.grid(row=0,column=0, columnspan=2) # WTF is this?
canvas.config(background=BACKGROUND_COLOR)

cardTitle=canvas.create_text(400,163,text="", font=("Arial",25,"italic"))
# englishLabel=Label(text="lol", font=("Arial",25,"italic"), background="white")
# englishLabel.place(x=350,y=100)
cardWord=canvas.create_text(400,253, text="", font=("Arial",30,"bold"))

rightButton=Button(image=rightImg, highlightthickness=0,)
rightButton.grid(row=1,column=0,)
rightButton.config(command=nextCard)

wrongButton=Button(image=wrongImg, highlightthickness=0)
wrongButton.grid(row=1, column=1)
wrongButton.config(command=nextCard)

nextCard()
myWindow.mainloop()

