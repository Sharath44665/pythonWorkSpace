import requests

# apiKey = input("enter your API key: ")

# parameters ={
#     "appid" : apiKey,
#     "lat": 13.343730,
#     "lon": 74.746643
# }

# response = requests.get(url="https://api.openweathermap.org/data/2.5/weather",params=parameters)
# response.raise_for_status()
# print("everything is ok")

api_key = ""
LATITUDE = 3.154430
LONGITUDE = 101.715103

API_ADDRESS = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(url=API_ADDRESS, params=parameters)
response.raise_for_status()
hourlyList = response.json()["hourly"]
# print(hourlyList)

isRaining = False
for idx in range(12):

    getWeatherList = hourlyList[idx]["weather"]
    weatherDictionary = getWeatherList[0]
    # print(weatherDictionary["id"])

    if weatherDictionary["id"] < 700:
        # print("Get an umbrella, there is rain on the way.")
        isRaining = True
        break

if isRaining:
    # send message via twilio once account get activated
    pass

