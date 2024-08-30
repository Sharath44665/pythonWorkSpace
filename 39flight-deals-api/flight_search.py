import requests,json

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.myApiKey = {"apikey":""} # delete this
        self.searchEndpoint = "https://api.tequila.kiwi.com/v2/search"
        self.flyFrom = "LON"


    def makeFlightSearch(self, tomorrowDate="11/11/2023", sixMonthDate="03/03/2024", flyTo="PAR"):
        parameters= {
            "fly_from" : self.flyFrom,
            "fly_to" :flyTo,

            "date_from" : tomorrowDate,
            "date_to" : sixMonthDate,
            "limit":50,
            "selected_cabins": "M",
            "curr": "GBP"

        }

        response = requests.get(url=self.searchEndpoint, headers=self.myApiKey, params=parameters )
        response.raise_for_status()

        # with open("deleteMe.json", mode="w") as myFile:
        #     json.dump(obj=response.json(), fp= myFile, indent=4)

        dataList = response.json()["data"]
        minPrice = 999999
        for val in dataList:
            if val["price"] < minPrice:
                minPrice = val["price"]


        # print(response.json())
        print(f"flight search done for {flyTo} ")
        return minPrice
    pass