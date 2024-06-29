def groupElements(inputLists):
    outputLists = []
    index = 0

    for i in range(len(inputLists[0])):
        outputLists.append([])
        for j in range(len(inputLists)):
            outputLists[index].append(inputLists[j][ index])
        index = index + 1

    a, b, c = outputLists[0], outputLists[1], outputLists[2]

    return [a, b, c]

inputLists = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
print(groupElements(inputLists)) # [[10, 40, 70], [20, 50, 80], [30, 60, 90]]
