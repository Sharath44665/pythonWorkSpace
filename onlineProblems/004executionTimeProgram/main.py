from time import time

start = time()

word = "Artificial Intelligence"
textList = word.split()
a = ""

for val in textList:
    a += str(val[0]).upper()
print(a)

end = time()

executionTime = end-start
print(f"Execution Time: {executionTime} ")