def palindromeCheck(stringValue):
    if len(stringValue) <= 1:
        return True

    if stringValue[0] == stringValue[-1]:
        stringValue = stringValue[1:]
        stringValue = stringValue[:-1]
        return palindromeCheck(stringValue)

    return False



# stringValue = "abcdcba"
# stringValue = "ab"
stringValue="aaa"
print(palindromeCheck(stringValue))
