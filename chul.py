class Node:
    def __init__(self,word,mean,next=None):
        self.word=word
        self.mean=mean
        self.next=next

class Linkedlist:
    def __init__(self):
        self.head=None

    def insert(self,node):
        if(self.head==None)or(self.head.word>node.word):
            node.next = self.head
            self.head=node
        else:
            b=self.head
            while(b.next!=None)and(b.next.word<node.word):
                b=b.next
            node.next=b.next
            b.next=node






with open("r/anddict_utf8.TXT") as f:
    line=f.readlines()

a=Linkedlist()
'''
for i in range(len(line)):
    line[i]=line[i].split(" : ")
    node=Node(line[i][0],line[i][1])
    a.insert(node)
'''
print(a.head.word)
