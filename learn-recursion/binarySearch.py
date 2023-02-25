def binarySearch(array, searchItem, firstIdx, lastIdx):
    mid = (firstIdx + lastIdx)//2
    if array[mid] == searchItem:
        return True

    elif searchItem < array[mid]:
        lastIdx = mid-1
    elif searchItem > array[mid]:
        firstIdx = mid+1

    if firstIdx > lastIdx:
        return False
    return binarySearch(array, searchItem, firstIdx, lastIdx)



array = [ 10, 10, 20, 30, 50, 60, 80, 110, 130, 140, 170]

searchItem = 170
firstIdx = 0
lastIdx = len(array)-1

print(binarySearch(array, searchItem, firstIdx, lastIdx))
