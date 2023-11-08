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
            
    def insertatBeginning(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
            
    def insertatEnding(self,data):
        new_node=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        
    def insertatPosition(self,data,pos):
        new_node=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        new_node.data=data
        new_node.next=temp.next
        temp.next=new_node
                
L=SLL()
n1=Node(10)
L.head=n1
n2=Node(20)
n1.next=n2
n3=Node(30)
n2.next=n3
n4=Node(40)
n3.next=n4
n5=Node(50)
n4.next=n5

print("Linked List is")
L.display()

print("\nAfter inserting an element at Begining ")
L.insertatBeginning(60)
L.display()

print("\nAfter inserting an element at Ending")
L.insertatEnding(70)
L.display()

print("\nInserting an element at certain position")
L.insertatPosition(80,2)
L.display()

