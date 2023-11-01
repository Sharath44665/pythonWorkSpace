import requests, smtplib
from datetime import datetime

MY_LAT = 12.975400  # Your latitude
MY_LONG = 77.624832  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

closeToLocation = False
# Your position is within +5 or -5 degrees of the ISS position.
myIncreasedLatLong = (MY_LAT + 5, MY_LONG + 5)
myDecreasedLatLong = (MY_LAT - 5, MY_LONG - 5)

if (iss_latitude < myIncreasedLatLong[0] and iss_longitude < myIncreasedLatLong[1]) and (
        iss_latitude > myDecreasedLatLong[0] and iss_longitude > myDecreasedLatLong[1]):
    closeToLocation = True
closeToLocation = True
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
print(response.url)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
timeNow = str(time_now)
nowHour = timeNow.split(" ")[1].split(":")[0]
nowMinute = timeNow.split(" ")[1].split(":")[1]

# adding +5:30 to convert UST
utcHour = int(nowHour) + 5
utcMinute = int(nowMinute) + 30

if utcMinute > 59:
    utcMinute = utcMinute % 60
    utcHour += 1
if utcHour > 23:
    utcHour = utcHour % 24
night = sunset + 2

utcHour = 23
# print(utcHour)
# print(night)


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
def sendMail():
    subject = "Look at the night sky, ISS overhead"
    myMsg = """
Hello Sharath...

International space station is up above the sky, please look up

Good night
    """
    myEmailId = input("enter Your email ID: ")
    myPassword = input("enter your app password: ")
    acceptorMail = input("enter acceptor Mail ID: ")
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as myConnection:
        myConnection.starttls()
        myConnection.login(user=myEmailId, password=myPassword)
        myConnection.sendmail(from_addr=myEmailId, to_addrs=acceptorMail, msg=f"Subject:{subject}\n\n{myMsg} ")
    print("mail sent")


#
if closeToLocation:
    if utcHour >= night or utcHour < sunrise:
        # send mail
        sendMail()
    else:
        print("its day")
