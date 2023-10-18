class DemoUser:
    def __init__(self, userId, userName ):
        self.userId = userId
        self.name = userName
        self.following = 0
        self.followers = 0

    def follow(self, user):
        self.followers += 1
        user.following += 1


# userOne = DemoUser()
# userOne.id = 101
# userOne.name = "Sharath"
#
# userTwo = DemoUser()
# userTwo.id = 102
# userTwo.name = "blah blah"

userOne = DemoUser(101, "Sharath")
userTwo = DemoUser(102, "Priyanka")
print(userOne.name)
print(userTwo.name)

userOne.follow(userTwo)

print(userOne.followers)
print(userOne.following) # 0

print(userTwo.followers) # 0
print(userTwo.following)