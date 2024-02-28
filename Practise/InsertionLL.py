# Node Creation
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

# LinkedList
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    # insertion at start
    def insertAtStart(self, data):
        newNode = Node(data=data)   # node creation for new data

        newNode.next = self.head
        self.head = newNode

    # insert to make 10->20->30->40 to 10->20->25->30->40
    def insertInLL(self, prevNode,data):
        newNode = Node(data=data)     

        if prevNode is None:
            print("Node is not available...!")
            return
        else:
            newNode.next = prevNode.next
            prevNode.next = newNode
       
    # insertion from end
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

    # print LL
    def printLL(self):
        temp = self.head
        while temp:
            print(str(temp.data), end=" ")
            temp = temp.next            


# Driver code
ll = LinkedList()
ll.insertAtStart(20)
ll.insertAtStart(10)
ll.insertAtEnd(30)
ll.insertAtEnd(40)
ll.insertInLL(ll.head.next, 25)
ll.printLL()