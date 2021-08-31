dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs():
  result=1
  queue=set([(0,0,board[0][0])])

  while queue: 
    x,y,visited=queue.pop()

    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx<0 or nx>=r or ny<0 or ny>=c:
        continue
      elif board[nx][ny] not in visited:
        next_visited=visited+board[nx][ny]
        queue.add((nx,ny,next_visited))
        result=max(result,len(next_visited))

  return result
  
r,c=map(int, input().split())
board=[]
for i in range(r):
  board.append(list(input()))

print(bfs())