class User:
    def __init__(self,name):
        self.name = name
        self.isLoggedIn = False

def isAuthenticatedDecorator(function):
    def wrapperFn(*args,**kwargs):
        if args[0].isLoggedIn == True:
            function(args[0])
    return wrapperFn

@isAuthenticatedDecorator
def createBlogPost(user):
    print(f"This is {user.name}'s new blog post ")

newUser = User("Sharath")
newUser.isLoggedIn = True
createBlogPost(newUser)



