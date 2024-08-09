ar = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
# ar = [4, 2, 2, 8, 3, 3, 1]

def countSort(ar):
    # find max
    maxVal = max(ar)
    
    # create counterAr
    counterAr = [0 for _ in range(maxVal+1)]

    # count Values
    for val in ar:
        counterAr[val] = counterAr[val]+1
      
    
    #cumilative Sum
    total =0
    for idx in range(1, len(counterAr)):
        total += counterAr[idx]
        counterAr[idx] = total
    
    outputAr = [0 for _ in ar]
    
    for val in ar:
        putIdx = counterAr[val]
        outputAr[putIdx-1] = val
        counterAr[val] = counterAr[val]-1

    print(outputAr)
countSort(ar)

