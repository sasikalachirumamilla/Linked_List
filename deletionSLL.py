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
            
    def delete_beginning(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        
    def deleting_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
        
    def delete_position(self,pos):
        prev=self.head
        temp=self.head.next
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
        
        
            

                
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

print("Singly Linked List")
L.display()
print("\n")

print("After Deletion at Beginning")
L.delete_beginning()
L.display()
print("\n")

print("After deletion at Ending")
L.deleting_end()
L.display()

print("Deleting at certain position")
L.delete_position(2)
L.display()
            