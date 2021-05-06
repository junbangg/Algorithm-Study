# Python program to find the shortest
# path between a given source cell
# to a destination cell.
 
from collections import deque
ROW = 8 
COL = 8
 
# To store matrix cell cordinates
class Point:
    def __init__(self,x, y):
        self.x = x
        self.y = y
 
# A data structure for queue used in BFS
class queueNode:
    def __init__(self, pt, dist):
        self.pt = pt  # The cordinates of the cell
        self.dist = dist  # Cell's distance from the source
 
# Check whether given cell(row,col)
# is a valid cell or not
def isValid(row, col):
    if row < 0 or row >= ROW or col < 0 or col >= COL:
        return False
    return True
 
# These arrays are used to get row and column
# numbers of 4 neighbours of a given cell
rowNum = [-1, 0, 0, 1]
colNum = [0, -1, 1, 0]
 
# Function to find the shortest path between
# a given source cell to a destination cell.
def BFS(mat, src, dest):
     
    # check source and destination cell
    # of the matrix have value 1
    if mat[src.x][src.y]!=1 or mat[dest.x][dest.y]!=1:
        return -1
     
    visited = [[False for i in range(COL)]
                       for j in range(ROW)]
     
    # Mark the source cell as visited
    visited[src.x][src.y] = True
     
    # Create a queue for BFS
    q = deque()
     
    # Distance of source cell is 0
    s = queueNode(src,0)
    q.append(s) #  Enqueue source cell
     
    # Do a BFS starting from source cell
    while q:
 
        curr = q.popleft() # Dequeue the front cell
         
        # If we have reached the destination cell,
        # we are done
        pt = curr.pt
        if pt.x == dest.x and pt.y == dest.y:
            return curr.dist
         
        # Otherwise enqueue its adjacent cells
        for i in range(4):
            row = pt.x + rowNum[i]
            col = pt.y + colNum[i]
             
            # if adjacent cell is valid, has path 
            # and not visited yet, enqueue it.
            if (isValid(row,col) and
               mat[row][col] == 0 and
                not visited[row][col]):
                visited[row][col] = True
                Adjcell = queueNode(Point(row,col),
                                    curr.dist+1)
                q.append(Adjcell)
     
    # Return -1 if destination cannot be reached
    return -1
 
# Driver code
def main():
    mat = [[0,0,0,0,0,0,0,1],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,1,0,0],
           [0,0,0,0,1,0,0,0],
           [0,0,0,1,0,0,0,1],
           [0,0,1,0,0,0,1,0],
           [0,1,0,0,0,1,0,0],
           [1,0,0,0,0,0,0,0]]
    source = Point(0,0)
    dest = Point(len(mat) - 1,len(mat[0]) - 1)
     
    dist = BFS(mat,source,dest)
     
    if dist!=-1:
        print("Shortest Path is",dist)
    else:
        print("Shortest Path doesn't exist")
main()
