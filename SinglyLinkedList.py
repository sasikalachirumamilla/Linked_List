class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class SingleLinkedList:
    def __init__(self):
        self.head=None
        
    def display(self):
        if self.head is None:
            print("LinkedList is Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end="")
                temp=temp.next 
            print("None")
                
L=SingleLinkedList()
n=Node(10)
L.head=n
n1=Node(20)
L.head.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
L.display()