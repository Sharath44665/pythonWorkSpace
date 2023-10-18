alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

import art
print(art.logo)

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

def decisionMaker():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "e" or direction == "encode":
        #
        encrypt(text=text, shift=shift)
    else:
        decrypt(text=text, shift=shift)

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    cipherText = ""
    for letter in text:
        if letter not in alphabet:
            cipherText += letter
        else:
            position = alphabet.index(letter)
            shiftedIdx = position + shift

            if shiftedIdx > 25:
                shiftedIdx = shiftedIdx%25 - 1

            cipherText += alphabet[shiftedIdx]
    print(f"encrypted Msg: {cipherText}")


# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# e.g.
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"


##HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'? = hnznqndfynts

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
# if direction == "e" or direction == "encode":
#     encrypt(text=text,shift=shift)
# else:
#     print("bleh")


#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
  #e.g.
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"

def decrypt(text, shift):
    plainText = ""
    for letter in text:
        if letter not in alphabet:
            plainText += letter
        else:

            position = alphabet.index(letter)
            newPosition = position - shift


            plainText += alphabet[newPosition]
    print(f"decoded Msg: {plainText}")

decision = "y"

while decision == "y" or decision == "yes":
    decisionMaker()
    print("-----------------------------------")
    decision = input("would you like to continue, type y for yes:\n")



