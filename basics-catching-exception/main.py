# try:
#     with open("some.txt") as myFile:
#         myFile.read()
# except:
#     print("something went wrong")

# try:
#     with open("data.txt") as dataFile:
#         pass
#     mydict ={"a": "apple"}
#     print(mydict["b"])
# except FileNotFoundError:
#     print("file not found, so file is created")
#     with open("data.txt", mode="w") as myFile:
#         pass
# except KeyError:
#     print("Hey that key not found")

# read the key as errorMsg and print it on console
# try:
#     with open("data.txt") as dataFile:
#         pass
#     mydict ={"a": "apple"}
#     # print(mydict["b"])
#     print(mydict["a"])
# except FileNotFoundError:
#     print("file not found, so file is created")
#     with open("data.txt", mode="w") as myFile:
#         myFile.write("Hello, this is something")
#         pass
# except KeyError as errorMsg: # errorMsg is not key word, its just a variable, can name anything you want
#     print(f"Hey, that key: {errorMsg} not found")
#
# else: # optional
#     # if there is exception following code not work
#     # if there is no exceptions following code will execute
#     with open("data.txt") as myFile:
#         content = myFile.read()
#         print(content)
#
# finally: # optional
#     print("this prints finally")


# raise exception
# try:
#     with open("data.txt") as dataFile:
#         pass
#     mydict = {"a": "apple"}
#     # print(mydict["b"])
#     print(mydict["a"])
# except FileNotFoundError:
#     print("file not found, so file is created")
#     with open("data.txt", mode="w") as myFile:
#         myFile.write("Hello, this is something")
#         pass
# except KeyError as errorMsg:  # errorMsg is not key word, its just a variable, can name anything you want
#     print(f"Hey, that key: {errorMsg} not found")
#
# else:  # optional
#     # if there is exception following code not work
#     # if there is no exceptions following code will execute
#     with open("data.txt") as myFile:
#         content = myFile.read()
#         print(content)
#
# finally:  # optional
#     # print("this prints finally")
#     raise IndexError("index error has been raised by me")


height = float(input("Enter Hieght: "))
weight = int(input("Enter weight: "))

if height >3:
    raise ValueError("Human height should not be greater than 3 meters")
bmi = weight/(height*height)
print(bmi)





