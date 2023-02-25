def sumOfNaturalNumbers(num, sum=0):
    if num == 0:
        return sum

    sum = sum+num
    return sumOfNaturalNumbers(num-1, sum)

# num = 5
num = 10
print(sumOfNaturalNumbers(num))
