import requests,json
from data_manager import DataManager

googleSheetEndpoint = "https://api.sheety.co/6528310ba568f8dce1c56797433c6ba8/flightDeals/users"
myHeader = {
    "Authorization": "" # delete this
}
def enterUsers():
    firstName = input("Enter your first name: ")
    lastName = input("enter your last Name: ")
    emailId = input("enter your emailID: ")
    enterEmailIdAgain = input("confirm your emailID one more time: ")

    while emailId != enterEmailIdAgain:
        enterEmailIdAgain = input("did not match, please try again, enter your emailId / press 0 for exit: ")
        if enterEmailIdAgain == "0":
            break

    if emailId == enterEmailIdAgain:
        return {"firstName": firstName, "lastName": lastName, "email": emailId}
    else:
        print("something went wrong")
        return

def getFlightSearch(fromCity= "LON", toCity="IXE"):
    parameters = {
        "fly_from": fromCity,
        "fly_to": toCity,

        "date_from": "9/11/2023",
        "date_to": "3/3/2024",
        "limit": 50,
        "selected_cabins": "M",
        "curr": "GBP"

    }

    myHeaderForFlight ={
        "apikey": ""
    }

    response = requests.get(url="https://api.tequila.kiwi.com/v2/search", headers=myHeaderForFlight, params=parameters)
    response.raise_for_status()
    jsonData = response.json()

    with open("delete.json", mode="w") as myFile:
        json.dump(obj=jsonData,indent=4, fp=myFile)
    # return []

getFlightSearch()
# sheetData=  DataManager()
# sheetData.updateSheet(columnName=)
# userData = enterUsers()
# newDataForSheet = {
#     "user":{
#         "firstName": userData["firstName"],
#         "lastName" : userData["lastName"],
#         "email": userData["email"]
#
#     }
# }
# # response = requests.get(url= googleSheetEndpoint, headers=myHeader)
# response = requests.post(url= googleSheetEndpoint, headers=myHeader,json=newDataForSheet)
#
# print(response.text)





