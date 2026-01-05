# Here we will understand the basic of linked list data structure

# creating Nodes 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
node1 = Node(3)
node2 = Node(6)
node3 = Node(8)

# linking the nodes in linked list or creating linked list
node1.next = node2
node2.next = node3

# making the node1 as head 
head = node1

# traversaling in the linked list
def PrintLinkedList(head):
    current = head
    while current != None:
        print(current.data, end = " ")
        current = current.next
  
#  creating the new node at the begning of the linked list
new_node = Node(2)
new_node.next = head
head = new_node

# creting new node at the last of the linked list 

new_node = Node(9)
current = head
while current.next != None:
    current = current.next

current.next = new_node

# creating a new node at the kth index of the linked list 

new_node = Node(7)
current = head
k = 4
for i in range(k-1):
     current = current.next
     
new_node.next = current.next     
current.next = new_node




PrintLinkedList(head)
    


