MY_LATITUDE = 12.971599
MY_LONGITUDE = 77.594566

import requests
import datetime as myDate

parameters = {
    "lat":MY_LATITUDE,
    "lng":MY_LONGITUDE,
    "formatted": 0
}

# see below for params
# response = requests.get(url=f"https://api.sunrise-sunset.org/json?lat={parameters['lat']}&lng={parameters['lng']}")
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
jsonData = response.json()

# print(jsonData)
sunrise = jsonData["results"]["sunrise"]
sunset = jsonData["results"]["sunset"]

now = myDate.datetime.now()
time = now.time()

print(now)      # 2023-10-31 18:00:28.991485
# Format the following line as required
print(sunrise)  # 2023-10-31T00:41:47+00:00

# print(time)     # 17:57:13.138068


