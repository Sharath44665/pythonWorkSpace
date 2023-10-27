from tkinter import *

window = Tk()
window.title(string="Miles to Km Converter")
window.minsize(width=400, height=300)
window.config(padx=50, pady=50)


mileEntryBox = Entry()
mileEntryBox.grid(row=1, column = 2)

mileLabel = Label(text="Miles")
mileLabel.grid(row=1, column = 3)

equalLabel = Label(text="Is equal to : ")
equalLabel.grid(row=3, column = 1)

kmValueLabel = Label(text="0")
kmValueLabel.grid(row=3, column = 2)

kmLabel = Label(text="Km")
kmLabel.grid(row=3,column=4)

calculateButton = Button(text="Calculate")
calculateButton.grid(row=4,column=2)

def calculateMiles():
    mileValue = mileEntryBox.get()
    mileValue = int(mileValue)

    kmValue = mileValue*1.609
    kmValueLabel.config(text=f"{kmValue}")

calculateButton.config(command=calculateMiles)




window.mainloop()