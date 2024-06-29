def findMissingNumbers(n):
    lastNo = n[len(n)-1]
    notFoundNos=[]
    for idx in range(1, lastNo):
        if idx not in n:
            notFoundNos.append(idx)
    return notFoundNos

listOfNumbers = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]
print(findMissingNumbers(listOfNumbers))    # [4, 12, 15]
