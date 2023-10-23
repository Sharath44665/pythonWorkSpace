# getFile = open("myFile.txt")
# allContent = getFile.read()
# print(allContent)
# getFile.close()

# reading a file
# with open("myFile.txt") as getFile:
#     allContents = getFile.read()
#     print(allContents)

# writing to a file, if a file doesn't exist, it will create a new file
# with open("myFile.txt", mode="w") as getFile:
#     getFile.write("This is a Linux System")

# appending to a file
# with open("myFile.txt", mode="a") as getFile:
#     getFile.write("\nThis is a something ish")

# read from desktop folder
# with open("../../../Desktop/data.txt") as dataFile:
#     content = dataFile.read()
#     print(content)

with open("/home/sharath/Desktop/data.txt") as dataFile:
    content = dataFile.read()
    print(content)