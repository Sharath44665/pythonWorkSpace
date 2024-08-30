from bs4 import BeautifulSoup
import requests

# The code below will not work for the live website because the HTML has changed.
# For scraping the live site see: https://gist.github.com/TheMuellenator/941a8d6bfc555dbc7c939d2c3720a87d
# response = requests.get("https://news.ycombinator.com/")

# This code will fetch data from the static practice website that I've created for you:
response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')

# Find all articles, identified by <a> tags with the class "storylink"
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []

# Iterate over each article tag found
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

# Find all <span> tags with the class "score" and extract the upvote count
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])