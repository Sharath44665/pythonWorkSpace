import requests,smtplib,time
from datetime import datetime

MY_LAT = 13.340881 # Your latitude
MY_LONG = 74.742142 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

print(sunrise)
print(sunset)
print(time_now.hour)
print(type(time_now.hour))

myEmail="someone@noreply.com"
myPasswd="hello world" # app passwd of gmail
recieverEmail="reciever@noreply.com"

if MY_LAT<=iss_latitude <= MY_LAT+5 and MY_LONG<=iss_longitude <= MY_LONG+5:
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        for _ in range(3):
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=myEmail, password=myPasswd)
                connection.sendmail(from_addr=myEmail, to_addrs=recieverEmail,
                                    msg="subject: ISS is over head!!! \n\n Please look into the sky")
            time.sleep(60)

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



