arr = [9, 7, 5, 3, 1, 6, 8, 4, 2]

def quickSort(ar):
    stack = [(0, len(ar)-1 )]
    while stack:
        startIdx, endIdx = stack.pop()
        if startIdx >= endIdx:
            continue
        lastIdx = makePartition(ar, startIdx, endIdx)
        stack.append((startIdx, lastIdx -1))
        stack.append((lastIdx + 1, endIdx))

def makePartition(ar, startIdx, endIdx):
    firstIdx = startIdx + 1
    pivot = ar[startIdx]
    lastIdx = endIdx

    while True:
        while firstIdx <= lastIdx and ar[firstIdx] <= pivot:
            firstIdx += 1
        while firstIdx <= lastIdx and ar[lastIdx] > pivot:
            lastIdx -= 1
        
        if firstIdx <= lastIdx:
            ar[firstIdx], ar[lastIdx] = ar[lastIdx], ar[firstIdx]
        else:
            break
    ar[startIdx], ar[lastIdx] = ar[lastIdx], ar[startIdx]
    
    return lastIdx

print(f"before sort: {arr}")
quickSort(arr)
print(f"after sort: {arr}")


