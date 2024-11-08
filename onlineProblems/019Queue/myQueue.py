# front -> used to be delete
# rare -> used to insert
# peek -> get whatever at the front --> not coded because it should print the first val
# dequeue -> delete operation
# enqueue -> insert operation
import random

from tpQueue import front

MAX_SIZE = 6

class Queue:

    def __init__(self):
        self.front =0
        self.rare =0
        self.q =  [0 for _ in range(MAX_SIZE)]

    def enqueu(self, data):
        # print(self.rare)
        # print(MAX_SIZE)
        if self.rare >= MAX_SIZE:
            print("q is full : cant insert")
        else:
            self.q[self.rare] = data
            self.rare += 1
            print(f"inserted {data}")

    def deleteQ(self):

        if self.q[self.front] == 0:
            print("Empty: Queue have no data")
        else:
            data = self.q[self.front]
            idx  =0
            while idx < len(self.q)-1: # [83, 37, 81, 1, 81, 19]
                if self.q[idx]== 0:
                    self.rare -= 1
                    if self.rare >= 0:
                        self.q[self.rare] = 0
                    print(f"{data}: just got deleted.")
                    return
                self.q[idx] = self.q[idx +1]
                idx += 1
            self.rare -= 1
            self.q[self.rare] = 0


            print(f"{data}: just got deleted.")


    def show(self):
        print(self.q)


def getData():
    data = random.randint(1, 99)
    return  data
myQ = Queue()


myQ.enqueu(getData())
myQ.show()
myQ.enqueu(getData())
myQ.show()
myQ.enqueu(getData())
myQ.show()
myQ.enqueu(getData())
myQ.show()
myQ.enqueu(getData())
myQ.show()
myQ.enqueu(getData())
myQ.show()
# myQ.enqueu(getData())
# myQ.show()
myQ.deleteQ()
myQ.show()
myQ.deleteQ()
myQ.show()
myQ.deleteQ()
myQ.show()
myQ.deleteQ()
myQ.show()
myQ.deleteQ()
myQ.show()
myQ.deleteQ()
myQ.show()
myQ.deleteQ()
myQ.show()
myQ.enqueu(getData())
myQ.show()
myQ.deleteQ()
myQ.show()
myQ.deleteQ()
myQ.show()
myQ.enqueu(getData())
myQ.show()




