import time
currentTime = time.time()
print(currentTime)

def speed_calc_decorator(function):
    def wrapperFunction():
        startTime = time.time()
        function()
        endTime = time.time()

        print(f"{function.__name__} run speed: {endTime-startTime} ")

    return wrapperFunction

@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i

@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i

fast_function()
slow_function()