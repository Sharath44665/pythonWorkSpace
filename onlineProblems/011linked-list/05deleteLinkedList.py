class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def displayNodes(self):
        print("\ndisplay:")
        headNode = self.head
        while headNode is not None:
            print(headNode.data, end=" ")
            headNode = headNode.next

    def insertAtBegin(self,data):
        headNode = self.head
        newNode = Node(data)

        if headNode is None:
            self.head = newNode
            return

        newNode.next = headNode
        self.head = newNode

    def deleteNodeBeginning(self, data):
        headNode = self.head

        self.head = headNode.next
        headNode.next = None
        # print("deleted First No")


    def deleteNode(self, data):
        headNode = self.head
        previousNode = None

        # if first one to delele

        if headNode.data == data:
            self.deleteNodeBeginning(data)
            return

        # otherwise
        while headNode.data != data:
            previousNode = headNode
            headNode = headNode.next

        previousNode.next = previousNode.next.next
        headNode.next = None


demoLink = MyLinkedList()
demoLink.insertAtBegin(10)
demoLink.displayNodes()
demoLink.insertAtBegin(20)
demoLink.insertAtBegin(3)
demoLink.insertAtBegin(30)
demoLink.insertAtBegin(40)
demoLink.insertAtBegin(5)
demoLink.insertAtBegin(50)
demoLink.displayNodes()

# delete the first node
demoLink.deleteNode(50)
demoLink.displayNodes()
demoLink.deleteNode(5)
demoLink.displayNodes()
demoLink.deleteNode(3)
demoLink.displayNodes()
demoLink.deleteNode(30)
demoLink.displayNodes()


