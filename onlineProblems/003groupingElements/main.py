
def groupElements(inputLists):
    outputLists = []
    addList= []

    idxOne =0
    idxTwo= 0
    totalLength = len(inputLists[0])
    while idxOne < totalLength or idxTwo < totalLength:
        if idxOne > len(inputLists[0]) - 1:
            outputLists.append(addList)
            addList =[]
            idxOne= 0
            idxTwo += 1
        if idxTwo == totalLength:
            break
        addList.append(inputLists[idxOne][idxTwo])
        idxOne += 1
    return outputLists

# outputLists.append(addList)
inputLists = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
print(groupElements(inputLists)) # [[10, 40, 70], [20, 50, 80], [30, 60, 90]]
