def mergeSort(array, firstIdx, lastIdx):
    # mid = None
    if firstIdx < lastIdx:
        mid = (firstIdx+lastIdx)//2

        mergeSort(array, firstIdx, mid)
        mergeSort(array, mid+1, lastIdx)
        merge(array, firstIdx, lastIdx, mid)


def merge(array, firstIdx, lastIdx, mid):
    idxOne = firstIdx
    idxTwo = mid+1
    k=0
    temp = [None]*(lastIdx-firstIdx+1)
    
    while idxOne <= mid and idxTwo <= lastIdx: # 1,20,3
        if array[idxOne]<=array[idxTwo]:
            temp[k]=array[idxOne]
            idxOne += 1
            k += 1
        else:
            temp[k]=array[idxTwo]
            idxTwo += 1
            k += 1

    while idxOne <= mid:
        temp[k]=array[idxOne]
        idxOne += 1
        k += 1

    while idxTwo <= mid:
        temp[k]=array[idxTwo]
        idxTwo += 1
        k += 1

    for idx in range(firstIdx, lastIdx+1):
        array[idx]= temp[idx-firstIdx] # firstIdx is helpful 
        # when we are in right side of the array so that we can adjust temp idx values
        # if firstIdx = 3, lastIdx = 5 temp should be called from temp[0] or temp[1] or temp[2] ...


array = [20,-5,10,3,2,0]
print(array)
mergeSort(array, 0, len(array)-1)
print(array)
