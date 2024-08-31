import requests
url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(url)
dummyData = response.json()
for data in dummyData:
    print(data["title"])

# output:

# The Life of Cactus
# Top 15 Things to do When You are Bored
# Introduction to Intermittent Fasting