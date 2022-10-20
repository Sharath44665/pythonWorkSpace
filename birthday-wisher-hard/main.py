##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt

import pandas as pd

# 1. Update the birthdays.csv
now=dt.datetime.now()
oldDF=pandas.read_csv("birthdays.csv")
# print(oldDF)
originData=oldDF.to_dict(orient="records")
# print(originData)
getData=originData[0]
getData["name"]="Sharath"
getData["email"]="someone@noreply.com"
getData["year"]=1920
getData["month"]=now.month
getData["day"]=now.weekday()
originData[0]=getData

# print(originData)
newDF=pd.DataFrame(originData) # converting list of dictionaries to DataFrame (pandas)
# print(newDF)
newDF.to_csv("birthdays.csv", header=True, index=False)
# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




