def decimalToBinary(num, result=""):
    if num == 0:
        return result

    result = str(num%2)+result

    return decimalToBinary(num//2, result)

# num = 7
num = 5
num = 15
print(decimalToBinary(num))
