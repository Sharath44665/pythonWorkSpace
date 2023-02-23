
class Person:
    def __init__(self):
        self.next = None

def getMyPositionInLine(p):
    if p.next is None:
        return 1

    return 1+getMyPositionInLine(p.next)

p1 = Person()
p2 = Person()
p3 = Person()
p4 = Person()
p5 = Person()
p6 = Person()
p7 = Person()
p8 = Person()

p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5
p5.next = p6
p6.next = p7
p7.next = p8
# p8.nextLine = None


print(getMyPositionInLine(p1))
