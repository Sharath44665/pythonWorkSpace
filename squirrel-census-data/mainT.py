import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
greySquirrelsCounter = len(data[data["Primary Fur Color"] == "Gray"])
redSquirrelsCounter = len(data[data["Primary Fur Color"]=="Cinnamon"])
blackSquirrelCounter = len(data[data["Primary Fur Color"] =="Black"])

dataDict =  {
    "Fur Color":["grey", "red", "black"],
    "count":[greySquirrelsCounter,redSquirrelsCounter,blackSquirrelCounter]
}

datas = pandas.DataFrame(dataDict)
datas.to_csv("Squirrel Count.csv")