# segment tree code
import sys

input = sys.stdin.readline

maxvalue = 1024*1024

class maketree :
    
    def __init__(self) :
        self.tree = [0]*(maxvalue*2)
    
    def push(self,where,val) :
        
        #wheretmp : 숫자를 트리 내의 인덱스로 바꿔준 값 
        wheretmp = where + maxvalue - 1
        
        while True :
            if wheretmp < 1 :
                break 
            self.tree[wheretmp] += val
            
            wheretmp = wheretmp // 2
        
    def findrank( self, rank) :
        
        # 첫번째 노트부터 아래로 내려가면서 순서를 찾는다 (tmp:index)
        tmp = 1
        # 현재 노드의 최소 순위 
        tmprank = 0 
        
        while True:
            
            if tmp*2+1 > maxvalue*2 - 1 :
                
                return(tmp - maxvalue + 1)

            if rank <= self.tree[tmp*2] + tmprank :
                tmp = tmp*2
            
            else :
                tmprank += self.tree[tmp*2]
                tmp = tmp*2 + 1
        
N = int(input())

tree1 = maketree()
for i in range(N) :
    input1 = input().rstrip().split(" ")
    
    if input1[0] == '1' :
        x = tree1.findrank( int(input1[1]) )
        tree1.push(x,-1)
        print( x )
        
    elif input1[0] == '2' :
        tree1.push( int(input1[1]), int(input1[2]) )
