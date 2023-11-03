import requests,datetime


APP_ID = input("enter your Application ID: ")
APP_KEY = input("enter your app Key: ")



webHeader = {
    "x-app-id":APP_ID,
    "x-app-key" : APP_KEY
}

todayDate = datetime.datetime.now()
timeFormat = todayDate.strftime("%X")
myFormat = todayDate.strftime("%d/%m/%Y")
# print(timeFormat)
# print(myFormat)


requestBody = {
    "query" : input("Tell me which exercise you did: "),
    "gender":"female",
    "weight_kg":72.5,
    "height_cm":167.64,
    "age":30
}
exerciseEndpoints = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=exerciseEndpoints,headers=webHeader, json=requestBody)
exerciseData = response.json()


exerciseList = exerciseData["exercises"]
finalList = []

authorizationHeader ={
    "Authorization": "Basic bleh bleh bleh"
}
for val in exerciseList:
    finalList.append({
        "date" : myFormat,
        "time" : timeFormat,
        "exercise" : val["name"],
        "duration": val["duration_min"],
        "calories": val["nf_calories"]
    })

# adding data to sheet
sheetyEndpoint = "https://api.sheety.co/6528310ba568f8dce1c56797433c6ba8/workoutTracking/workouts"
# # https://api.sheety.co/6528310ba568f8dce1c56797433c6ba8/workoutTracking/workouts
#
# sheetyResponse = requests.get(url=sheetyEndpoint)
# print(sheetyResponse.text)


for val in finalList:
    # print(val)
    body ={
        "workout": val
    }
    sheetyResponse = requests.post(url=sheetyEndpoint, json=body, headers=authorizationHeader )
    print(sheetyResponse.text)


