arr = [450, 25, 75, 23, 671, 8, 12]
print(arr)
def radixSort(arr):
    radixArr = [[] for _ in range(10)]
    maxValue = max(arr)
    
    devider = 1

    while maxValue//devider > 0:
        while len(arr) > 0:
            val = arr.pop()
            devideVal = val//devider
            idx = devideVal % 10
            radixArr[idx].append(val)
        
        for bucket in radixArr:
            while len(bucket) > 0:
                bucketVal = bucket.pop()
                arr.append(bucketVal)
        devider = devider*10
    print(arr)

radixSort(arr)




