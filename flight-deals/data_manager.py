import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheetEndpoint = "https://api.sheety.co/6528310ba568f8dce1c56797433c6ba8/flightDeals/prices"
        # delete below Line
        self.authHeader = {
            "Authorization": ""

        }

        pass

    def getResponse(self):
        response = requests.get(url= self.sheetEndpoint, headers=self.authHeader)
        sheetData = response.json()
        print("sheet reponse done")
        return sheetData

    def updateSheet(self,columnName = "iataCode",dataList=[]):
        # print(dataList)
        length = len(self.getResponse()["prices"])

        for idx in range(1, length+1):
            updateSheetEndpoint = f"https://api.sheety.co/6528310ba568f8dce1c56797433c6ba8/flightDeals/prices/{idx + 1}"
            updateConfig = {
                "price": {
                    # "iataCode": f"Testing"
                    columnName: f"{dataList[idx-1]}"
                }
            }

            response = requests.put(url=updateSheetEndpoint, json=updateConfig, headers=self.authHeader)
            response.raise_for_status()
            print(f"writing to {columnName} in google sheet ")
            print(response.text)



