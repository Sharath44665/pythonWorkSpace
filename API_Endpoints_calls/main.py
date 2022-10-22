import requests
import datetime as dt

MY_LATITUDE = 13.340881
MY_LONGITUDE = 74.742142
# response=requests.get("http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# # print(response)
#
# data=response.json()
# # print(data)
# longitude =data["iss_position"]["longitude"]
# latitude=data["iss_position"]["latitude"]
#
# iss_position=(latitude,longitude)
# print(iss_position)

# this is required for https://api.sunrise-sunset.org/json
parameters = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
# print(data)
# print(sunrise.split("T")[1].split(":")[0])
timeNow = dt.datetime.now()
print(sunrise)
print(sunset)
print(timeNow.hour)
