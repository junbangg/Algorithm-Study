from collections import deque
n = int(input())
for _ in range(n):
    n, m = list(map(int, input().split(' ')))
    q = deque()
    nums = list(map(int, input().split(' ')))
    for i, val in enumerate(nums):
        q.append((val, i))
    count = 0
    while True:
        if q[0][0] == max(q, key = lambda x: x[0])[0]:
            count += 1
            if m == q[0][1]:
                print(count)
                break
            else:
                q.popleft()
        else:
            q.append(q.popleft())