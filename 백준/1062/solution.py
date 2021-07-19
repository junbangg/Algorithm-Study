N, K = map(int, input().split())

if K < 5:
    print(0)
elif K == 26:
    print(N)
K -= 5

visited = [False] * 26
for c in 'antic':
    visited[ord(c)-97] = True

def dfs(letter, cnt):
    pass

for _ in range(N):
    word = input()[4:-4]




    
    