def stringReversal(sentence):
    length = len(sentence)
    return stringReversalHelper(sentence, length)

def stringReversalHelper(sentence, length, val=""):
    if length == 0:
        return val
    val = val+sentence[length-1]
    return stringReversalHelper(sentence, length-1, val)

sentence = "the simple code"
print(stringReversal(sentence))
