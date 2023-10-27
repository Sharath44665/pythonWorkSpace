# import tkinter
from tkinter import *

window = Tk()
window.title(string="First GUI")
window.minsize(width=500, height=300)
# label
'''
myLabel = Label(text="Sharath", font=("Arial", 24, "bold"))
# myLabel.pack(side="left")
myLabel.pack()

# myLabel["text"] = "First Label"
# myLabel.config(text="renamed Label")

# button
myButton = Button(text="Click me")
myButton.pack()


# def myButtonClick(): # get the value from label and set it to entry
#     # print("click happened")
#     labelText = myLabel["text"]
#     myLabel.config(text="Button got clicked")
#
#     textBox.delete(0,len(textBox.get()))
#
#     textBox.insert(0,string=labelText)

def myButtonClick():
    # enter into entry box and click the button
    # then change the label value
    entryValue = textBox.get()
    myLabel.config(text=entryValue)
    pass


# do something after click
myButton.config(command=myButtonClick)

textBox = Entry()
textBox.pack()
textBox.insert(0, string="Default Value")
'''

myLabel = Label(text="First Label")
# myLabel.pack()
# myLabel.place(x=100, y=0)
myLabel.grid(column=0, row=0)

myButton = Button(text="Click Me")
# myButton.pack()

entryBox = Entry()
# entryBox.pack()



window.mainloop()
