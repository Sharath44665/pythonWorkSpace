import pandas as pd
data = pd.read_csv("demoExample.csv")
totalLength = len(data["words"])
# print(type(length))
# print(length)

for idx in range(totalLength):
    data.at[idx, "letter Count"] = str(len(data.at[idx, "words"]))
# print(data.at[0,"words"])


print(data)