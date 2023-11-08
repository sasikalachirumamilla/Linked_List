class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
class DLL:
    def __init__(self):
        self.head=None
        
    def display(self):
        if self.head is None:
            print("Empty Double Linked List")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end="")
                temp=temp.next
            print("None")
            
    def insertBegining(self,data):
        new_node=Node(data)
        temp=self.head
        temp.prev=new_node
        new_node.next=temp
        self.head=new_node
        
    def insertEnding(self,data):
        new_node=Node(data)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp
        
    def insertPosition(self,data,pos):
        new_node=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        new_node.prev=temp
        new_node.next=temp.next
        temp.next.prev=new_node
        temp.next=new_node
        
        
        
L=DLL()
n1=Node(10)
L.head=n1
n2=Node(20)
n1.next=n2
n2.prev=n1
n3=Node(30)
n2.next=n3
n3.prev=n2

print("Double Linked List is:") 
L.display()
print("\nAfter inserting an element at Begining ")       
L.insertBegining(40)
L.display()
print("\nAfter inserting an elenent at End position:")
L.insertEnding(50)
L.display()
print("\nInserting an element at certain position:")
L.insertPosition(60,2)
L.display()
        