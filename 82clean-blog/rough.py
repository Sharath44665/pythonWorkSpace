import main
from datetime import datetime, timedelta
jsonData = main.getJasonData()

# for blogHeader in jsonData:
#     print(blogHeader["title"])
#     print(blogHeader["subtitle"])

# calculating date time difference

nowDate = datetime.now()
daysToSubtract = 20
timeDateDiff = timedelta(days=daysToSubtract)
newDiffDate = nowDate-timeDateDiff
mydate = newDiffDate.date()
print(mydate.strftime("%d %b %Y")) # 2024-08-12