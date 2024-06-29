class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.headNode = None


    def displayNodes(self):
        myheadNode = self.headNode

        while myheadNode is not None:
            print(myheadNode.data)
            myheadNode = myheadNode.next


    def insertAtBegin(self, data):
        myheadNode = self.headNode
        newNode = Node(data)

        newNode.next = myheadNode
        self.headNode = newNode

#
myNode = MyLinkedList()
myNode.headNode = Node("Mon")
second = Node("Tue")
third = Node("wed")

myNode.headNode.next = second
second.next = third

print(f"before insert")
myNode.displayNodes()

myNode.insertAtBegin("Sun")
print(f"after  insert--------")
myNode.insertAtBegin("Sat")
myNode.displayNodes()
