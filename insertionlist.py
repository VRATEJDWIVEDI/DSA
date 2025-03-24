#this program is insert node at the second address of the linkedlist
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

node1=Node(10)
node1=Node(20)
node1=Node(30)
node1=Node(40)

node1.next=node2
node2.next=node3
node3.next=node4

head=node1
new_node=Node(25)
position=2
if position==0:
    new_node.next=head
    head=new_node
else:
    current=head
for current in range(position-1):
    if current is None or current.next is None:
        #if position is out of bounds
        print("position is out of range")
    exit()
    current=current.next
new_node.next=current.next
current.next=new_node
current=head
while current:
    print(current.data,end=">>>")
    current=current.next
    print("none")
