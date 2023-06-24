# create a node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# create a linkedlist class
class LinkedList:

    # create default constructor
    def __init__(self):
        self.head = None

    # create a method to check if the list is empty
    def islistEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    # create a method to find the length of a linked list
    def listLength(self):
        currentNode = self.head
        length = 0
        while currentNode != None:
            length += 1
            currentNode = currentNode.next
        return length

    # create a method to insert a node as head
    def insertHead(self,newNode):
        tempNode = self.head
        self.head = newNode
        self.head.next = tempNode
        del tempNode

    # create a method to insert a node at the end of the linked list
    def insertEnd(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    # create a method to insert a node at particular postion of a linked list
    def insertAt(self, newNode, position):
        if position < 0 or position > self.listLength():
            print("Invalid Position")
            return 
        if position == 0:
            self.insertHead(newNode)
            return
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1

    # create a method to delete head of a linked list
    def deleteHead(self):
        if self.islistEmpty() == False:
            previousHead = self.head
            self.head = self.head.next
            previousHead.next = None
        else:
            print("Linked List is empty, delete failed")

    # create a method ot delete end node of a linked list
    def deleteEnd(self):
        lastNode =  self.head
        while lastNode.next != None:
            previousNode = lastNode
            lastNode = lastNode.next
        previousNode.next = None
        del lastNode    

    # create a method to delete a node at a particular position
    def deleteAt(self, position):
        if position < 0 or position >= self.listLength():
            print("Invalid Position")
            return
        if self.islistEmpty() == False:
            if position == 0:
                self.deleteHead()
                return
            currentNode = self.head
            currentPosition = 0
            while True:
                if currentPosition == position:
                    previousNode.next = currentNode.next
                    currentNode.next = None
                    return
                previousNode = currentNode
                currentNode = currentNode.next
                currentPosition += 1

    # create a method to print the all the data in each of the nodes of a linked list
    def printLlist(self):
        if self.head is None:
            print("List is empty")
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

firstNode = Node("biswa")
llist = LinkedList()
llist.insertEnd(firstNode)
secondNode = Node("smita")
llist.insertEnd(secondNode)
thirdNode = Node("bismita")
llist.insertEnd(thirdNode)
fourthNode = Node("biswamita")
llist.insertHead(fourthNode)
fifthNode = Node("sahu")
llist.insertAt(fifthNode, 3)
sixthNode = Node("stranger")
llist.insertEnd(sixthNode)
seventhNode = Node("stranger")
llist.insertAt(seventhNode,3)
llist.deleteEnd()
llist.deleteAt(3)
llist.deleteHead()
llist.printLlist()
print(llist.listLength())
print(llist.islistEmpty())