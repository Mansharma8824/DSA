# Here we will understand the basic of linked list data structure

# creating Node 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
node1 = Node(3)
node2 = Node(6)
node3 = Node(8)

node1.next = node2
node2.next = node3
head = node1

current = head

while current != None:
    print(current.data, end = " ")
    current = current.next

