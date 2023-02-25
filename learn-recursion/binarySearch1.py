def binarySearch(array, searchItem, firstIdx, lastIdx):
    if firstIdx > lastIdx:
        return False

    mid = (firstIdx + lastIdx)//2

    if searchItem == array[mid]:
        return True
    elif searchItem < array[mid]:
        return binarySearch(array, searchItem, firstIdx, mid-1)

    return binarySearch(array, searchItem, mid+1, lastIdx)

array = [ 10, 10, 20, 30, 50, 60, 80, 110, 130, 140, 170]

searchItem = 55
firstIdx = 0
lastIdx = len(array)-1

print(binarySearch(array, searchItem, firstIdx, lastIdx))
