import sys
input = sys.stdin.readline

def dfs(letter, cnt):
    global answer
    if cnt == K:
        temp = 0
        for i in range(len(unlearned)):
            flag = True
            for j in range(len(unlearned[i])):
                if not visited[ord(unlearned[i][j]) - 97]:
                    flag = False
                    break
            if flag:
                temp += 1
        answer = max(answer, temp)
        return
    for c in range(letter, 26):
        if not visited[c]:
            visited[c] = True
            dfs(c, cnt + 1)
            visited[c] = False

# 입력
N, K = map(int, input().split())
solved = False
answer = 0
# 예외처리
if K < 5:
    solved = True
elif K == 26:
    answer = N
    solved = True
# antic 빼기
K -= 5

visited = [False] * 26
for c in 'antic':
    visited[ord(c)-97] = True

unlearned = []
for _ in range(N):
    unlearned.append(input()[4:-4])

if solved:
    print(answer)
    exit(0)
dfs(0, 0)
print(answer)