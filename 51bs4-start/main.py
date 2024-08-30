from bs4 import BeautifulSoup
import lxml

with open("./website.html") as myFile:
    contents = myFile.read()

mysoup = BeautifulSoup(contents, "lxml")
print(mysoup.title) # <title>Angela's Personal Site</title>
print(mysoup.title.name) # title
print(mysoup.title.string) # Angela's Personal Site
print(mysoup.prettify())
print(mysoup.a) # returns first anchor tag // can be u      sed to first li, p etc

allAnchorTags = mysoup.find_all(name="a")
print(allAnchorTags) # returns list of anchor tags

for tag in allAnchorTags:
    if "brewery" in tag.getText().lower():
        print(tag.getText()) # The App Brewery

# printing all hrefs in anchor tag
for tag in allAnchorTags:
    print(tag.get("href"))

## find with id
nameOfUser = mysoup.find(name="h1", id="name")
print(nameOfUser.getText()) # Angela Yu

## find with class

contentHeading = mysoup.find(name="h3", class_="heading")
print(contentHeading) # <h3 class="heading">Books and Teaching</h3>

demoHeader = mysoup.find(name="h3", class_="heading demo")
print(demoHeader) # <h3 class="heading demo">my demo header</h3>

companyUrl = mysoup.select_one(selector="p a") # can be used selector = #idname
print(companyUrl.get("href")) ## only href printed

# all heading having class = heading
allHeadingClass = mysoup.select(".heading")
print(allHeadingClass) # returns list of h3 having ...
