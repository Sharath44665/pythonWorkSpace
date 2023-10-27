from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def startTimer():
    countDown(12)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countDown(counter):
    reps = 0

    minute = counter // 60
    seconds = counter % 60
    # if seconds == 0:
    #     seconds = "00"
    if seconds < 10:
        seconds= f"0{seconds}"

    # while True:
    #     if minute ==0 and seconds =="00":
    #
    #         if reps <3:
    #             print("break 5")
    #         else:
    #             print("break 20")

    canvas.itemconfig(timerText, text=f"{minute}:{seconds}")
    if counter > 0:
        window.after(1000, countDown, counter - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=40, bg=YELLOW)
# def doSomething(thing):
#     print(thing)

# https://tcl.tk/man/tcl8.6/TclCmd/after.htm
# window.after(1000, doSomething, "Hello", )


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatoImg = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomatoImg)  # half of width, half of height
timerText = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
# canvas.pack()
canvas.grid(row=1, column=1)

# countDown(counter=5)

timerNameLable = Label(text="Timer", font=(FONT_NAME, 22, "bold"), fg=GREEN, bg=YELLOW)
timerNameLable.grid(row=0, column=1)

startButton = Button(text="Start", command=startTimer)
startButton.grid(row=2, column=0)

resetButton = Button(text="Reset")
resetButton.grid(row=2, column=2)

checkMarkLabel = Label(text="✔", fg=GREEN, bg=YELLOW)
checkMarkLabel.grid(row=3, column=1)

window.mainloop()
