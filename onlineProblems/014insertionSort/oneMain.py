import random;

ar = [57, 81, 6, 85, 5, 73, 26, 76]
def insertionSort(ar):

    for idx in range(1, len(ar)):
        
        currentVal = ar[idx]

        while idx > 0 and  ar[idx - 1] > currentVal:
            ar[idx] = ar[idx - 1]
            idx -= 1
        ar[idx] = currentVal
        # print(ar)
    return ar
    

insertionSort(ar)
print(ar)

# [57, 81, 6, 85, 5, 73, 26, 76]
# [6, 57, 81, 85, 5, 73, 26, 76]
# [6, 57, 81, 85, 5, 73, 26, 76]
# [5, 6, 57, 81, 85, 73, 26, 76]
# [5, 6, 57, 73, 81, 85, 26, 76]
# [5, 6, 26, 57, 73, 81, 85, 76]
# [5, 6, 26, 57, 73, 76, 81, 85]


