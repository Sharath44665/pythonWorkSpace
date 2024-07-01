class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None

    def displayAll(self):
        headNode = self.head

        while headNode is not None:
            print(headNode.data, end=" ")
            headNode = headNode.next

        print("\n\n")


    def insertAtBeginning(self, data):
        newNode = Node(data)

        headNode = self.head
        if headNode is None:
            self.head = newNode
            return

        newNode.next = headNode
        self.head = newNode


    def reverseLinkedList(self):
        previousNode = None
        headNode = self.head

        while headNode is not None:
            temp = headNode.next
            headNode.next = previousNode
            previousNode = headNode
            headNode = temp

        self.head = previousNode


demoLink = MyLinkedList()
demoLink.insertAtBeginning(10)
demoLink.displayAll()

demoLink.insertAtBeginning(20)
demoLink.insertAtBeginning(30)
demoLink.insertAtBeginning(40)
demoLink.insertAtBeginning(50)

demoLink.displayAll()

demoLink.reverseLinkedList()
demoLink.displayAll()



