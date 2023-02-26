# not optimized
def fibonacci(number):
    if number <= 1:
        return number
    
    num1 = fibonacci(number-1)
    num2 = fibonacci(number-2)

    return num1+num2


number = 6
# 0 1 1 2 3 5 8
print(fibonacci(number))
