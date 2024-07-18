arr =  [7, 3, 10,9, 12, 11]

arrLength = len(arr)

for i in range(0, arrLength-1):
    checkSwap = False

    for j in range(0,arrLength-i-1):
        if arr[j]> arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            checkSwap = True
    if checkSwap is False:
        break


print(arr)


