def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
'''
def calculate(functionName, num1, num2):
    return functionName(num1,num2)

result = calculate(multiply,2,3)
print(result)
'''
# nested functions

# def outerFunction():
#     print("this is outer function")
#
#     def nestedFunction():
#         print("this is inside nested function")
#
#     nestedFunction()
#
# outerFunction()

# functions can be returned from other functions
def outerFunction():
    print("outer function")

    def innerFunction():
        print("inside inner function")

    return innerFunction

getInnerFn = outerFunction()
getInnerFn()



