import smtplib,random
import datetime as myDate
now = myDate.datetime.now()
dayOfWeek = now.weekday()
print(dayOfWeek)
with open("quotes.txt") as myFile:
    dataList = myFile.readlines()
    quote = random.choice(dataList)
    # print(quote)
# print(dataList)

sender = "user@noreply.com"
appPasswd = input("enter your app passwd: ")
reciever = "reciever@noreply.me"

sendMessage = f"""Subject:Quote Of the Day


{quote}
"""

with smtplib.SMTP(host="smtp.gmail.com", port=587) as myConnection:
    myConnection.starttls()
    myConnection.login(user=sender,password=appPasswd)
    myConnection.sendmail(from_addr=sender, to_addrs=reciever,msg=sendMessage)

print("message sent")


