a = [ 7, 12, 9, 11, 3]

length = len(a)

for i in range(length-1):
    minIdx = 0
    for j in range(i+1, length):
        if a[i] > a[j]:
            minIdx = j

    val = a.pop(minIdx)
    a.insert(i,val) # insert(index, val)
    print(a)
# print(a)

