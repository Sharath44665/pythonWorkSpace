import pandas as pd

data = pd.read_csv("articles.csv", encoding="latin1")
data["No of Words Article"] = data["Article"].apply(lambda n: len(n.split()))
print(data.head())