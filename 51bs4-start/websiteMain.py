import requests
from bs4 import BeautifulSoup
import lxml

response = requests.get("https://news.ycombinator.com/news")
# print(response.text) # prints html code of above page
hackerNews =  response.text

mysoup = BeautifulSoup(hackerNews, "lxml")
allSpan = mysoup.find_all(name="span", class_="titleline")
# demo = mysoup.find(name=allSpan)
# print(allSpan.children) # <list_iterator object at 0x7f62f6573580>

print(len(allSpan))
for span in allSpan:
    counter= 0
    for anchor in span.children:
        counter += 1
        if counter == 2:
            continue
        print(f"{counter}{anchor.contents}")



# for anchor in allSpan:
#     print(anchor.getText())