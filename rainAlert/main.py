import requests
# import os
from twilio.rest import Client

account_sid = ""
auth_token = ""

apiKey = ""
api_url = "https://api.openweathermap.org/data/2.8/onecall"
# https://api.openweathermap.org/data/2.5/onecall?
# https://api.openweathermap.org/data/2.5/onecall

parameters = {
    "lat": 37.7,
    "lon": 71.43,
    "appid": apiKey,
    "exclude": "current,minutely,daily"
}
response = requests.get(api_url, params=parameters)
response.raise_for_status()

weatherData = response.json()
# print(weatherData)
hourList = weatherData["hourly"]
isRain = False
for idx in range(11):
    hourValue = hourList[idx]
    weatherValue = hourValue["weather"]
    for val in weatherValue:
        weatherID = val["id"]
        if weatherID < 700:
            isRain = True
if isRain:
    # print("bring Umbrella")
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Today it will be going to rain, Take Umbrella, Have a great day",
        from_='+895757575',
        to='+3388444333'
    )
    print(message.status)
