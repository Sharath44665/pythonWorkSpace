import csv

# with open("cafe-data.csv", newline="") as demo:
#     csvReader = csv.reader(demo)
#     data = []
#     for row in csvReader:
#         data.append(row)
#
#
#     print(data)

myData = [['bleh Name', 'blehLocation', '10PM', '3 AM', '☕☕☕☕', '💪💪💪', '🔌']]
with open("cafe-data.csv", "a",) as demo:
    csvWriter = csv.writer(demo)
    csvWriter.writerows(myData)
