import time

def delayDecorator(function):

    def wrapperFunction():
        time.sleep(2)
        # do something before
        function()
        # do something after
        function()

    return wrapperFunction

@delayDecorator
def sayHello():
    print("Hello")

@delayDecorator
def sayBye():
    print("Bye")

def sayGreetings():
    print("How are you?")

# sayHello() # executes after 2 seconds
# sayGreetings() # executes immediately

decoratedFunction = delayDecorator(sayGreetings) # applying decorator to the function sayGreetings()
decoratedFunction()

