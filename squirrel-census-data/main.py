import pandas
csvData = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
sqColor = csvData[csvData["Primary Fur Color"] == "Gray"].count()
# print(type(sqColor["Primary Fur Color"]))
greyCounter = sqColor["Primary Fur Color"]

blackColor = csvData[csvData["Primary Fur Color"] == "Black"].count()
blackColorCounter = blackColor["Primary Fur Color"]

redColor = csvData[csvData["Primary Fur Color"] == "Cinnamon"].count()
redColorCounter = redColor["Primary Fur Color"]

myData = {
    "furColor" : ["black", "grey", "red"],
    "count": [ int(blackColorCounter), int(greyCounter), int(redColorCounter)]
}

counterData = pandas.DataFrame(myData)
counterData.to_csv("squirrel Count.csv")

# print(counter)
