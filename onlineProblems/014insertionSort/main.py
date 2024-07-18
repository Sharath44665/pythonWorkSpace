arr = [ 7, 12, 6, 11, 3]
idx = 1

while idx < len(arr):
    prevIdx = idx-1
    tempIdx = idx
    while prevIdx >= 0 and prevIdx != tempIdx:
        if arr[prevIdx] >= arr[tempIdx]:
            arr[prevIdx], arr[tempIdx] = arr[tempIdx], arr[prevIdx]
        tempIdx -= 1
        prevIdx -= 1

    idx += 1

print(arr)



