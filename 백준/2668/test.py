import sys
input = sys.stdin.readline

N = int(input())
arr = [0]
for _ in range(N):
    arr.append(int(input()))
answer = set()

def dfs(num, first, second):
    first.add(num)
    second.add(arr[num])
    if arr[num] in first:
        if first == second:
            answer.update(first)
        return
    return dfs(arr[num], first, second)

for i in range(1, N+1):
    if i not in answer:
        dfs(i, set(), set())

print(len(answer))
for num in sorted(list(answer)):
    print(num)
