from flask import Flask
import random

app = Flask(__name__)
num = random.randint(0, 9)
print(num)


@app.route("/")
def hello_world():
    return ("<h2>Guess a number between 0 and 9</h2> "
            "<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmh3azljcnVkbWpxaXVndjhzZmt3OWFkZGMwOGF6dXRxd25pYzlsNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Kehzyp9EFa2IYDte8P/giphy.gif'/> ")


# def guess(function):
#     def wrapperFn(*args,**kwargs):
#         if args[0] == num:
#             # function(args[0])
#             return f"<h3>Thats Correct! Guessed Num: {num}</h3>"
#         # elif args[0] > num:
#         #     return "<p>your number is bigger</p>"
#         # elif args[1] < num:
#         #     return "<p>your number is bigger</p>"
#     return wrapperFn
#
# @guess
@app.route("/<int:number>")
def getNum(number):
    if num == number:
        return f"<h3>Thats Correct! Guessed Num: {num}</h3>"
    elif number > num:
        return "<p>your number is bigger</p>"
    elif number < num:
        return "<p>your number is smaller</p>"


if __name__ == "__main__":
    app.run(debug=True)
