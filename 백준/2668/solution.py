import sys
input = sys.stdin.readline

N = int(input())
firstRow = [i for i in range(1, N+1)]
secondRow = [int(input()) for _ in range(N)]
answer = set()

def dfs(index, comb1, comb2):
    comb1.add(firstRow[index])
    comb2.add(secondRow[index])
    if secondRow[index] in comb1:
        if comb1 == comb2:
            answer.update(comb1)
        return
    return dfs(secondRow[index], comb1, comb2)

for i in range(N):
    if firstRow[i] not in answer:
        dfs(i, set(), set())

print(len(answer))
for num in sorted(list(answer), reverse = True):
    print(num)
