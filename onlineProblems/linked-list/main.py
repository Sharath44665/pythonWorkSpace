# create linked list and add items
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def appendData(self, nodeData):
        node = Node(nodeData)
        if self.head is None:
            self.head = node
            return
        else:
            self.head = node
            while self.head.next is not None:
                self.head.next = self.head.next
            self.head.data = node.data
            




