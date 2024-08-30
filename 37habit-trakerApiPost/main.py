import requests,datetime, pandas
csvData = pandas.read_csv("./token.csv")
webUrl= csvData.get("webUrl")[0]
TOKEN = csvData.get("TOKEN")[0]
USERNAME = csvData.get("USERNAME")[0]
GRAPH_ID = csvData.get("GRAPH_ID")[0]

userParamerters ={
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# creating user
# response = requests.post(url=webUrl, json=userParamerters)  # requests.POST()
# # response.raise_for_status()
# print(response.url) # https://pixe.la/v1/users
# print(response.text) # {"message":"This user already exist.","isSuccess":false}

# Create a graph definition
# graphConfig ={
#     "id":GRAPH_ID,
#     "name": "Cyclic Graph",
#     "unit": "km",
#     "type" : "float",
#     "color" : "sora"
# }
#



webHeader= {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=f"{webUrl}/{USERNAME}/graphs", json=graphConfig, headers=webHeader)
# print(response.text)
# Get the graph!
# https://pixe.la/v1/users/sharath44665/graphs/graph1.html

now = datetime.datetime(day=28,month=10,year=2023)
todayDate = now.date()

formatDate = todayDate.strftime("%G%m%d")
print(formatDate)

# Post value to the graph
postingConfig = {
    "date":formatDate,
    "quantity":"8.5"
}
#
response = requests.post(url=f"{webUrl}/{USERNAME}/graphs/{GRAPH_ID}", json=postingConfig, headers=webHeader)
print(response.text)

# update a graph
updateEndpoint = f"{webUrl}/{USERNAME}/graphs/{GRAPH_ID}/{formatDate}"

updateConfig={
    "quantity": "6.5"
}

# response = requests.put(url=updateEndpoint, headers=webHeader, json=updateConfig )
# print(response.text)

# Delete the registered "Pixel".

deleteEndpoint = f"{webUrl}/{USERNAME}/graphs/{GRAPH_ID}/{formatDate}"
response = requests.delete(url=deleteEndpoint, headers=webHeader)
print(response.text)

