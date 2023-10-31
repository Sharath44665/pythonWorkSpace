import  datetime as myDate

now = myDate.datetime.now()
# print(now)  # 2023-10-30 19:14:29.839610
# year = now.year
# day = now.day
# month = now.month
# weekDay = now.weekday()
# print(day)
# print(month)
# print(weekDay)  # 0 - monday, 1 - tuesday, 2 - wednesday ....
# print(year)
# if year == 2023:
#     print("hello world")

dateOfBirth = myDate.datetime(year=1995, month=10, day=25)
print(dateOfBirth)  # 1995-10-25 00:00:00


