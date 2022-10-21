import requests

response=requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()
# print(response)

data=response.json()
# print(data)
longitude =data["iss_position"]["longitude"]
latitude=data["iss_position"]["latitude"]

iss_position=(latitude,longitude)
print(iss_position)