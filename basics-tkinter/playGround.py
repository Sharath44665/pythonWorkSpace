# work on args and keyword args
# def add(*args):
#     sum = 0
#     for val in args:
#         sum += val
#
#     print(sum)
#
# add(3,4,10)

# def calculate(**kwargs): # kwargs = Key Word Arguments
#     # print(kwargs) # {'add': [1, 2], 'multiply': (2, 3, 4)}
#     sum = 0
#     answer = 1
#     for key,value in kwargs.items():
#
#         if key == "add":
#             for val in value:
#                 sum += val
#
#         if key == "multiply":
#
#             for val in value:
#                 answer *= val
#     return [sum, answer]
#
#
# answer = calculate(add= [1,2])
# print(answer)


class Car:
    def __init__(self, **kwargs):
        self.color = kwargs.get("color")  # getting from dictionary
        self.model = kwargs.get("model")  # if you dont pass model, then it will return None


carOne = Car(color="blue", model="audi")
print(carOne.color)
print(carOne.model)
carTwo = Car(model="innova")
print(carTwo.color) # None
print(carTwo.model)

