import json

website = "hello world"
username = "user@usermail.com"
password = "user@passwd"
newData = {website: {
    "username": username,
    "password": password
}}

# writing into json file
# with open("data.json","w") as myFile:
#     json.dump(newData,myFile, indent=4)


# reading from json file
# with open("data.json", "r" ) as myFile:
#     data=json.load(myFile)
#     print(data)
website = "new web"
newData = {website: {
    "username": username,
    "password": password
}}

# updating to json
with open("data.json", "r") as myFile:
    data = json.load(myFile)  # read old data
    data.update(newData)  # update new data

with open("data.json", "w") as myFile:
    json.dump(data, myFile, indent=4)  # save with updated data in file
