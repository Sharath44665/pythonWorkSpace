html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
from bs4 import BeautifulSoup
import lxml
soup = BeautifulSoup(html_doc, 'lxml')

head_tag = soup.head
print(head_tag) # <head><title>The Dormouse's story</title></head>
print(head_tag.contents) # [<title>The Dormouse's story</title>]

title_tag = head_tag.contents[0]
print(title_tag)
print(title_tag.contents) # ["The Dormouse's story"]
print(len(soup.contents)) # 1
print(soup.contents[0].name) # html             