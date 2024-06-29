class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def displayNodes(self):
        headNode = self.head
        while headNode is not None:
            print(headNode.data)
            headNode = headNode.next

    def insertAtBegin(self, data):
        headNode = self.head
        newNode = Node(data)
        newNode.next = headNode
        self.head = newNode

    def insertAtLast(self, data):
        headNode= self.head
        newNode= Node(data)

        if headNode is None:
            self.head = newNode
            return

        while headNode.next:
            headNode= headNode.next

        headNode.next = newNode

    def insertAtLocation(self, data, loc):
        headNode = self.head
        newNode = Node(data)
        counter = 1
        previousNode = None

        if loc == counter:
            self.insertAtBegin(data)
            return

        while counter< loc:
            previousNode = headNode
            headNode= headNode.next
            counter += 1
        # print(previousNode.data)
        # print(headNode.data)
        # print(headNode.next)
        previousNode.next = newNode
        newNode.next = headNode




mynode = MyLinkedList()
mynode.insertAtLast("Mon")
mynode.insertAtLast("wed")
mynode.displayNodes()
print("-------")
mynode.insertAtLocation("Tue",2)
mynode.displayNodes()
print("-------")
mynode.insertAtLocation("two",2)
mynode.displayNodes()
print("-------")
mynode.insertAtLocation("one",1)
mynode.displayNodes()


