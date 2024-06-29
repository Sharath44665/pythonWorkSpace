
def groupAnagram(words):
    myDict = {}
    resultWord = []
    for val in words:
        w = "".join(sorted(val))
        if w in myDict:
            myDict[w].append(val)
        else:
            myDict[w]=[val]

    for key, val in myDict.items():
        # print(myDict[key])
        resultWord.append(myDict[key])
    return resultWord

words = ["tea", "eat", "bat", "ate", "arc", "car"]
print(groupAnagram(words)) #[['tea', 'eat', 'ate'], ['bat'], ['arc', 'car']]
