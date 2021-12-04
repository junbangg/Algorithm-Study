import sys
input = sys.stdin.readline

N = int(input())
values = [0]
for _ in range(N):
    values.append(int(input()))
answer = set()

def dfs(index, first, second):
    first.add(index)
    second.add(values[index])
    if arr[index] in first:
        if first == second:
            answer.update(first)
        return
    return dfs(values[index], first, second)

for i in range(1, N+1):
    if i not in answer:
        dfs(i, set(), set())

print(len(answer))
for num in sorted(list(answer)):
    print(num)
