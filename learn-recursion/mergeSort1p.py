def mergeSort(array, firstIdx, lastIdx):
    if firstIdx < lastIdx:
        mid = (firstIdx+lastIdx)//2
        mergeSort(array, firstIdx, mid)
        mergeSort(array, mid+1, lastIdx)
        merge(array, firstIdx, lastIdx, mid)

def merge(array, firstIdx, lastIdx, mid):
    idxOne= firstIdx
    idxTwo= mid+1
    k=0
    temp = [None]*(lastIdx-firstIdx+1)

    while idxOne<=mid and idxTwo<=lastIdx:
        if array[idxOne]<= array[idxTwo]:
            temp[k]=array[idxOne]
            idxOne += 1
            k += 1
        else:
            temp[k]= array[idxTwo]
            idxTwo += 1
            k+=1

    # left over in idxOne
    while idxOne <= mid:
        temp[k]=array[idxOne]
        k += 1
        idxOne += 1

    # left over in idxTwo
    while idxTwo <= lastIdx:
        temp[k] = array[idxTwo]
        idxTwo += 1
        k += 1

    for idx in range(firstIdx, lastIdx+1):
        array[idx] = temp[idx-firstIdx]


array = [20,-5,10,3,2,0]
print(array)
mergeSort(array, 0, len(array)-1)
print(array)
