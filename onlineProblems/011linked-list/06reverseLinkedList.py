class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def displayAll(self):
        headNode = self.head
        print('displayAll')

        while headNode is not None:
            print(headNode.data, end=" ")
            headNode = headNode.next
        print()

    def insertAtLast(self, data):
        headNode = self.head
        newNode = Node(data)

        if headNode is None:
            self.head = newNode
            return

        while headNode.next is not None:
            headNode = headNode.next

        headNode.next = newNode


    def reverseNode(self):
        previousNode = None
        headNode = self.head

        while headNode is not None: # 30 4
            temp = headNode.next # 4
            headNode.next = previousNode  # 30 20 10
            previousNode = headNode #30 20 10
            headNode = temp # 30 4

        self.head = previousNode



demoLink = MyLinkedList()
demoLink.insertAtLast(10)
demoLink.displayAll()
demoLink.insertAtLast(20)
demoLink.insertAtLast(30)
demoLink.insertAtLast(4)
demoLink.displayAll()

demoLink.reverseNode()
demoLink.displayAll()
