class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class SLL:
    def __init__(self):
        self.head=None
        
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
            print("None")
            
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        
L=SLL()
n1=Node(10)
L.head=n1
n2=Node(20)
n1.next=n2
n3=Node(30)
n2.next=n3
print("LinkedList is:")
L.display()
print("\nReverse of a Linked List is:")
L.reverse()
L.display()
