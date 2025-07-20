import random
# print("enter the number you guessed")
# num = int(input("enter the number you guessed: \n"))
# print(f"guessed number: {num}");

def computerGuess(num1, num2):
    # print(f"method num1: {num1} num2: {num2}")
    return random.randint(num1, num2)

# actualNum= 5
# n1=0
# n2 = 100
# guessedNo = computerGuess(num1=n1, num2=n2) 
# while(guessedNo != actualNum ):
#     if guessedNo < actualNum:
#         n1 = guessedNo
#     else:
#         n2 = guessedNo
#     guessedNo = computerGuess(num1=n1, num2=n2) 
   
n1 =0
n2 = 10
choice = "n"
while (choice == "n" or choice=="no"):
    computerNo = computerGuess(n1, n2)  

    choice = input(f"computer guessed Number: {computerNo}, is that correct? yes or no:\n").lower()

    if (choice == "yes" or choice =="y"):
        break
    bigSmall = input("current computer guessed number is big  or small number: \n").lower()
    if (bigSmall =="b" or bigSmall=="big" ):
        n2 = computerNo -1
    else:
        n1 = computerNo + 1
    

