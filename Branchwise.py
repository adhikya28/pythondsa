class Node:
    def __init__(self,v):
        self.val=v
        self.next=None
    
def createLL(n):
    head=None
    for i in range(n):
        v=input("Enter v:")
        new_node=Node(v)
        if i==0:
            head=new_node
        else:
            t=head
            while t.next:
                t=t.next
            t.next=new_node
    return head

def show(head):
    t=head
    print("\n List:")
    while t:
        print(t.val,end='->')
        t=t.next
        
def branch(head):
    t=head
    cseh=None
    noncseh=None
    while t:
        if t.val=='CSE':
            if cseh==None:
                cseh=t
                tcse=t
            else:
                tcse.next=t
                tcse=tcse.next
        else:
            if noncseh==None:
                noncseh=t
                tnoncse=t
            else:
                tnoncse.next=t
                tnoncse=tnoncse.next

        t=t.next
    tcse.next=None
    tnoncse.next=None
    print("\n CSE list")
    show(cseh)
    print("\n NonCSE list")
    show(noncseh)

n=int(input("How many nodes:"))
head=createLL(n)
show(head)
branch(head)    
