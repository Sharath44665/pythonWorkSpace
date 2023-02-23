def recursion(val):
    if val >= 10:
        return val
    return recursion(val+1)

print(recursion(1))
