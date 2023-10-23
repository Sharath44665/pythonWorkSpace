class Animal:
    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print("inhale, exhale")


# class Fish:
#     def swim(self):
#         print("moving in water")

class Fish(Animal): #inheritance

    def __init__(self):
        super().__init__() # inheriting super class properties

    def breathe(self):
        super().breathe()
        print("breathing underwater")
    def swim(self):
        print("moving in water")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.eyes)