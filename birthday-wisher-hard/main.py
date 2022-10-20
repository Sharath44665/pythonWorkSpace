##################### Extra Hard Starting Project ######################
import pandas, random,smtplib
import datetime as dt

import pandas as pd

# 1. Update the birthdays.csv
now = dt.datetime.now()
# oldDF=pandas.read_csv("birthdays.csv")
# # print(oldDF)
# originData=oldDF.to_dict(orient="records")
# # print(originData)
# getData=originData[0]
# getData["name"]="Sharath"
# getData["email"]="someone@noreply.com"
# getData["year"]=1920
# getData["month"]=now.month
# getData["day"]=now.day
# originData[0]=getData
#
# # print(originData)
# newDF=pd.DataFrame(originData) # converting list of dictionaries to DataFrame (pandas)
# # print(newDF)
# newDF.to_csv("birthdays.csv", header=True, index=False)
# 2. Check if today matches a birthday in the birthdays.csv
getDF = pandas.read_csv("birthdays.csv")
newData = getDF.to_dict(orient="records")
newData = newData[0]
month = int(newData["month"])
day = int(newData["day"])
# print(f"{month},{day}, {type(month)} {type(now.month)} ")
if now.month == month and now.day == day:
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
    # actual name from birthdays.csv
    no = random.randint(1, 3)
    with open(f"letter_templates/letter_{no}.txt", mode="r") as myFile:
        getFileData = myFile.readlines()
        getFileData[0] = "Hey Sharath,\n"
        # print(getFileData)
    print(no)
    with open(f"letter_templates/letter_{no}.txt", mode="w") as myFile:
        myFile.writelines(getFileData)
    pass
# 4. Send the letter generated in step 3 to that person's email address.
