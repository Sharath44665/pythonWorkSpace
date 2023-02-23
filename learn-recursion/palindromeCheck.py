

def palindromeCheck(stringValue):
    return palindromeHelper(stringValue)
    pass

def palindromeHelper(stringValue):
    if stringValue == "":
        return True

    if stringValue[0] != stringValue[-1]:
        return False

    stringValue = stringValue[:-1]

    return palindromeHelper(stringValue[1:])

stringValue = "abcdcba"
# stringValue = "abcdcbad"
# stringValue = "aaa"
print(palindromeCheck(stringValue))
