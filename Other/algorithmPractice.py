#using another data structure
def unique(s):
    dic = {}
    for i in s:
        if i not in dic:
            dic[i] = 1
        else:
            return False
    return True

#without using another data structure
# use bit operation?

def bit_unique(s):
    check = 0
    for c in s:
        bit = ord(c)
        if (check & (1 << bit)) > 0:
            return False
        check = (check | (1 << bit))
    return True

def permutation(s1,s2):
    dic = {}
    for c in s2:
        if c not in dic:
            dic[c] = 1
        else:
            dic[c] += 1
    for c in s1:
        if c in dic:
            if dic[c] == 0:
                return False
            dic[c] -= 1
        return False
    return True

def replace_space(s):
    replace = "%20"
    output = ""
    tokens = s.split()
    tokens.reverse()
    for _ in range(len(tokens)):
        temp = tokens.pop()
        if(len(tokens) != 0):
            output += temp+replace
        else:
            output += temp
    return output

def palindrome_permutation(s):
    count = [0] * 256
    odd = 0
    for i in range(0,len(s)):
        count[ord(s[i])] += 1

    for i in range(0,256):
        if count[i] & 1:
            odd += 1
        if odd>1:
            return False
    return True

def one_away(s1, s2):
    dic = {}
    if len(s1) > len(s2):
        bigger = s1
        smaller = s2
    else:
        bigger = s2
        smaller = s1

    for c in bigger:
        if c not in dic:
            dic[c] = 1
        else:
            dic[c] += 1

    for c in smaller:
        if c not in dic:
            dic[c] = 1
        else:
            dic[c] -= 1

    values = dic.values()

    for n in values:
        edits += n

    return (edits <= 1)

def string_compression(s):
    count = 1
    current = s[0]
    output = ""
    for i in range(1,len(s)):
        if s[i] == current:
            count += 1
        else:
            output += current+str(count)
            count = 1
            current = s[i]
    output += current + str(count)
    return output

def rotate_matrix(mat):
    N = len(mat)
    for x in range(0, int(N/2)):
        for y in range(x,N-1-x):
            #top
            top = mat[x][y]
            #left -> top
            mat[x][y] = mat[N-1-y][x]
            #bottom -> left
            mat[N-1-y][x] = mat[N-1-x][N-1-y]
            #right->bottom
            mat[N-1-x][N-1-y] = mat[y][N-1-x]
            #top->right
            mat[y][N-1-x] = top
    return mat

def displayMatrix( mat ):
    N = len(mat)
    for i in range(0, N):
        for j in range(0, N):
            print (mat[i][j], end = ' ')
        print ("")


def zerofiy(mat,I,J):
    for j in range(len(mat[0])):
        mat[I][j] = 0
    for i in range(len(mat)):
        mat[i][J] = 0

def zero_matrix(mat):
    #check for zero
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                zerofiy(newmat,i,j)
    return newmat

# Driver Code
mat = [[0 for x in range(4)] for y in range(4)]
newmat = [[0 for x in range(4)] for y in range(4)]
mat = [
      [1,0,3,0],
      [4,1,2,2],
      [3,1,4,5],
      [1,1,1,2]
                ]
newmat = [
      [1,2,3,0],
      [0,3,0,1],
      [4,3,1,0],
      [5,4,2,1]
                ]

def zero_flagver(mat):
    row_flag  = [False]*len(mat)
    col_flag = [False]*len(mat[0])

    for i in range(len(row_flag)):
        for j in range(len(col_flag)):
            if mat[i][j] == 0:
                row_flag[i] = True
                col_flag[j] = True

    for i in range(len(row_flag)):
        if row_flag[i] is True:
            mat = zerofy_row(mat,i)
    for j in range(len(col_flag)):
        if col_flag[j] is True:
            mat = zerofy_col(mat,j)

    return mat

def zerofy_row(mat,I):
    for j in range(len(mat)):
        mat[I][j] = 0
    return mat

def zerofy_col(mat,J):
    for i in range(len(mat[0])):
        mat[i][J] = 0
    return mat

def string_rotation(s1,s2):
    length = len(s1)
    if len(s2) == length and length > 0:
        s1s1 = s1 + s1
        return isSubstring(s1s1, s2)
def isSubstring(s1,s2):
    if s1.count(s2) > 0:
        return True
    return False

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        newnode = Node(data)
        if self.head:
            current = self.head
            while(current.next):
                current = current.next
            current.next = newnode
        else:
            self.head = newnode
    def printData(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

    def getLength(self):
        current = self.head
        length = 0
        while(current):
            length += 1
            current = current.next
        return length

    def delete(self, key):
        temp = self.head
        #if key is in head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        #else
        while temp.next is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None






#2.1 Remove Dups
def remove_dups(llist):
    head = llist.head
    temp = head
    count = [0] * llist.getLength()
    while(head is not None):
        count[head.data] += 1
        head = head.next
    while(temp is not None):
        if count[temp.data] > 1:
            llist.delete(temp.data)
        temp = temp.next

#2.1-2 Remove Dups- without buffer
def removedups_nobuffer(head):
    current = head
    while current:
        runner = current
        while runner.next:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            runner = runner.next
        current = current.next

def k_tolast(k):
    length = llist.getLength()-k
    current = llist.head
    for _ in range(length):
        current = current.next

    return current.data

def delete_middle_node(x, head):
    current = head
    if current.data == x:
        return
    while current:
        if current.next is None:
            return
        if current.data == x:
            break
        prev = current
        current = current.next

    prev.next = current.next
    current = None

#2.4
def partition(node, x):
    beforeStart = None
    beforeEnd = None
    afterStart = None
    afterStart = None
    while node:
        lnext = node.next
        node.next = None
        if node.data < x:
            if beforeStart == None:
                beforeStart = node
                beforeEnd = beforeStart
            else:
                beforeEnd.next = node
                beforeEnd = node
        else:
            if afterStart == None:
                afterStart = node
                afterEnd = afterStart
            else:
                afterEnd.next = node
                afterEnd = node
        node = lnext
    if beforeStart == None:
        return afterStart


    beforeEnd.next = afterStart
    return beforeStart


def partition_ll(node, x):
    head = node
    tail = node
    while node:
        nnext = node.next
        if node.data < x:
            node.next = head
            head = node
        else:
            tail.next = node
            tail = node
        node = nnext
    tail.next = None
    return head

def add_ll(l1,l2):
    temp1 = l1.head
    temp2 = l2.head
    result = 0
    for i in range(l1.getLength()):
        result += temp1.data * 10 ** i
        temp1 = temp1.next
    for j in range(l2.getLength()):
        result += temp2.data * 10 ** j
        temp2 = temp2.next
    return result

l1 = LinkedList()
l2 = LinkedList()
a1 = [7,1,6]
a2 = [5,9,2]
for i in a1:
    l1.insert(i)
for i in a2:
    l2.insert(i)

p = LinkedList()
arr = ['r','a', 'c','c','a','r']
for i in arr:
    p.insert(i)

def palindrome_ll(l):
    count = [0] * 256
    head = l.head
    counter = 0
    while head:
        if counter < int(l.getLength() / 2):
            count[ord(head.data)] += 1
        elif counter > int(l.getLength() / 2):
            count[ord(head.data)] -= 1
        head = head.next
        counter += 1
    for i in count:
        if i != 0:
            return False
    return True

def palindrome_stack(l):
    fast = l.head
    slow = l.head
    stack = []
    while fast is not None and fast.next is not None:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    if fast is not None:
        slow = slow.next

    while slow is not None:
        top = stack.pop()
        if top != slow.data:
            return False
        slow = slow.next
    return True

#print(palindrome_ll(p))
print(palindrome_stack(p))
