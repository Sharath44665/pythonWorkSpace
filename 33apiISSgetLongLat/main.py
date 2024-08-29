# please note that calculating night time day time is wrong.
#  also maybe calculating my head is wrong
# https://github.com/Sharath44665/pythonWorkSpace/tree/main/Solution_issoverhead


MY_LAT = 12.971599
MY_LONG = 77.594566
import requests
from datetime import  datetime
responseISS  = requests.get("http://api.open-notify.org/iss-now.json")
# print(response) # <Response [200]>
# print(response.status_code)
responseISS.raise_for_status()
jsonData = responseISS.json()
# print(jsonData)
# print(jsonData["iss_position"])
issLatitude = float(jsonData["iss_position"]["latitude"])
issLongitude = float(jsonData["iss_position"]["longitude"])
# print(lat)
# print(longitud)

parameters = {
    "lat":MY_LAT,
    "lng": MY_LONG,
    "formatted":0

}
def checkSunriseSunsetMyLocation():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunriseHour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunsetHour = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    return [sunriseHour, sunsetHour]
# print(sunrise.split("T")[1].split(":")[0])
# print(sunset) 
def checkISSHead(mylat, mylong):
    if (issLatitude > (mylat - 5) or issLatitude < (mylat + 5) ) and (issLongitude > (mylong - 5) or issLongitude < (mylong + 5) ):
        return True
    return False

def checkNight():
    timeNow = datetime.now()
    currentHour = timeNow.hour
    myHours = checkSunriseSunsetMyLocation()
    sunriseHour = myHours[0]
    sunsetHour = myHours[1] # get sunset
    if currentHour > sunsetHour or currentHour < sunriseHour :
        return True
    return False

if checkISSHead(MY_LAT,MY_LONG):
    if checkNight():
        print("its dark")
    else:
        print("its day")


timeNow = datetime.now()
# print(timeNow.hour)