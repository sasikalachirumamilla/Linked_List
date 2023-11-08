class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class DLL:
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
            
    def deleteBegining(self):
        temp=self.head
        self.head=temp.next
        self.head.prev=None
        
    def deleteEnding(self):
        temp=self.head.next
        before=self.head
        while temp.next is not None:
            temp=temp.next
            before=before.next
        before.next=None
        temp.prev=None
        
    def deletePosition(self,pos):
        temp=self.head
        before=self.head
        for i in range(1,pos-1):
            temp=temp.next
            before=before.next
        before.next=temp.next
        temp.next.prev=before
        temp.prev=None
        temp.next=None
            
            
            
L=DLL()
n1=Node(10)
L.head=n1
n2=Node(20)
n1.next=n2
n2.prev=n1
n3=Node(30)
n2.next=n3
n3.prev=n2
n4=Node(40)
n3.next=n4
n4.prev=n3
print("Double Linked List")
L.display()
L.deleteBegining()
L.display()
L.deleteEnding()
L.display()
L.deletePosition(2)
L.display()

