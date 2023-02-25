def decimalToBinary(num,count, result=0):
    if num == 0:
        return result

    result = ((num%2)*count)+result
    return decimalToBinary(num//2, count*10, result)


num = 233
print(decimalToBinary(num, 1))
