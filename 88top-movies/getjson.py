import requests,csv


def getJsonData(movieName):
    apiKey = ""
    with open("mytoken.csv", mode="r") as myFile:
        reader = csv.reader(myFile)
        counter = 0
        for row in reader:
            counter += 1
            if counter == 1:
                continue
            apiKey = row[2]

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {apiKey}",
    }

    parameters = {
        "query": movieName
    }

    webUrl = "https://api.themoviedb.org/3/search/movie"

    response = requests.get(url=webUrl, headers=headers, params=parameters )
    response.raise_for_status()
    # print(response.text)
    data = response.json()
    return data

def getDataFromId(movieId):
    apiKey = ""
    with open("mytoken.csv", mode="r") as myFile:
        reader = csv.reader(myFile)
        counter = 0
        for row in reader:
            counter += 1
            if counter == 1:
                continue
            apiKey = row[2]

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {apiKey}",
    }



    apiUrl = f"https://api.themoviedb.org/3/movie/{movieId}"

    response = requests.get(url=apiUrl, headers=headers )
    response.raise_for_status()
    # print(response.text)
    return response.json()