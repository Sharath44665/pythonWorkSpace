age: int
# name: string

age = 17
print(age)


def ageCheck(age:int):
    if age < 18:
        return False
    else:
        return True


if ageCheck(18):
    print("allowed")
else:
    print("not allowed")
