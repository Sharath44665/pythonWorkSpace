import requests
import datetime as myDate
from datetime import timedelta

STOCK = "IBM"
COMPANY_NAME = "IBM"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "demo"
}


def getTodayDate():
    now = myDate.datetime.now()
    todayDate = now.date()
    yesterdayDate = todayDate - timedelta(days=1)
    return str(yesterdayDate)


def getYesterdayDate():
    now = myDate.datetime.now()
    todayDate = now.date()
    yesterdayDate = todayDate - timedelta(days=2)
    # print(yesterdayDate)
    return str(yesterdayDate)

def getStockInfo():
    response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
    response.raise_for_status()
    # print(response.url)
    todayDate = getTodayDate()
    yesterdayDate = getYesterdayDate()
    stockData = response.json()["Time Series (Daily)"]
    openingStockToday = float(stockData[todayDate]["1. open"])

    # print(openingStockToday)
    closingStockYesterday = float(stockData[yesterdayDate]["4. close"])
    # print(closingStockYesterday)

    # percentage increase = (new value - old value) / old value * 100
    percentageIncreaseOrDecrease = (openingStockToday - closingStockYesterday) / closingStockYesterday * 100

    firstLine = ""
    if percentageIncreaseOrDecrease > 0:
        firstLine = f"IBM {percentageIncreaseOrDecrease}⏫ Up"
    else:
        firstLine = f"IBM {percentageIncreaseOrDecrease}⏬ Down"
    return  firstLine


def getNewsOfIBM():
    newsAPIKey = input("enter your News api key: ")
    newParameters = {
        "q" : "IBM",
        "from" : f"{myDate.datetime.now().date()-timedelta(days=1)}",
        "sortBy" : "publishedAt",
        "apiKey" : newsAPIKey
    }

    response = requests.get(url="https://newsapi.org/v2/everything",params=newParameters)
    response.raise_for_status()
    articleList = response.json()["articles"]
    # print(response.url)
    # print(articleList)
    headLine = articleList[0]["title"]
    brief = articleList[0]["description"]
    #
    # print([headLine,brief])
    return [headLine, brief]


# main program starts here
newsList = getNewsOfIBM()

twilioMessage = f"""
{getStockInfo()}
Headline: {newsList[0]}
Brief: {newsList[1]}
"""

print(twilioMessage)
# unable to send twilio message via SMS API, account on hold







