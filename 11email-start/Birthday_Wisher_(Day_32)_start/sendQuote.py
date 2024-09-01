import random, smtplib
import datetime as dt

with open("quotes.txt", "r") as myfile:
    lines = myfile.readlines()

someQuote = random.choice(lines)
# print(someQuote)
now = dt.datetime.now()

weekDay = now.weekday()

if weekDay == 6:
    mymail = "user@noreply.com"
    myAppPassword = "some passwd" # app password
    sendToMail = "reciever@noreply.com"

    with smtplib.SMTP("smtp.gmail.com") as myConnection:
        myConnection.starttls()
        myConnection.login(user=mymail, password=myAppPassword)
        myConnection.sendmail(from_addr=mymail, to_addrs=sendToMail,
                              msg=f"Subject: Quote of the Day\n\n {someQuote} ")
