import time

BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas, random

toLearn={}
try:
    data=pandas.read_csv("data/wordsToLearn.csv")
except FileNotFoundError:
    originalData = pandas.read_csv("data/french_words.csv")
    toLearn=originalData.to_dict(orient="records")
else:
    toLearn=data.to_dict(orient="records")
# toLearn=data.to_dict()
# print(toLearn)
# toLearn=data.to_dict(orient="records")
currentCard={}

def nextCard():

    # print(currentCard)
    # canvas.config(cardTitle, text="French")
    global currentCard,flipTimer
    myWindow.after_cancel(flipTimer)
    currentCard = random.choice(toLearn)

    canvas.itemconfig(cardTitle, text="French", fill="black")
    canvas.itemconfig(cardWord, text=currentCard["French"], fill="black")
    canvas.itemconfig(cardBackground,image=frontImg)
    flipTimer=myWindow.after(3000, func=flipCard)

def flipCard():
    canvas.itemconfig(cardTitle, text="English", fill="white")
    canvas.itemconfig(cardWord, text=currentCard["English"], fill="white")
    canvas.itemconfig(cardBackground, image=backImg)

def isKnown():
    toLearn.remove(currentCard)
    # print(len(toLearn))
    data=pandas.DataFrame(toLearn)
    data.to_csv("data/wordsToLearn.csv", index=False)
    nextCard()
myWindow = Tk()
myWindow.title("Flashy")
myWindow.config(padx=50,pady=50, background=BACKGROUND_COLOR)

flipTimer=myWindow.after(3000,func=flipCard)

rightImg=PhotoImage(file="images/right.png")
wrongImg=PhotoImage(file="images/wrong.png")
frontImg=PhotoImage(file="images/card_front.png")
backImg=PhotoImage(file="images/card_back.png")

canvas= Canvas(height=526, width=800, highlightthickness=0)

cardBackground=canvas.create_image(400,263, image=frontImg)
canvas.grid(row=0,column=0, columnspan=2)
canvas.config(background=BACKGROUND_COLOR)

cardTitle=canvas.create_text(400,163,text="", font=("Arial",25,"italic"))
# englishLabel=Label(text="lol", font=("Arial",25,"italic"), background="white")
# englishLabel.place(x=350,y=100)
cardWord=canvas.create_text(400,253, text="", font=("Arial",30,"bold"))

rightButton=Button(image=rightImg, highlightthickness=0,)
rightButton.grid(row=1,column=0,)
rightButton.config(command=isKnown)

wrongButton=Button(image=wrongImg, highlightthickness=0)
wrongButton.grid(row=1, column=1)
wrongButton.config(command=nextCard)

nextCard()
myWindow.mainloop()

