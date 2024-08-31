class User:
    def __init__(self,name):
        self.name = name
        self.isLoggedIn = False

def isAuthenticatedDecorator(function):
    def wrapperFn(*args,**kwargs):
        # print(args) # (<__main__.User object at 0x7f35a61306e0>,)
        if args[0].isLoggedIn == True:
            function(args[0]) # you can even return this also, it doesnt make any difference
    return wrapperFn

@isAuthenticatedDecorator
def createBlogPost(user):
    print(f"This is {user.name}'s new blog post ")

newUser = User("Sharath")
newUser.isLoggedIn = True
createBlogPost(newUser)



