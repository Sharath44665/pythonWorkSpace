# inputs = eval(input())


# TODO: Create the logging_decorator() function 👇

def logging_decorator(function):
    def wrapperFn(*args, **kwargs):
        function(args[0], args[1], args[2])
        print(f"You called {function.__name__}({args[0]}, {args[1]}, {args[2]})")
        print(f"It returned: {function(args[0], args[1], args[2])}")

    return wrapperFn


# TODO: Use the decorator 👇
@logging_decorator
def a_function(a, b, c):
    return a * b * c


a_function(1,2,3)