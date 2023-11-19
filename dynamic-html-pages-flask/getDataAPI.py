import requests

def getDataFromAPI(userName):
    parameters = {
        "name": {userName}
    }
    response = requests.get(url="https://api.agify.io/",params= parameters)
    response.raise_for_status()
    jsonData = response.json()
    # response.close()

    return jsonData
def getGender(userName):
    parameters = {
        "name":userName
    }
    response = requests.get(url="https://api.genderize.io/", params=parameters)
    response.raise_for_status()
    genderData = response.json()
    return  genderData
# getDataFromAPI()