# Create Node Class to create new node for entered data
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

# Create the LinkedList class
class LinkedList:
    def __init__(self) -> None:
        self.head = None    # Initially head is pointing at nothing

    def insertAtBegining(self, data):
        # create the node for entered data
        newNode = Node(data)

        # 1. Make newNode.next to point at value self.head is storing
        newNode.next = self.head
        # 2. Store newNode address into self.head
        self.head = newNode

    # Define method to print linkedlist
    def printLinkedList(self):
        # Take temp pointer to traverse through linkedlist
        temp = self.head
        while temp:     # run this untill temp become None
            print(str(temp.data), end=" ")
            temp = temp.next

## Driver code

# Make object of LinkedList class
ll = LinkedList()
ll.insertAtBegining(5)
ll.insertAtBegining(15)
ll.insertAtBegining(25)
ll.insertAtBegining(35)
ll.insertAtBegining(45)
ll.printLinkedList()
