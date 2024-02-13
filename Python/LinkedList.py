class Node:
    def __init__(self, data):   # Each node contain two elements -->
                                    # 1. Data   2. NextPointer
        self.data = data
        self.next = None        # Initially pointing at None

class LinkedList:
    def __init__(self) -> None:
        self.head = None        # Head initially pointing at None

    def insertAtBegining(self, data):
        # Create a node for newly entered data
        newNode = Node(data)    

        # 1. newNode pointer should point at the value head is stored
        newNode.next = self.head 
        # 2. make head to point at the newNode address
        self.head = newNode
    
    def printLinkedList(self):
        temp = self.head

        while temp: # Execute this loop unless value of temp becomes None
            print(str(temp.data), end = " ")    
            temp = temp.next

# Driver code
ll = LinkedList()
ll.insertAtBegining(5)
ll.insertAtBegining(14)
ll.insertAtBegining(19)
ll.insertAtBegining(35)
ll.printLinkedList()
