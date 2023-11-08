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
L=DLL()
n1=Node(10)
L.head=n1
n2=Node(20)
n1.next=n2
n2.prev=n1
n3=Node(30)
n2.next=n3
n3.prev=n2
L.display()