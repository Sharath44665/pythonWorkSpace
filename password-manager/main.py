from tkinter import *
from tkinter import messagebox
from passwordGenerator import generatePassword
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def passwordGenerate():
    passwordEntry.delete(0, END)
    password = generatePassword()
    passwordEntry.insert(0, password)

    pyperclip.copy(password) # copy to clipboard in python

# ---------------------------- SAVE PASSWORD ------------------------------- #

def savePassword():
    website = webUrlEntry.get()
    email = emailEntry.get()
    password = passwordEntry.get()
    # print(website)
    # print(email)
    # print(password)
    emptyError = "not ok"
    if len(website) == 0:
        emptyError = messagebox.showerror(title="Empty Field", message="please enter Website ")

    elif len(email) == 0:
        emptyError = messagebox.showerror(title="Empty Field", message="please enter email ")
    elif len(password) == 0:
        emptyError = messagebox.showerror(title="Empty Field", message="please enter password ")

    isSave = False
    if emptyError != "ok":
        isSave = messagebox.askokcancel(title=website, message=f"these are the details entered\n"
                                                               f"email: {email}\nPassword: {password}\n"
                                                               f"Do you want to save?")

    if isSave:
        with open("passwordData.txt", mode="a") as passwordFile:
            passwordFile.write(f"{website} | {email} | {password} \n")

        webUrlEntry.delete(0, END)
        passwordEntry.delete(0, END)
        webUrlEntry.focus()

    pass


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lockImg = PhotoImage(file="logo.png")
canvas.create_image(100, 145, image=lockImg)

# canvas.pack()
canvas.grid(row=0, column=1)

websiteLabel = Label(text="Website: ")
websiteLabel.grid(row=1, column=0)

webUrlEntry = Entry(width=25)
webUrlEntry.grid(row=1, column=1, columnspan=2)
webUrlEntry.focus()

emailLabel = Label(text="Email/UserName : ")
emailLabel.grid(row=2, column=0)

emailEntry = Entry(width=25)
emailEntry.grid(row=2, column=1, columnspan=2)
emailEntry.insert(0, "sharath@example.com")

passwordLabel = Label(text="Password: ")
passwordLabel.grid(row=3, column=0)

passwordEntry = Entry(width=21)
passwordEntry.grid(row=3, column=1)

generatePasswordButton = Button(text="Generate Password", command=passwordGenerate)
generatePasswordButton.grid(row=3, column=2)

addButton = Button(text="Add Button", width=36, command=savePassword)
addButton.grid(row=4, column=1, columnspan=2)

window.mainloop()
