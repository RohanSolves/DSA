# Node Creation
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

# LinkedList
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insertAtEnd(self, data):
        newNode = Node(data=data)

        if self.head is None:   # if LL is empty
            self.head = newNode
            return
        else:
            temp = self.head    
            while temp.next:    # travel until node.next has value
                temp = temp.next
            
            temp.next = newNode # chng next ptr with newNode address

    # reverse LL
    def reverseLL(self):
        prev = None
        temp = self.head

        while temp:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        self.head = prev

    # print LL
    def printLL(self):
        temp = self.head
        while temp:
            print(str(temp.data), end=" ")
            temp = temp.next            

# Driver Code
ll = LinkedList()
ll.insertAtEnd(10)
ll.insertAtEnd(20)
ll.insertAtEnd(30)
ll.insertAtEnd(40)
ll.printLL()
ll.reverseLL()
print("\n")
ll.printLL()