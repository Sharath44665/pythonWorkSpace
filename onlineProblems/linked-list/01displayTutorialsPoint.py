class Node:
    def __init__(self, dataVal=None):
        self.data = dataVal
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.headVal = None

    def display(self):
        headNode = self.headVal

        while headNode is not None:
            print(headNode.data)
            headNode = headNode.next


# demo

firstNode = MyLinkedList()
firstNode.headVal = Node("Mon")

anotherNode = Node("Tue")
demoNode = Node("Wed")

firstNode.headVal.next = anotherNode
anotherNode.next =demoNode

firstNode.display()
