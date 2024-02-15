class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    #   Insert data at start of LL 
    def insertAtStart(self, data):
        # Create a node for entered data
        newNode = Node(data=data)

        # make newNode.next as head
        newNode.next = self.head
        # make head value to store newNode address
        self.head = newNode
    
    #   Insert at end of LL
    def insertAtEnd(self, data):
        # Create node for entered data
        newNode = Node(data=data)
        if not self.head:
            self.head = newNode
        else:
            # Traverse through the LL
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode

    #   Do the reversal of LinkedList
    def reverseLL(self):
        prev = None
        curr = self.head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
    
    #   Print the linked list
    def printLL(self):
        temp = self.head

        while temp:
            print(str(temp.data), end="-->")
            temp = temp.next
    
##   Driver Code
ll = LinkedList()
ll.insertAtEnd(52)
ll.insertAtStart(50)
ll.insertAtEnd(55)
ll.insertAtStart(45)

print("Original Linked List is:")
ll.printLL()
print("\nLinked List after reversal is:")
ll.reverseLL() 
ll.printLL()
