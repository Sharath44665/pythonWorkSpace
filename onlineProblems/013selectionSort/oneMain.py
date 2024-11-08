ar  = [30, 43, 9, 1, 6, 5]


def selectionSort(ar):

    firstIdx = 0
    lastIdx = len(ar)-1
    maxIdx = 0
    while firstIdx < lastIdx:
        max = ar[firstIdx]
        maxIdx = firstIdx
        for secondIdx in range(firstIdx + 1, lastIdx+1):
            if ar[secondIdx] > max:
                max = ar[secondIdx]
                maxIdx = secondIdx
            if secondIdx == lastIdx:
                ar[maxIdx], ar[lastIdx] = ar[lastIdx], ar[maxIdx]
        lastIdx -= 1
        # print(ar)
    return ar

selectionSort(ar)
print(ar)

# [30, 5, 9, 1, 6, 43]
# [6, 5, 9, 1, 30, 43]
# [6, 5, 1, 9, 30, 43]
# [1, 5, 6, 9, 30, 43]
# [1, 5, 6, 9, 30, 43]
# [1, 5, 6, 9, 30, 43]

