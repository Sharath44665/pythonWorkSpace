import pandas

myData = pandas.read_csv("./token.csv")
print(myData["sender"].get(0))