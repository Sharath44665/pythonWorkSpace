class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None


    def displayNodes(self):
        getNodes = self.head

        while getNodes is not None:
            print(getNodes.data)
            getNodes = getNodes.next


    def insertAtBegin(self, data):
        headNode = self.head
        newNode = Node(data)
        newNode.next = headNode
        self.head = newNode

    def insertAtEnd(self, data):
        # list is empty
        headNode = self.head
        newNode = Node(data)

        if headNode is None:
            self.head = newNode
            return

        while headNode.next:
            headNode = headNode.next

        headNode.next = newNode


#
myNode = MyLinkedList()
myNode.insertAtEnd("Mon")
myNode.insertAtEnd("Tue")
myNode.insertAtBegin("Sun")

myNode.insertAtEnd("Wed")
myNode.insertAtBegin("Sat")

myNode.displayNodes()


