import requests,datetime
from  datetime import timedelta
class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.defaultEndpoint = "https://api.tequila.kiwi.com/"
        # https://api.tequila.kiwi.com/
        # delete below line
        self.myHeader = {
            "apikey": ""
        }


    def doSearch(self,searchQuery):
        locationEndpoint = "https://api.tequila.kiwi.com/locations/query"

        parameters ={
            "term": f"{searchQuery}",
            "limit": 2,
            "locale": "en-US",
            "location_types": "airport",
            "active_only": "true"

        }
        # "location_types": "airport"
        # "locale": "en-US",
        response = requests.get(url=locationEndpoint, params=parameters, headers=self.myHeader)
        response.raise_for_status()
        # locationData = response.json()
        return response.json()



    # def searchFlight(self):
    #     today = datetime.datetime.now()
    #     todayFormat = today.strftime("%d/%m/%Y")
    #
    #     nextDate = today + timedelta(days=15)
    #     nextDateFormat = nextDate.strftime("%d/%m/%Y")
    #
    #     parameters = {
    #         "fly_from": "FRA",
    #         "date_from" : f"{todayFormat}",
    #         "date_to" : f"{nextDateFormat}"
    #     }
    #
    #     searchEndpoint = "https://api.tequila.kiwi.com/v2/search"
    #
    #     response = requests.get(url=searchEndpoint, params=parameters, headers= self.myHeader)
    #     print(response.text)
    pass
