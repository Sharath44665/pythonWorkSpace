#This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
import requests
from data_manager import DataManager
from flight_data import FlightData

data = DataManager()
cities = data.getResponse()["prices"]
# print(cities)

cityList = []
iataCodeList = []
# add all cities to cityList from sheet
for val in cities:
    cityList.append(val["city"])

flightData = FlightData()

# get IATA code from flightData and append it to iatcCodeList
for city in cityList:
    locationsData = flightData.doSearch(city)
    # print(locationsData["locations"][0]["city"]["code"])
    iataCode = locationsData["locations"][0]["city"]["code"]
    iataCodeList.append(iataCode)

# update sheet with iataCode
data.updateSheet(iataCodeList)






