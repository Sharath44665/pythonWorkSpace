# def stringReversal(sentence):
#     length = len(sentence)
#     return stringReversalHelper(sentence, length)
#
# def stringReversalHelper(sentence, length, val=""):
#     if length == 0:
#         return val
#     val = val+sentence[length-1]
#     return stringReversalHelper(sentence, length-1, val)
#
#
sentence = "the simple code"
# print(stringReversal(sentence))



def stringReversalHelper(sentence, val=""):
    if sentence =="":
        return val

    val = sentence[0]+val
    return stringReversalHelper(sentence[1:],val)

# e  e+ ht
# he  h+t
# the  t


print(stringReversalHelper(sentence))
