BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import random, pandas, time

CSV_DATA = pandas.read_csv("./data/french_words.csv")
actualRow = 0


def updateText(englishText="", language="French", textOneId=0, textTwoId=0):
    if language == "French":
        canvas.itemconfig(textOneId, text=language, fill="black")
        fillColor = "black"
    else:
        canvas.itemconfig(textOneId, text=language, fill="white")
        fillColor = "white"

    canvas.itemconfig(textTwoId, text=englishText, fill=fillColor)


def getFrenchWordFromCSV():
    global actualRow,flipTimer
    window.after_cancel(flipTimer) # to happen continuously

    actualRow = random.randint(1, len(CSV_DATA.French))

    frenchWord = CSV_DATA.at[actualRow, "French"]
    frenchWord = str(frenchWord)

    canvas.itemconfig(backgroundImg, image=bgImgOne)  # white

    updateText(englishText=frenchWord, language="French", textOneId=textOne, textTwoId=textTwo)

    flipTimer = window.after(3000,func=showEnglishText) # to happen continuously


def showEnglishText():
    englishWord = CSV_DATA.at[actualRow, "English"]
    englishWord = str(englishWord)

    # bgImgTwo = PhotoImage(file="./images/card_back.png") # does not work here
    canvas.itemconfig(backgroundImg, image=bgImgTwo)  # light green

    updateText(englishText=englishWord, language="English", textOneId=textOne, textTwoId=textTwo)
    pass


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flipTimer = window.after(3000, func=showEnglishText)

canvas = Canvas(width=800, height=526, highlightthickness=0)
bgImgOne = PhotoImage(file="./images/card_front.png")  # white
bgImgTwo = PhotoImage(file="./images/card_back.png")  # light green
backgroundImg = canvas.create_image(400, 263, image=bgImgOne)
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

textOne = canvas.create_text(400, 150, text="French", font=("Arial", 25, "italic"))

textTwo = canvas.create_text(400, 283, text=f"English", font=("Arial", 25, "bold"))
getFrenchWordFromCSV()

wrongImg = PhotoImage(file="./images/wrong.png")
wrongButton = Button(image=wrongImg, highlightthickness=0, command=getFrenchWordFromCSV)
wrongButton.grid(row=1, column=0)

rightImg = PhotoImage(file="./images/right.png")
rightButton = Button(image=rightImg, highlightthickness=0, command=getFrenchWordFromCSV)
rightButton.grid(row=1, column=1)

window.mainloop()
