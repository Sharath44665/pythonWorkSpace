#This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
import requests,datetime
from datetime import  timedelta
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch

data = DataManager()
cities = data.getResponse()["prices"]
searchFlight = FlightSearch()
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

print(iataCodeList)
# update sheet with iataCode
# data.updateSheet(columnName="iataCode", dataList=iataCodeList)
'''
tomorrowDate = datetime.datetime.now() + timedelta(days=1)
tomorrowDate = tomorrowDate.strftime("%d/%m/%Y")

sixMonthDate = datetime.datetime.now() + timedelta(days= 6*30 )
sixMonthDate = sixMonthDate.strftime("%d/%m/%Y")

# get this from sheet
minPriceList =[]
for flyTo in iataCodeList:
    val = searchFlight.makeFlightSearch(flyTo=flyTo, tomorrowDate=tomorrowDate,sixMonthDate=sixMonthDate)
    # print(f"{flyTo}: {val} ")
    minPriceList.append(val)
# print(minPriceList)
data.updateSheet(columnName="lowestPrice", dataList=minPriceList)
'''










