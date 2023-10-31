##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
# with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import pandas, random, smtplib
import datetime as myDate

birthday = pandas.read_csv("birthdays.csv")
birthDayDict = birthday.to_dict()
now = myDate.datetime.now()
fYear = 1985
fday = now.day
fmonth = now.month
name = "Sharath"
reciverMail = "reciever@example.com"

data = ",".join([f"\n{name}", reciverMail, str(fYear), str(fmonth), str(fday)])
# try:
#     with open("birthdays.csv", mode="a") as myFile:
#         myFile.write(data)
# except FileNotFoundError:
#     print("File not exist")

try:
    csvData = pandas.read_csv("birthdays.csv")
    # csvData.drop_duplicates(inplace=True)
    # csvData.to_csv("birthdays,csv",index=False)   # not working

    # get the matching data for today
    csvMonth = csvData[csvData.month == now.month]
    csvDay = csvMonth[csvMonth.day == now.day]
    csvDay = csvDay.to_dict()

    # for index,val in csvData.iterrows():
    #     print(val)

    #get random letter
    choiceList = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    getLetter = random.choice(choiceList)
    # getLetter = "letter_2.txt"

    with open(f"./letter_templates/{getLetter}") as letterFile:
        letterDataList = letterFile.readlines()

    newStringList = []
    # replace [name] with actual value
    for key, val in csvDay["name"].items():
        newString = letterDataList[0].replace("[NAME]", val)
        newStringList.append([newString])
    # print(newStringList)

    # get email addrress
    toEmailList =[]
    for key,val in csvDay["email"].items():
        toEmailList.append(str(val))
    # print(toEmailList)

    # modify newStringList with letter content
    for idx in range(len(newStringList)):
        val = newStringList[idx]
        newStringList[idx] = val + letterDataList[1:]

    # send message to everyone
    userMail = "example@gmail.com"
    appPasswd = input("enter your app password: ")
    # print(newStringList)
    for idx in range(len(newStringList)):
        finalMsg = "".join(newStringList[idx])
        firstIdx = finalMsg.index(",")
        finalName = finalMsg[5:firstIdx]
        if getLetter == "letter_2.txt":
            finalName = finalMsg[4:firstIdx]

        message = f"""Subject: Happy Birthday {finalName}... \n\n{finalMsg}"""
        # print(message)
        # print(toEmailList[idx])
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as mailConnection:
            mailConnection.starttls()
            mailConnection.login(user=userMail, password=appPasswd)
            mailConnection.sendmail(from_addr=userMail,to_addrs=toEmailList[idx],msg=message)
        print("mail sent")

except FileNotFoundError:
    print("File not exist")
