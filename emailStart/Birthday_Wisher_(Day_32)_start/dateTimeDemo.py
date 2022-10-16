import datetime as dt

now=dt.datetime.now()
year=now.year
month=now.month
weekDay=now.weekday() # 6- sunday, 0- Monday, 1- Tuesday, ... 6- sunday

print(now)
print(year)
print(month)
print(weekDay)

dateOfBirth=dt.datetime(year=2000, month=2, day=15, hour=4)

print(dateOfBirth)