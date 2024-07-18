arr = [7, 12, 9, 11, 3]

arrLength = len(arr)

'''
for i in range(0, arrLength -1):
    for j in range(i+1, arrLength):
        if arr[i] > arr[j]:
            temp = arr [i]
            arr[i] = arr[j]
            arr[j] = temp
'''

for i in range(0, arrLength -1):
    for j in range(i+1, arrLength):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
   
print(arr)



