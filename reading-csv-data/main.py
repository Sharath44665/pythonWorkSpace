# with open("weather_data.csv") as weatherFile:
#     weatherData = weatherFile.readlines()
#     print(weatherData)

import csv
with open("weather_data.csv") as weatherFile:
    weatherData = csv.reader(weatherFile)

    # for row in weatherData:
    #     print(row)

    # getting Temperature from weatherData
    # temperature = []
    # for row in weatherData:
    #     if row[1] != "temp":
    #         temperature.append(row[1])
    #
    # print(temperature)

import pandas
csvData = pandas.read_csv("weather_data.csv")
# print(csvData)
# printing temperature
# tempData  = csvData["temp"]
# print(tempData)

# dataDict = csvData.to_dict()
# print(dataDict)

temperatureList = csvData["temp"].tolist()

# print(temperatureList)
# calculate avg temperature:
total = 0
# for val in temperatureList:
#     total+= val
# total = sum(temperatureList)
# avgTemp = total/len(temperatureList)
# print(f"average temperature : {avgTemp} ")
# or
# avgTempTwo = csvData["temp"].mean()
# print(f"avgTempTwo: {avgTempTwo}")

# getting the max temp
# maxTemp = csvData["temp"].max()
# print(f"max temperature: {maxTemp}")

# ways to get data from the column
# conditionData = csvData["condition"]
# print(conditionData) # or
# print(csvData.condition)

# get single row
# mondayRow = csvData[csvData["day"] == "Monday"]
# print(mondayRow)

# getting the day of week having max temperature
# maxTempDay = csvData[csvData["temp"] == csvData["temp"].max()]
# print("max temp day")
# print(maxTempDay)

# getting only condition from monday row
# mondayRow = csvData[csvData.day == "Monday"]
# conditionCol = mondayRow.condition
# print(conditionCol)

# get monday column with farhanite temperature
# mondayRow = csvData[csvData.day == "Monday"]
#
# mondayTemp = mondayRow.temp[0] #getting the value of a cell
# mondayFarhanite = (mondayTemp*9/5)+32
# print(mondayFarhanite)
# print(tempCol)

# create dataframe from scratch
dataDict = {
    "students": ["Amy", "James", "Sharath"],
    "scores": [76, 75, 65 ]
}

studentData = pandas.DataFrame(dataDict)
print(studentData)
studentData.to_csv("studentData.csv")



