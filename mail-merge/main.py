# TODO: Create a letter using starting_letter.txt

with open("./Input/Letters/starting_letter.txt") as letterFile:
    # returns the first line
    content = letterFile.readline()
    # returns rest, with list with its content
    fullContent = letterFile.readlines()
# print(content)
# print(fullContent)


with open("./Input/Names/invited_names.txt") as namesFile:
    nameData = namesFile.readlines()
    idx = 0
    # print(nameData)
    while idx < len(nameData):
        #
        name = nameData[idx]
        # print(name)
        if idx == len(nameData)-1:
            contentValue = content.replace("[name]", name)
        else:
            contentValue = content.replace("[name]", name[:-1])
        # print(contentValue)
        # create and write the first line to name.txt
        with open(f"./Output/ReadyToSend/{name}.txt", mode="w") as writeFile:
            writeFile.write(contentValue)

        # append the rest of the values to name.txt
        with open(f"./Output/ReadyToSend/{name}.txt", mode="a") as writeFile:
            for fullValue in fullContent:
                writeFile.write(fullValue)

        idx += 1

# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
