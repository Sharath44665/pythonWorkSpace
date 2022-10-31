import requests

apiKey=""
api_url="https://api.openweathermap.org/data/2.8/onecall"
# https://api.openweathermap.org/data/2.5/onecall?
# https://api.openweathermap.org/data/2.5/onecall

parameters={
    "lat": 13.340881,
    "lon": 74.742142,
    "appid":apiKey,
    "exclude": "current,minutely,daily"
}
response=requests.get(api_url,params=parameters)
response.raise_for_status()

weatherData=response.json()
# print(weatherData)
hourList=weatherData["hourly"]
for idx in range(11):
    hourValue=hourList[idx]
    weatherValue=hourValue["weather"]
    for val in weatherValue:
        weatherID=val["id"]
        if weatherID < 700:
            print("bring umbrella")
            break
