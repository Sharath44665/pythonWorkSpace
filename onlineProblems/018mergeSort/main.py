from turtledemo.forest import start


def makeMergeSort(arr):
    counter = 1
    length = len(arr)
    while counter < length:
        for startIdx in range(0, length, counter*2 ):
            mid = min(startIdx + counter, length)
            rightIdx = min(mid+counter, length)
            leftArr = arr[startIdx: mid]
            rightArr = arr[mid: rightIdx]

            mergeAndSort(arr, startIdx, leftArr, rightArr)
        counter *= 2


def mergeAndSort(arr, startIdx, leftArr, rightArr):
    sortedArr = []
    i = j = 0

    while i < len(leftArr) and j < len(rightArr):
        if leftArr[i] < rightArr[j]:
            sortedArr.append(leftArr[i])
            i += 1
        else:
            sortedArr.append(rightArr[j])
            j += 1

    sortedArr = sortedArr + leftArr[i:]
    sortedArr = sortedArr + rightArr[j:]

    print(sortedArr)
    idx = 0
    if len(sortedArr) == 1:
        return
    while idx < len(sortedArr):
        arr[startIdx] = sortedArr[idx]
        idx += 1
        startIdx += 1


# arr = [12, 8, 9, 3, 11, 5, 4]

arr = [38, 27, 43, 3, 9, 10, -10, 82, -1]
print(f"before sort: {arr}")
makeMergeSort(arr)
print(f"after sort: {arr}")
